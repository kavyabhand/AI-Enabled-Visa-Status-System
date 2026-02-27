import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

sns.set_style("whitegrid")

BASE_DIR = Path(__file__).resolve().parent.parent
data_path = BASE_DIR / "data" / "clean_applications.csv"
output_path = BASE_DIR / "reports" / "figures"

df = pd.read_csv(data_path)

print("Dataset Shape:", df.shape)
print(df.describe())

# 1. Processing Time Distribution
plt.figure(figsize=(8,5))
sns.histplot(df["processing_days"], bins=50, kde=True)
plt.title("Distribution of Visa Processing Days")
plt.xlabel("Processing Days")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig(output_path / "processing_distribution.png")
plt.close()

# 2. Processing by Visa Type
plt.figure(figsize=(8,5))
sns.boxplot(x="visa_type", y="processing_days", data=df)
plt.title("Processing Time by Visa Type")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_path / "visa_type_processing.png")
plt.close()

# 3. Processing by Destination Country
plt.figure(figsize=(8,5))
sns.boxplot(x="destination_country", y="processing_days", data=df)
plt.title("Processing Time by Destination Country")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_path / "country_processing.png")
plt.close()

# 4. Monthly Trend
monthly_avg = df.groupby("submission_month")["processing_days"].mean()

plt.figure(figsize=(8,5))
monthly_avg.plot(marker="o")
plt.title("Average Processing Time by Month")
plt.xlabel("Month")
plt.ylabel("Average Days")
plt.tight_layout()
plt.savefig(output_path / "monthly_trend.png")
plt.close()

# 5. Office Impact
office_avg = df.groupby("processing_office")["processing_days"].mean()

plt.figure(figsize=(8,5))
office_avg.plot(kind="bar")
plt.title("Average Processing Time by Office")
plt.ylabel("Average Days")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig(output_path / "office_processing.png")
plt.close()

# 6. Correlation Matrix
encoded_df = df.copy()

from sklearn.preprocessing import LabelEncoder

for col in ["destination_country", "visa_type", "processing_office", "applicant_country"]:
    encoded_df[col] = LabelEncoder().fit_transform(encoded_df[col])

numeric_df = encoded_df.select_dtypes(include=[np.number])

plt.figure(figsize=(8,6))
sns.heatmap(numeric_df.corr(), annot=False, cmap="coolwarm")
plt.title("Correlation Matrix")
plt.tight_layout()
plt.savefig(output_path / "correlation_matrix.png")
plt.close()