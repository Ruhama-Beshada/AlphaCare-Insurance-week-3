import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def load_data(path):
    return pd.read_csv(path)

def plot_histogram(df, column, bins=50):
    sns.histplot(df[column], bins=bins)
    plt.show()

def plot_boxplot(df, x_col, y_col):
    sns.boxplot(x=x_col, y=y_col, data=df)
    plt.show()
