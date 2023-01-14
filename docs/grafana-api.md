# Grafana API

Basic authentication, grafana allows for the API to be called using the Username and Password as well, so by default using the `admin` credentials you'd be able to use the HTTP APIs like so.

**BASE URL**: `http://admin:admin@localhost:3000/`

## Data source API

### Get all data sources
`GET /api/datasources`

### Creating new data source
`POST /api/datasources`

**Request body:**
```json
{
    "name": "PostgreSQL",               // Datasource name
    "type": "postgres",                 // Type of database
    "access": "proxy",
    "url": "postgres:5432",             // In this case postgres is the name of the service in docker-compose
    "database": "grafana",              // DB name
    "user": "grafana",                  // DB user name

    "basicAuth": true,                  // Setting Basic authentication
    "basicAuthUser": "admin",           // Basic authentication username
    "secureJsonData": {                 // Data inside this object gets saved as encrypted blob
        "password": "grafana",          // DB password
    },
    "jsonData": {
        "sslmode": "disable",           // SSL mode disabled for DB connection
        "postgresVersion": 1500         // Postgres version
    },
    "isDefault": true                   // Setting the source to default
}
```
