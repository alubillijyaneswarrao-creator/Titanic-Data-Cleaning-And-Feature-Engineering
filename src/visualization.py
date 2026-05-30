import matplotlib.pyplot as plt
import seaborn as sns
import os


def create_visualizations(df):

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    

    plt.figure(figsize=(10, 5))

    df.isnull().sum().plot(
        kind="bar"
    )

    plt.title(
        "Missing Values After Cleaning"
    )

    plt.savefig(
        "outputs/missing_values_before.png"
    )

    plt.close()

   

    plt.figure(figsize=(8, 5))

    sns.histplot(
        df["Age"],
        kde=True
    )

    plt.title(
        "Age Distribution"
    )

    plt.savefig(
        "outputs/age_distribution.png"
    )

    plt.close()


    plt.figure(figsize=(12, 8))

    sns.heatmap(
        df.select_dtypes(
            include="number"
        ).corr(),
        cmap="coolwarm"
    )

    plt.title(
        "Correlation Heatmap"
    )

    plt.savefig(
        "outputs/correlation_heatmap.png"
    )

    plt.close()

    print("\nGraphs Generated Successfully")