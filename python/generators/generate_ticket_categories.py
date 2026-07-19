# ============================================================
# Project : Customer Success Intelligence Platform
# File    : generate_ticket_categories.py
# Purpose : Generate Ticket Category Master Data
#
# Author  : Prayank Gupta
#
# Description:
# Generates raw ticket category master data.
#
# Output:
# data/raw/dim_ticket_category.csv
# ============================================================


# ============================================================
# Import Libraries
# ============================================================

import random

import pandas as pd


# ============================================================
# Configuration
# ============================================================

OUTPUT_FILE = "C:/AnalyticsProjects/customer-success-intelligence-platform/data/raw/dim_ticket_category.csv"


# ============================================================
# Reference Data
# ============================================================

CATEGORY_DATA = [

    ("Maintenance Payment", "Medium", 24),

    ("Visitor Management", "Low", 48),

    ("Parking", "Medium", 48),

    ("Amenities", "Low", 72),

    ("Complaint", "High", 12),

    ("Account", "Medium", 24),

    ("Security", "High", 4),

    ("Other", "Low", 72)

]


STATUS_LIST = [

    "Active",

    "Inactive"

]


# ============================================================
# Empty List
# ============================================================

categories = []


# ============================================================
# Generate Category Records
# ============================================================

for i, category in enumerate(CATEGORY_DATA, start=1):

    category_id = f"CAT{i:03d}"

    category_name = category[0]

    priority = category[1]

    expected_sla_hours = category[2]

    category_status = random.choice(STATUS_LIST)


    # ========================================================
    # Dirty Data Injection
    # ========================================================

    if random.random() < 0.10:

        category_name = category_name.upper()

    if random.random() < 0.10:

        category_name = category_name.lower()

    if random.random() < 0.05:

        category_name = " " + category_name

    if random.random() < 0.05:

        category_name = category_name + " "

    if random.random() < 0.05:

        priority = priority.lower()

    if random.random() < 0.05:

        priority = priority.upper()

    if random.random() < 0.03:

        priority = None

    if random.random() < 0.03:

        expected_sla_hours = None

# ============================================================
# Store Record
# ============================================================

    category_record = {

        "category_id": category_id,

        "category_name": category_name,

        "priority": priority,

        "expected_sla_hours": expected_sla_hours,

        "category_status": category_status

    }

    categories.append(category_record)


# ============================================================
# Create DataFrame
# ============================================================

category_df = pd.DataFrame(categories)


# ============================================================
# Introduce Duplicate Records
# ============================================================

duplicate_rows = category_df.sample(

    frac=0.25,

    random_state=42

)

category_df = pd.concat(

    [

        category_df,

        duplicate_rows

    ],

    ignore_index=True

)


# ============================================================
# Shuffle Dataset
# ============================================================

category_df = category_df.sample(

    frac=1,

    random_state=42

).reset_index(drop=True)


# ============================================================
# Export CSV
# ============================================================

category_df.to_csv(

    OUTPUT_FILE,

    index=False

)


# ============================================================
# Summary
# ============================================================

print()

print("===============================================")
print(" Ticket Category Master Generated Successfully")
print("===============================================")

print()

print(f"Total Categories : {len(categories)}")

print(f"CSV Records      : {len(category_df)}")

print()

print(category_df)

print()

print("===============================================")