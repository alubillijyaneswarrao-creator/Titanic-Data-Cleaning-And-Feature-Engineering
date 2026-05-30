import os


def save_cleaned_dataset(df):

    os.makedirs(
        "outputs",
        exist_ok=True
    )

    output_file = (
        "outputs/cleaned_titanic.csv"
    )

    df.to_csv(
        output_file,
        index=False
    )

    print(
        "\nCleaned Dataset Saved:"
    )

    print(output_file)