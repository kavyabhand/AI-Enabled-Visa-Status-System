import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

np.random.seed(42)
random.seed(42)

# loading master datasets
destinations_df = pd.read_csv("../data/master_destinations.csv")
offices_df = pd.read_csv("../data/master_offices.csv")
season_df = pd.read_csv("../data/seasonal_index.csv")

n_records = 100000

applications = []

for app_id in range(n_records):

    # randomly selecting destination and visa type
    row = destinations_df.sample(1).iloc[0]
    destination = row["destination_country"]
    visa_type = row["visa_type"]
    base_min = row["base_min_days"]
    base_max = row["base_max_days"]
    complexity_index = row["complexity_index"]

    # random office
    office_row = offices_df.sample(1).iloc[0]
    office = office_row["office_name"]
    workload_multiplier = office_row["workload_multiplier"]

    # random submission date (2022-2024)
    submission_date = datetime(2022, 1, 1) + timedelta(days=random.randint(0, 900))
    submission_month = submission_date.month

    # base processing time
    base_time = np.random.randint(base_min, base_max)

    # seasonal multiplier
    seasonal_row = season_df[
        (season_df["month"] == submission_month) &
        (season_df["visa_type"] == visa_type)
    ].iloc[0]

    seasonal_multiplier = seasonal_row["seasonal_multiplier"]

    # calculating the final processing time
    processing_time = (
        base_time
        * seasonal_multiplier
        * workload_multiplier
        * complexity_index
    )

    # adding noise
    noise = np.random.normal(0, 5)
    processing_days = int(processing_time + noise)

    if processing_days < 1:
        processing_days = base_time

    decision_date = submission_date + timedelta(days=processing_days)

    applications.append([
        app_id,
        "India",
        destination,
        visa_type,
        office,
        submission_date,
        decision_date,
        processing_days
    ])

applications_df = pd.DataFrame(applications, columns=[
    "application_id",
    "applicant_country",
    "destination_country",
    "visa_type",
    "processing_office",
    "submission_date",
    "decision_date",
    "processing_days"
])

applications_df.to_csv("../data/synthetic_applications.csv", index=False)

print("100,000 application records generated successfully!")
print(applications_df.head())
print("Shape:", applications_df.shape)

