# Django Test Task

This is a test task for a Django project that involves working with currency rates.

# Author

**Olga Pykhova**
- Telegram: [@freedasw](https://t.me/freedasw)

## Test Task Description
The purpose behind this task is to understand your knowledge about system design thought process as well as evaluate your skillset regarding Python, Django, DRF and ability to document written code. 
written code. use PostgreSQL database, use Django, prepare setup instructions
1. Create models: Currency (id, code), RateSource (id, code), CurrencyRate (id, date, rate_source, rate)
2. Make migrations and fill database using fixtures:
   1. Currency: EUR, USD, BTC
   2. RateSource: Bank, Exchange
   3. CurrencyRate: month of random rates for given currencies and rate sources
3. Setup DRF application, implement REST endpoint to retrieve currency rates for a given date and date range (from/to/rate_source)
4. Setup an admin interface, make a custom table-like template for showing currency rates.

| Select rate source: | \\\/ Bank or Exchange (select box for rate source) |
|--------------|----------------------------------------------------|

| Date       | EUR   | USD  | BTC     |
| -----------|-------|------|---------|
| 2023-01-01 | 1.1   | 2.2  | 3.3     |
| 2023-01-02 | 1.2   | 2.3  | 3.4     |
| 2023-01-03 | 1.707 | 1.98 | 3.14159 |
| ...   | ...   | ...  | ...     |
| 2023-01-31   | ...   | ...  | ...     |



## Installation

### Using Docker

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   ```
   
2. **Navigate to the project directory:**
   ```bash
   cd currency_project
   ```
   
3. **Build the Docker images:**
   ```bash
   docker-compose build
   ```
   
4. **Start the containers:**
   ```bash
   docker-compose up
   ```
   
5. **Wait for the containers to start, then apply the migrations:**
   ```bash
   docker-compose exec web python manage.py migrate
   ```

6. **Load the fixtures into the database:**
   ```bash
   docker-compose exec web python manage.py loaddata currency_app/fixtures/currency_fixtures.json
   docker-compose exec web python manage.py loaddata currency_app/fixtures/ratesource_fixtures.json
   docker-compose exec web python manage.py loaddata currency_app/fixtures/currencyrate_fixtures.json
   ```
   
7. **Create a superuser:**
   ```bash
   docker-compose exec web python manage.py createsuperuser
   ```
   
8. **Open a web browser and navigate to:**
   ```bash
    http://localhost:8000/admin/currency_rates/
   ```

## Usage

    1. Log in to the admin interface using the superuser credentials.
    2. Select a rate source (Bank or Exchange) and click the "Submit" button.
    3. View the currency rates in a table format.

Notes

    The project uses PostgreSQL as the database.
    The project is set up to run with Docker and Docker Compose for easy deployment.