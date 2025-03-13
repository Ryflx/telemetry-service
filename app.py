from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# Simple in-memory storage using a dictionary
contract_status = {}

@app.route('/services/addData', methods=['POST'])
def add_data():
    try:
        # Get the JSON data from the request
        data = request.get_json()
        
        # Use contract_id as the key (or create a default one if not provided)
        contract_id = data.get('contract_id', 'default_contract')
        
        # Overwrite any existing data for this contract
        contract_status[contract_id] = data
        
        # Optionally log to console
        print(f"Updated status for {contract_id}: {data.get('status')}")
        
        return jsonify({"status": "success", "message": "Data updated"}), 200
    
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/services/getStatus/<contract_id>', methods=['GET'])
def get_status(contract_id):
    """Get the current status for a specific contract"""
    if contract_id in contract_status:
        return jsonify(contract_status[contract_id])
    else:
        return jsonify({"error": "Contract not found"}), 404

@app.route('/services/getAllStatus', methods=['GET'])
def get_all_status():
    """Get all contract statuses (for dashboard view)"""
    return jsonify(contract_status)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port