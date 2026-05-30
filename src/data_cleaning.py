import pandas as pd


def clean_data(filepath):

    df = pd.read_csv(filepath)

    print("\nDataset Shape Before Cleaning:")
    print(df.shape)

    print("\nMissing Values Before Cleaning:")
    print(df.isnull().sum())

    # Handle missing Age values
    df["Age"] = df["Age"].fillna(
        df["Age"].median()
    )

    # Handle missing Embarked values
    df["Embarked"] = df["Embarked"].fillna(
        df["Embarked"].mode()[0]
    )

    # Handle missing Cabin values
    df["Cabin"] = df["Cabin"].fillna(
        "Unknown"
    )

    # Remove duplicates
    duplicates = df.duplicated().sum()

    df = df.drop_duplicates()

    print("\nDuplicates Removed:")
    print(duplicates)

    print("\nMissing Values After Cleaning:")
    print(df.isnull().sum())

    print("\nDataset Shape After Cleaning:")
    print(df.shape)

    return df