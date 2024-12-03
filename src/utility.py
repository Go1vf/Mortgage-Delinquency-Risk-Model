import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

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




