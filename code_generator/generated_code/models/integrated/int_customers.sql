Before writing the DBT integrated SQL for the customers dataset, we need to define the ETL logic. In this scenario, let's assume we have raw data from a CRM system that includes customer information such as name, email, phone number, and address. The ETL logic for this dataset would involve extracting the raw data, transforming it by cleaning and standardizing the data, and finally loading it into a structured database table.

Here is an example of the ETL logic for the customers dataset:

1. Extract: Extract the raw data from the CRM system.

2. Transform:
   a. Clean the data by removing any duplicates or irrelevant information.
   b. Standardize the data by ensuring consistency in formatting (e.g. all names in Title Case, phone numbers in a standardized format).
   c. Enrich the data by adding any missing information (e.g. adding a default country code to phone numbers).
   
3. Load: Load the cleaned and standardized data into a structured database table.

Now, let's write the DBT integrated SQL for the customers dataset:

```sql
-- Create customers table
{% set source_table = 'customers_raw' %}
{% set target_table = 'customers' %}

create table {{ target_table }} as
select
  customer_id,
  concat_ws(' ', upper(substr(first_name,1,1)), lower(substr(first_name,2)) as first_name,
  concat_ws(' ', upper(substr(last_name,1,1)), lower(substr(last_name,2)) as last_name,
  lower(email) as email,
  phone_number,
  address,
  city,
  state,
  postal_code
from {{ source_table }};
```

In this SQL code, we are transforming the raw data from the `customers_raw` table and loading it into the `customers` table. We are cleaning and standardizing the data by formatting the first and last names, converting the email to lowercase, and keeping the phone number, address, city, state, and postal code as is.

You can customize this SQL code further based on your specific ETL requirements and data transformations.