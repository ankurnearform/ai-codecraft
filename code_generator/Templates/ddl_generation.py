import os

def generate_ddl(generator,prompt,table_name):
    print(f"Generated DDL prompt: {prompt}")
    ddl_script = generator.generate_code(prompt)
    if ddl_script:
        ddl_path = f'generated_code/ddl/{table_name}.sql'
        os.makedirs(os.path.dirname(ddl_path), exist_ok=True)
        with open(ddl_path, 'w') as f:
            f.write(ddl_script)
        print(f"Generated DDL script saved to {ddl_path}")
    else:
        print("Failed to generate DDL script.")
