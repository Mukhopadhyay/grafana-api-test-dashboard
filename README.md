# Grafana dashboard for API test data

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white) ![Grafana](https://img.shields.io/badge/grafana-%23F46800.svg?style=for-the-badge&logo=grafana&logoColor=white) ![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=for-the-badge&logo=fastapi)

## TODO

**2023-01-14 05:01:26**

+ [ ] Moving the FastAPI application inside `app` directory inside `src`
+ [x] Write grafana initialization script
  + [x] Setting up data sources
  + [x] Basic panels (e.g., Introductory readme and stuff)
  + [x] Installing a dashboard
+ [ ] Setting up the API call scheduler
+ [x] Write Base CRUD class
+ [ ] Optimizing the endpoint
+ [ ] One table just containing all endpoint informations


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
CREATE TABLE
  public.endpoint (
    id uuid NOT NULL DEFAULT uuid_generate_v4(),
    created_at timestamp without time zone NOT NULL,
    name character varying NOT NULL,
    url character varying NOT NULL,
    elapsed numeric NOT NULL,
    version character varying NULL,
    category character varying NOT NULL,
    status_code integer NOT NULL,
    content_length integer NOT NULL
  );

ALTER TABLE
  public.endpoint
ADD
  CONSTRAINT endpoint_pkey PRIMARY KEY (id)
```
