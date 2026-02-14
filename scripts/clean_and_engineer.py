import pandas as pd
import numpy as np

df = pd.read_csv("../data/synthetic_applications_realistic.csv")

print("Initial shape:", df.shape)


# handling missing values
df["visa_type"].fillna(df["visa_type"].mode()[0], inplace=True)

df["processing_office"].fillna(df["processing_office"].mode()[0], inplace=True)

print("Missing after cleaning:")
print(df.isnull().sum())


# converting dates
df["submission_date"] = pd.to_datetime(df["submission_date"])
df["decision_date"] = pd.to_datetime(df["decision_date"])


# feature engineering
df["submission_month"] = df["submission_date"].dt.month
df["submission_year"] = df["submission_date"].dt.year
df["submission_dayofweek"] = df["submission_date"].dt.dayofweek

# recalculating delay gap 
df["calculated_processing_days"] = (
    df["decision_date"] - df["submission_date"]
).dt.days


# handling outliers
upper_limit = df["processing_days"].quantile(0.99)

df["processing_days"] = np.where(
    df["processing_days"] > upper_limit,
    upper_limit,
    df["processing_days"]
)

print("Outlier cap at:", upper_limit)


# saving cleaned dataset
df.to_csv("../data/clean_applications.csv", index=False)

print("Final cleaned shape:", df.shape)
print(df.head())





