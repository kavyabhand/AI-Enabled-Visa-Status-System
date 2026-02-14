import pandas as pd
import numpy as np

np.random.seed(42)

df = pd.read_csv("../data/synthetic_applications.csv")

# processing office
mask_office = np.random.rand(len(df)) < 0.02
df.loc[mask_office, "processing_office"] = None

# missing visa type
mask_visa = np.random.rand(len(df)) < 0.01
df.loc[mask_visa, "visa_type"] = None

# adding extreme delays (outliers)
mask_outliers = np.random.rand(len(df)) < 0.03
df.loc[mask_outliers, "processing_days"] *= np.random.randint(2, 4)

# adding emergency fast-track cases 
mask_fast = np.random.rand(len(df)) < 0.01
df.loc[mask_fast, "processing_days"] = df.loc[mask_fast, "processing_days"] // 3

# saving updated dataset
df.to_csv("../data/synthetic_applications_realistic.csv", index=False)

print("Realistic dataset created.")
print(df.isnull().sum())
print("Shape:", df.shape)
