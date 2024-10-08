Sure, here is an example of a DBT prepared SQL for the customers dataset with macros for final transformations:

```sql
-- Create a staging table for the customers dataset
{% set staging_columns = ["customer_id", "customer_name", "email", "phone_number", "address"] %}
{% set staging_table = "customers_staging" %}
{% set staging_columns_str = staging_columns | join(", ") %}
CREATE TABLE {{ staging_table }} AS
SELECT
  {{ staging_columns_str }}
FROM
  customers;

-- Create a macro for final transformations
{% macro transform_customers(source_table, destination_table) %}
    {% set destination_columns = ["customer_id", "customer_name", "email", "phone_number", "address"] %}
    {% set destination_columns_str = destination_columns | join(", ") %}
    
    CREATE TABLE {{ destination_table }} AS
    SELECT
      {{ destination_columns_str }}
    FROM
      {{ source_table }};
{% endmacro %}

-- Apply final transformations to create the customers dataset
{% call transform_customers(staging_table, "customers_final") %}
{% endcall %}
```

In this SQL code, we first create a staging table for the customers dataset using a set of predefined columns. We then use a macro called `transform_customers` to define the final transformations for the customers dataset. Finally, we call the macro with the staging table as the source and the destination table name to apply the final transformations and create the customers dataset.