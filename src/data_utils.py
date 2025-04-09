# Import necessary libraries
import pandas as pd
import os


def load_data():
    """
    Load the churn_data_cleaned.csv file into a pandas DataFrame.
    Returns:
        pd.DataFrame: DataFrame containing the cleaned churn data.
    """
    # Define the file path for the CSV file
    file_path = r'../../Telecom Customer Churn/data/processed/churn_data_cleaned.csv'

    # Read the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    df.reset_index(drop=True)

    # Return the DataFrame
    return df


"""
This is a one-time operation to convert the Excel file to CSV.
The script reads the Excel file 'Telco_customer_churn.xlsx' from the specified path and saves it as a CSV file.
This is useful for initial data preparation and should not be run every time the script is executed.
"""
if __name__ == "__main__":
    try:
    # Define the file path for the Excel file
        file_path = r'../Telecom Customer Churn/data/raw/Telco_customer_churn.xlsx'

        # Read the Excel file into a DataFrame
        df = pd.read_excel(file_path, sheet_name='Telco_Churn')

        # Create an absolute path for the CSV file
        csv_file_path = os.path.abspath(r'../Telecom Customer Churn/data/processed/churn_data_cleaned.csv')

        # Save the DataFrame to the CSV file
        df.to_csv(csv_file_path, index=False)
    
    except Exception as e:
        print(f"An error occurred: {e}")    