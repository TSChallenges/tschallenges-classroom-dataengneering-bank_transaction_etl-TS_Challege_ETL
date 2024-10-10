from data_engineering.extract import extract_data
from data_engineering.transform import transform_data
from data_engineering.load import load_data

def main():
    # File paths
    csv_file = 'data/raw_data.csv'
    db_name = 'etl_database.db'
    table_name = 'cleaned_data'
    
    # Step 1: Extract data
    data = extract_data(csv_file)
    
    if data is not None:
        # Step 2: Transform data
        cleaned_data = transform_data(data)
        
        if cleaned_data is not None:
            # Step 3: Load data into the database
            load_data(cleaned_data, db_name, table_name)
            print("ETL process completed successfully!")
        else:
            print("Data transformation failed.")
    else:
        print("Data extraction failed.")

if __name__ == "__main__":
    main()
