def transform_data(data):
    """
    Function to transform the extracted data.
    Perform data cleaning, handle missing values, etc.
    :param data: DataFrame containing the raw data.
    :return: DataFrame containing the cleaned/transformed data.
    """
    # TODO: Implement data cleaning and transformation logic
    try:
        # Example: Handling missing values by filling with the mean
        transformed_data = data.fillna(data.mean())
        return transformed_data
    except Exception as e:
        print(f"Error transforming data: {e}")
        return None
