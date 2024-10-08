To generate the DBT staging SQL for the customers dataset, you can create a staging table in your DBT project and use the `dbt-utils` package to read data from the source. Here is an example of how you can achieve this:

First, install the `dbt-utils` package in your project by running the following command in your terminal:

```bash
dbt deps install
```

Next, create a SQL file in your DBT project directory (e.g., `staging/customers_staging.sql`) with the following code:

```sql
-- Create a staging table for the customers dataset
{% set customers_columns = ["customer_id", "customer_name", "customer_email", "customer_phone"] %}
create table {{ ref('stg_customers') }} as
select
  {{ customers_columns | join(', ') }}
from {{ source('your_source_name', 'customers') }};
```

In the code above, we are creating a staging table called `stg_customers` in the DBT project, based on the `customers` dataset from the source specified by `your_source_name`.

You can now run the staging SQL code by executing the following command in your terminal:

```bash
dbt run --models +staging.customers_staging
```

This will generate the staging table for the customers dataset in your DBT project, using data from the specified source.