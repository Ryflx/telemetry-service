# Telemetry Dashboard

A Flask-based application that provides both API endpoints and a web frontend for managing contract data and XML records. Perfect for integration with CLM (Contract Lifecycle Management) systems.

## Features

- **Web Dashboard**: Beautiful, responsive frontend with real-time data visualization
- **REST API**: Complete API for contract data and XML management
- **Data Storage**: In-memory storage for contracts and XML data
- **CORS Support**: Ready for cross-origin requests
- **Real-time Updates**: Dashboard auto-refreshes every 30 seconds

## Installation

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Run the application:
```bash
python app.py
```

The application will be available at `http://localhost:5000`

## Frontend Features

### Dashboard (`/`)
- Overview of all data with key metrics
- Recent contract activity
- XML data summary
- API endpoint documentation

### Contract Data (`/contracts`)
- Complete view of all contract records
- Detailed contract information in modals
- Statistics and analytics
- Direct API links

### XML Data (`/xml-data`)
- View all XML records
- Preview XML content
- Download XML files
- Storage statistics

## API Endpoints

### Contract Data

#### Add Contract Data
```http
POST /services/addData
Content-Type: application/json

{
  "user": "user@example.com",
  "use_case": "contract_approval",
  "contract_status": "pending"
}
```

#### Get Specific Contract Status
```http
GET /services/getStatus/<user>/<use_case>
```

#### Get All Contract Statuses
```http
GET /services/getAllStatus
```

### XML Data

#### Add XML Data
```http
POST /services/addXml
Content-Type: application/xml

<contract>
  <id>123</id>
  <status>active</status>
</contract>
```

#### Get XML Data
```http
GET /services/getXmlData/<uid>
```

## Usage Examples

### From CLM System

Your CLM system can post data via HTTP:

```bash
curl -X POST -H "Content-Type: application/json" \
  -d '{"user": "john.doe@example.com", "use_case": "contract_approval", "contract_status": "approved"}' \
  http://your-domain/services/addData
```

### XML Integration

```bash
curl -X POST -H "Content-Type: application/xml" \
  -d '<contract><id>123</id><status>active</status></contract>' \
  http://your-domain/services/addXml
```

## Frontend Navigation

- **Dashboard**: Main overview page with key metrics
- **Contracts**: Detailed contract data management
- **XML Data**: XML record viewing and management
- **API**: Direct link to JSON API endpoints

## Development

The application uses:
- Flask for web framework
- Bootstrap 5 for responsive UI
- Font Awesome for icons
- In-memory storage (data persists only while app is running)

## Deployment

For production deployment, consider:
- Using a proper WSGI server (gunicorn is included)
- Implementing persistent storage (database)
- Adding authentication and authorization
- Setting up proper logging

## License

This project is open source and available under the [MIT License](LICENSE). 