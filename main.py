from src.data_cleaning import clean_data
from src.feature_engineering import feature_engineering
from src.visualization import create_visualizations
from src.preprocessing_pipeline import save_cleaned_dataset


def main():

    filepath = "dataset/titanic.csv"

    # Data Cleaning
    df = clean_data(filepath)

    # Feature Engineering
    df = feature_engineering(df)

    # Visualizations
    create_visualizations(df)

    # Save Cleaned Dataset
    save_cleaned_dataset(df)

    print("\n" + "=" * 50)
    print("Titanic Preprocessing Completed Successfully")
    print("=" * 50)


if __name__ == "__main__":
    main()