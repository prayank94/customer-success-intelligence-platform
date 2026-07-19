# ============================================================
# Project : Customer Success Intelligence Platform
# File    : generate_societies.py
# Purpose : Generate Raw Society Master Data
#
# Author  : Prayank Gupta
#
# Description:
# This script generates dirty society master data which will
# later be cleaned using SQL scripts as part of the ETL process.
#
# Output:
# data/raw/dim_society.csv
#
# ============================================================


# ============================================================
# Import Libraries
# ============================================================

import random
import pandas as pd

from datetime import datetime
from datetime import timedelta


# ============================================================
# Configuration
# ============================================================

TOTAL_SOCIETIES = 1000

OUTPUT_FILE =  "C:/AnalyticsProjects/customer-success-intelligence-platform/data/raw/dim_society.csv"


# ============================================================
# Reference Data
# ============================================================

CITY_LIST = [

    "Bangalore",
    "Mumbai",
    "Delhi",
    "Hyderabad",
    "Pune",
    "Chennai",
    "Ahmedabad",
    "Kolkata"

]


STATUS_LIST = [

    "Active",
    "Phase 1 Churn",
    "Phase 2 Churn",
    "YTB"

]


prefixes = [

    "Green",
    "Royal",
    "Crystal",
    "Palm",
    "Elite",
    "Lake",
    "Sky",
    "Silver",
    "Golden",
    "Sunrise",
    "Hill",
    "River"

]


suffixes = [

    "Heights",
    "Residency",
    "Apartments",
    "Enclave",
    "Homes",
    "Gardens",
    "Tower",
    "Park",
    "County",
    "Plaza"

]


FLAT_COUNT = [

    20,
    30,
    40,
    60,
    80,
    120,
    180,
    240,
    320,
    450

]


MAINTENANCE_CHARGE = [

    1800,
    2200,
    2500,
    3000,
    3500

]


# ============================================================
# Helper Function
# Generate Random Onboarding Date
# ============================================================

def generate_onboarding_date():

    start_date = datetime(2018, 1, 1)

    end_date = datetime(2025, 12, 31)

    random_days = random.randint(
        0,
        (end_date - start_date).days
    )

    return start_date + timedelta(days=random_days)


# ============================================================
# Empty List
# ============================================================

societies = []


# ============================================================
# Generate Society Records
# ============================================================

for i in range(1, TOTAL_SOCIETIES + 1):

    society_id = f"SOC{i:04d}"

    society_name = (

        random.choice(prefixes)

        + " "

        + random.choice(suffixes)

    )

    city = random.choice(CITY_LIST)

    status = random.choice(STATUS_LIST)

    flat_count = random.choice(FLAT_COUNT)

    maintenance = random.choice(MAINTENANCE_CHARGE)

    monthly_revenue = flat_count * maintenance

    onboarding_date = generate_onboarding_date()


    # ========================================================
    # Dirty Data Injection
    # ========================================================

    if random.random() < 0.08:

        city = city.lower()

    if random.random() < 0.05:

        city = city.upper()

    if random.random() < 0.05:

        city = city.replace("a", "")

    if random.random() < 0.05:

        city = " " + city

    if random.random() < 0.05:

        city = city + " "

    if random.random() < 0.04:

        status = status.lower()

    if random.random() < 0.03:

        status = status.upper()

    if random.random() < 0.03:

        status = None

    if random.random() < 0.05:

        society_name = society_name.upper()

    if random.random() < 0.05:

        society_name = society_name.lower()

    if random.random() < 0.05:

        society_name = " " + society_name

    if random.random() < 0.05:

        society_name = society_name + " "

    if random.random() < 0.03:

        monthly_revenue = None

    if random.random() < 0.03:

        flat_count = None

# ============================================================
# Store Record
# ============================================================

    society = {

        "society_id": society_id,

        "society_name": society_name,

        "city": city,

        "status": status,

        "flat_count": flat_count,

        "maintenance_charge": maintenance,

        "monthly_revenue": monthly_revenue,

        "onboarding_date": onboarding_date

    }

    societies.append(society)


# ============================================================
# Create DataFrame
# ============================================================

society_df = pd.DataFrame(societies)


# ============================================================
# Introduce Duplicate Records
#
# Purpose:
# Duplicate records are intentionally created so they can be
# identified and removed later using SQL data cleaning scripts.
# ============================================================

duplicate_rows = society_df.sample(

    frac=0.03,

    random_state=42

)

society_df = pd.concat(

    [

        society_df,

        duplicate_rows

    ],

    ignore_index=True

)


# ============================================================
# Shuffle Dataset
#
# This prevents duplicate records from appearing together.
# ============================================================

society_df = society_df.sample(

    frac=1,

    random_state=42

).reset_index(drop=True)


# ============================================================
# Export CSV
# ============================================================

society_df.to_csv(

    OUTPUT_FILE,

    index=False

)


# ============================================================
# Summary Statistics
# ============================================================

print()

print("===============================================")
print(" Society Master Data Generated Successfully")
print("===============================================")

print()

print(f"Total Records Generated : {len(societies)}")

print(f"Final Records in CSV    : {len(society_df)}")

print(f"Duplicate Records Added : {len(duplicate_rows)}")

print()

print("Output File")

print(OUTPUT_FILE)

print()

print("===============================================")


# ============================================================
# Data Quality Summary
# ============================================================

print()

print("Missing Values")

print()

print(society_df.isnull().sum())

print()

print("Duplicate Rows")

print()

print(

    society_df.duplicated().sum()

)

print()

print("Unique Cities")

print()

print(

    society_df["city"]

    .value_counts()

)

print()

print("Status Distribution")

print()

print(

    society_df["status"]

    .value_counts(

        dropna=False

    )

)

print()

print("===============================================")