import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter

# Load the dataset
file = 'D:/Python Projects/Data_Analytics_Project/retraction_watch.csv'
df = pd.read_csv(file)

def bar_plots(cndn, cmn_df):
    """Plots a bar chart for categorical data using Seaborn."""
    plt.figure(figsize=(12,6))
    sns.barplot(data=cmn_df.head(10), x='Common', y='Count', palette='coolwarm')

    for i, value in enumerate(cmn_df.head(10)['Count']):
        plt.text(i, value + 5, f'{value:,}', fontsize=10, fontweight='bold', color='black')
    
    plt.xlabel(f'{cndn}')
    plt.xticks(rotation=45, ha='right', fontsize=10)
    plt.ylabel('Number of times they appear')
    plt.title(f'Occurrences of {cndn} - Bar Chart')
    plt.grid(axis='y', linestyle='--', alpha=0.7)

    # Show plot
    plt.show()

def pie_plot(cndn, cmn_df):
    """Plots a pie chart for categorical data."""
    perc = (cmn_df.head(10)['Count'] / cmn_df['Count'].sum()) * 100
    labels = cmn_df.head(10)['Common']

    plt.figure(figsize=(8, 8))
    plt.pie(perc, labels=labels, autopct='%1.1f%%', shadow=True, startangle=140)
    plt.title(f'Occurrences of {cndn} - Pie Chart', fontsize=14)

    plt.show()

def plot_common_entries(cndn):
    """Plots the most common occurrences of a given categorical column."""
    if cndn not in df.columns:
        print(f"Column '{cndn}' not found in DataFrame.")
        return None

    # Flattening the list
    all_cmn = df[cndn].dropna().str.split(';').explode()

    # Removing unwanted values
    invalid_entries = {'Unknown', 'unavailable', 'Unavailable', 'unknown', 'N/A', 'Not Available', ''}
    all_cmn = all_cmn[~all_cmn.isin(invalid_entries)].str.strip()
    all_cmn = all_cmn[all_cmn != '']

    # Count Occurrences
    counts = Counter(all_cmn)

    # Convert to DataFrame
    cmn_df = pd.DataFrame(counts.items(), columns=['Common', 'Count'])
    cmn_df = cmn_df.sort_values(by='Count', ascending=False)

    # Define which categories should have a bar chart
    bar_categories = {'Subject', 'Institution', 'Country', 'Author', 'ArticleType'}
    pie_categories = {'Journal', 'RetractionNature'}

    # Call plots function if applicable
    if cndn in bar_categories:
        bar_plots(cndn, cmn_df)
    elif cndn in pie_categories:
        pie_plot(cndn, cmn_df)

    return cmn_df  # Returning DataFrame for further analysis if needed


# Example Usage:
# plot_common_entries('Subject')  
# plot_common_entries('Institution')  
plot_common_entries('Journal')  
# plot_common_entries('ArticleType')