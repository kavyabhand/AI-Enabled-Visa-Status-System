# AI-Enabled Visa Status System

This project simulates and analyzes visa application processing using synthetic and real-world-inspired datasets. The workflow includes data generation, introducing realistic data issues, cleaning, and feature engineering for further analysis or modeling.

## Project Structure

- **data/**: Contains all datasets (raw, synthetic, cleaned, and master data)
- **scripts/**: Python scripts for data generation, cleaning, and feature engineering
- **LICENSE**: Project license

## Datasets

- `master_destinations.csv`: Master data for destination countries, visa types, base processing days, and complexity index
- `master_offices.csv`: Master data for processing offices, workload multipliers, and capacities
- `seasonal_index.csv`: Seasonal multipliers for visa types by month
- `synthetic_applications.csv`: 100,000 synthetic visa application records
- `synthetic_applications_realistic.csv`: Synthetic data with missing values and outliers for realism
- `clean_applications.csv`: Cleaned and feature-engineered dataset ready for analysis

## Scripts and Workflow

### 1. `generate_master_data.py`
- Generates master datasets: destinations, offices, and seasonal index
- Outputs: `master_destinations.csv`, `master_offices.csv`, `seasonal_index.csv`

### 2. `generate_applications.py`
- Uses master datasets to generate 100,000 synthetic visa application records
- Simulates realistic processing times using base days, complexity, workload, and seasonality
- Outputs: `synthetic_applications.csv`

### 3. `introduce_realism.py`
- Adds missing values (e.g., visa type, processing office)
- Introduces outliers (extreme delays, fast-track cases)
- Outputs: `synthetic_applications_realistic.csv`

### 4. `clean_and_engineer.py`
- Cleans missing values using mode imputation
- Converts date columns to datetime
- Engineers new features: submission month, year, day of week, recalculated processing days
- Handles outliers by capping extreme processing days
- Outputs: `clean_applications.csv`

## How to Reproduce

1. Run `generate_master_data.py` to create master data
2. Run `generate_applications.py` to generate synthetic applications
3. Run `introduce_realism.py` to add realism to the data
4. Run `clean_and_engineer.py` to clean and engineer features

## Notes
- All scripts are located in the `scripts/` directory
- Data files are saved in the `data/` directory
- The project is modular and can be extended for further analysis or modeling

---

