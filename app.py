from flask import Flask, request, jsonify
import os
import xmltodict

app = Flask(__name__)

# Simple in-memory storage using a dictionary
contracts = {}

# Simple storage for a single XML payload
xml_storage = None

@app.route('/services/addData', methods=['POST'])
def add_data():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        # Extract user email as a unique identifier
        # Note: The template variable will be replaced with actual email in your workflow
        user = data.get('user', 'unknown_user')
        
        # Create a key using user and use case
        contract_key = f"{user}_{data.get('use_case', 'unknown')}"
        
        # Store the complete data object
        contracts[contract_key] = data
        
        # Log the update
        print(f"Updated contract status: {data.get('contract_status')} for {contract_key}")
        
        return jsonify({"status": "success", "message": "Data updated"}), 200
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/services/getStatus/<user>/<use_case>', methods=['GET'])
def get_status(user, use_case):
    """Get the current status for a specific user and use case"""
    contract_key = f"{user}_{use_case}"
    
    if contract_key in contracts:
        return jsonify(contracts[contract_key])
    else:
        return jsonify({"error": "Contract not found"}), 404

@app.route('/services/getAllStatus', methods=['GET'])
def get_all_status():
    """Get all contract statuses"""
    return jsonify(contracts)

@app.route('/services/addXml', methods=['POST'])
def add_xml():
    global xml_storage
    try:
        # Get the XML data from the request
        xml_data = request.data
        
        # Validate the XML by attempting to parse it
        xmltodict.parse(xml_data)
        
        # Store the XML data
        xml_storage = xml_data
        
        # Log the update
        print("XML data updated")
        
        return jsonify({"status": "success", "message": "XML data updated"}), 200
    
    except Exception as e:
        return jsonify({"status": "error", "message": f"Invalid XML: {str(e)}"}), 400

@app.route('/services/getXmlData', methods=['GET'])
def get_xml_data():
    """Retrieve and return the stored XML data"""
    if xml_storage:
        try:
            # Parse and unparse the XML to ensure it's well-formed
            parsed_data = xmltodict.parse(xml_storage)
            clean_xml = xmltodict.unparse(parsed_data, pretty=True)
            return clean_xml, 200, {'Content-Type': 'application/xml'}
        except Exception as e:
            return jsonify({"error": "Failed to process XML data", "message": str(e)}), 500
    else:
        return jsonify({"error": "No XML data found"}), 404

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)