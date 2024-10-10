import pandas as pd

def extract_data(file_path):
    """
    Function to extract data from a CSV file.
    :param file_path: str, path to the CSV file.
    :return: DataFrame containing the extracted data.
    """
    # TODO: Implement code to read the CSV file using pandas
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None
