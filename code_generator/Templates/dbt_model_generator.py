import os

def generate_dbt_model(generator,prompt):


    # Generate prompts for each layer
    staging_prompt = "Generate the DBT staging SQL for the customers dataset. Read data from the source."
    integrated_prompt = "Generate the DBT integrated SQL for the customers dataset. Apply ETL logic."
    prepared_prompt = "Generate the DBT prepared SQL for the customers dataset. Include macros for final transformations."

    # Generate SQL for staging layer
    staging_sql = generator.generate_code(staging_prompt)
    if staging_sql:
        staging_path = 'generated_code/models/staging/stage_customers.sql'
        os.makedirs(os.path.dirname(staging_path), exist_ok=True)
        with open(staging_path, 'w') as f:
            f.write(staging_sql)
        print(f"Generated staging SQL saved to {staging_path}")
    else:
        print("Failed to generate staging SQL.")

    # Generate SQL for integrated layer
    integrated_sql = generator.generate_code(integrated_prompt)
    if integrated_sql:
        integrated_path = 'generated_code/models/integrated/int_customers.sql'
        os.makedirs(os.path.dirname(integrated_path), exist_ok=True)
        with open(integrated_path, 'w') as f:
            f.write(integrated_sql)
        print(f"Generated integrated SQL saved to {integrated_path}")
    else:
        print("Failed to generate integrated SQL.")

    # Generate SQL for prepared layer
    prepared_sql = generator.generate_code(prepared_prompt)
    if prepared_sql:
        prepared_path = 'generated_code/models/prepared/prepared_customers.sql'
        os.makedirs(os.path.dirname(prepared_path), exist_ok=True)
        with open(prepared_path, 'w') as f:
            f.write(prepared_sql)
        print(f"Generated prepared SQL saved to {prepared_path}")
    else:
        print("Failed to generate prepared SQL.")
