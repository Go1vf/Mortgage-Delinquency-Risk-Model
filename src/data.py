import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_and_concat_csv(file_path, column_names, column_classes, chunk_size=100000):
    """
    Loads a pipe-delimited CSV file in chunks and concatenates it into a single DataFrame.

    Parameters:
    - file_path (str): The path to the CSV file.
    - column_names (list): List of column names to assign to the DataFrame.
    - column_classes (dict): Dictionary specifying the data types for each column.
    - chunk_size (int): Number of rows to read at a time. Default is 100,000.

    Returns:
    - pd.DataFrame: Concatenated DataFrame containing all the data.
    """
    result = []

    # Read the CSV file in chunks
    for chunk in pd.read_csv(file_path, sep='|', names=column_names, chunksize=chunk_size, dtype=column_classes):
        result.append(chunk)

    # Concatenate all chunks into a single DataFrame
    final_df = pd.concat(result, ignore_index=True)

    return final_df

def analyze_dataframe(df):
    """
    Analyzes the given DataFrame by printing the distribution of each column
    and calculating the percentage of NA values for each column.

    Parameters:
    df (pd.DataFrame): The DataFrame to analyze.
    """
    # Check if the DataFrame is empty
    if df.empty:
        print("The DataFrame is empty.")
        return

    # Display the distribution of each column
    for column in df.columns:
        print(f"\nDistribution of {column}:")
        
        # Check the dtype of the column
        if pd.api.types.is_numeric_dtype(df[column]):
            print(df[column].describe())  # Statistical summary for numerical columns
        else:
            print(df[column].value_counts())  # Counts of unique values for categorical columns
        
def visualize_NA_percentage(df):
    na_percentage = df.isna().mean() * 100  # Percentage of NA values
    na_percentage = na_percentage.sort_values(ascending=False)
    na_percentage_df = na_percentage.reset_index()
    na_percentage_df.columns = ['Column', 'NA Percentage']
    plt.figure(figsize=(12, 6))
    # Create a bar plot using Seaborn
    sns.barplot(data=na_percentage_df, x='NA Percentage', y='Column', palette='viridis')

    # Adding titles and labels
    plt.title('Percentage of NA Values in Each Column', fontsize=16)
    plt.xlabel('Percentage of NA Values (%)', fontsize=12)
    plt.ylabel('Columns', fontsize=12)

    # Show the plot
    plt.tight_layout()
    plt.show()

def remove_NA_columns(df, threshold_val=0.8):
    # Remove the columns containing more than 80% NA
    threshold = threshold_val * len(df)
    df = df.dropna(axis=1, thresh=threshold)
    return df




