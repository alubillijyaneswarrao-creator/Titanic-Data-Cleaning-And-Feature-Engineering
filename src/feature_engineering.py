import pandas as pd
from sklearn.preprocessing import (
    LabelEncoder,
    StandardScaler
)


def feature_engineering(df):


    df["Title"] = df["Name"].str.extract(
        " ([A-Za-z]+)\.",
        expand=False
    )

    # Family Size

    df["FamilySize"] = (
        df["SibSp"]
        + df["Parch"]
        + 1
    )


    def age_group(age):

        if age < 13:
            return "Child"

        elif age < 20:
            return "Teen"

        elif age < 60:
            return "Adult"

        return "Senior"

    df["AgeGroup"] = (
        df["Age"]
        .apply(age_group)
    )


    encoder = LabelEncoder()

    df["Sex"] = encoder.fit_transform(
        df["Sex"]
    )


    df = pd.get_dummies(
        df,
        columns=[
            "Embarked",
            "Title",
            "AgeGroup"
        ]
    )

    scaler = StandardScaler()

    numerical_cols = [
        "Age",
        "Fare",
        "FamilySize"
    ]

    df[numerical_cols] = (
        scaler.fit_transform(
            df[numerical_cols]
        )
    )

    print("\nNew Features Created:")
    print(
        "Title, FamilySize, AgeGroup"
    )

    return df