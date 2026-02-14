import pandas as pd

# master destinations data
data = [
    # USA
    ["USA", "Tourist", 30, 90, 1.4],
    ["USA", "Student", 45, 120, 1.6],
    ["USA", "Work", 60, 180, 1.8],
    ["USA", "Business", 20, 60, 1.3],

    # UK
    ["UK", "Tourist", 15, 40, 1.2],
    ["UK", "Student", 30, 60, 1.3],
    ["UK", "Work", 45, 90, 1.5],
    ["UK", "Business", 20, 45, 1.2],

    # Japan
    ["Japan", "Tourist", 5, 15, 0.9],
    ["Japan", "Student", 20, 45, 1.1],
    ["Japan", "Work", 30, 60, 1.2],
    ["Japan", "Business", 15, 35, 1.0],

    # Canada
    ["Canada", "Tourist", 20, 60, 1.3],
    ["Canada", "Student", 40, 100, 1.5],
    ["Canada", "Work", 50, 150, 1.6],
    ["Canada", "Business", 25, 55, 1.2],
]

df = pd.DataFrame(data, columns=[
    "destination_country",
    "visa_type",
    "base_min_days",
    "base_max_days",
    "complexity_index"
])

df.to_csv("../data/master_destinations.csv", index=False)
print("master_destinations.csv created")


# master offices data
office_data = [
    ["Mumbai", 1.3, 500],
    ["New Delhi", 1.4, 600],
    ["Chennai", 1.1, 400],
    ["Hyderabad", 1.0, 350],
    ["Kolkata", 0.9, 300]
]

df_offices = pd.DataFrame(office_data, columns=[
    "office_name",
    "workload_multiplier",
    "avg_daily_capacity"
])

df_offices.to_csv("../data/master_offices.csv", index=False)
print("master_offices.csv created")


# seasonal index data
season_data = []

for month in range(1, 13):
    for visa in ["Tourist", "Student", "Work", "Business"]:
        multiplier = 1.0
        
        # Student peak season
        if visa == "Student" and month in [5,6,7]:
            multiplier = 1.3
        
        # Tourist peak season
        if visa == "Tourist" and month in [11,12]:
            multiplier = 1.2
        
        season_data.append([month, visa, multiplier])

df_season = pd.DataFrame(season_data, columns=[
    "month",
    "visa_type",
    "seasonal_multiplier"
])

df_season.to_csv("../data/seasonal_index.csv", index=False)
print("seasonal_index.csv created")


