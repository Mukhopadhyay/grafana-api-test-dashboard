# Grafana dashboard for API test data

## TODO

**2023-01-14 05:01:26**

+ [ ] Moving the FastAPI application inside `app` directory inside `src`
+ [ ] Write grafana initialization script
  + [ ] Setting up data sources
  + [ ] Basic panels (e.g., Introductory readme and stuff)

## Setting up the project (for Contributors)
```bash
# Clone the project
git clone git@github.com:Mukhopadhyay/grafana-api-test-dashboard.git

# Create the development virtual environment
python3 -m venv venv_dev

# Installing the dev dependencies
pip3 install -r requirements.dev.txt

# Installing the pre-commit hooks
pre-commit install
```

Temp table query:

```sql
CREATE TABLE IF NOT EXISTS temp
(
    id uuid NOT NULL,
  	ep_name character varying NOT NULL,
    created_at timestamp with time zone NOT NULL,
    url character varying NOT NULL,
    elapsed numeric NOT NULL,
    status_code integer NOT NULL,
    PRIMARY KEY (id)
);
```
