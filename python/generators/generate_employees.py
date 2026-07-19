# ============================================================
# Project : Customer Success Intelligence Platform
# File    : generate_employees.py
# Purpose : Generate Raw Employee Master Data
#
# Author  : Prayank Gupta
#
# Description:
# This script generates dirty employee master data which will
# later be cleaned using SQL scripts as part of the ETL process.
#
# Output:
# data/raw/dim_employee.csv
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

TOTAL_EMPLOYEES = 50

OUTPUT_FILE = "C:/AnalyticsProjects/customer-success-intelligence-platform/data/raw/dim_employee.csv"


# ============================================================
# Reference Data
# ============================================================

FIRST_NAMES = [

    "Rahul",
    "Amit",
    "Neha",
    "Priya",
    "Rohit",
    "Anjali",
    "Akash",
    "Sneha",
    "Vikas",
    "Megha",
    "Arjun",
    "Divya"

]


LAST_NAMES = [

    "Sharma",
    "Gupta",
    "Patel",
    "Verma",
    "Singh",
    "Reddy",
    "Kapoor",
    "Joshi",
    "Nair",
    "Jain"

]


DEPARTMENTS = [

    "Customer Support",
    "Customer Success",
    "Operations",
    "Sales",
    "Finance",
    "Technology"

]


DESIGNATIONS = [

    "Executive",
    "Senior Executive",
    "Associate",
    "Team Lead",
    "Assistant Manager",
    "Manager"

]


STATUS_LIST = [

    "Active",
    "Inactive"

]


# ============================================================
# Helper Function
# Generate Joining Date
# ============================================================

def generate_joining_date():

    start_date = datetime(2019, 1, 1)

    end_date = datetime(2026, 6, 30)

    random_days = random.randint(

        0,

        (end_date - start_date).days

    )

    return start_date + timedelta(days=random_days)


# ============================================================
# Empty List
# ============================================================

employees = []


# ============================================================
# Generate Employee Records
# ============================================================

for i in range(1, TOTAL_EMPLOYEES + 1):

    employee_id = f"EMP{i:03d}"

    first_name = random.choice(FIRST_NAMES)

    last_name = random.choice(LAST_NAMES)

    employee_name = first_name + " " + last_name

    employee_email = (

        first_name.lower()

        + "."

        + last_name.lower()

        + "@company.com"

    )

    department = random.choice(DEPARTMENTS)

    designation = random.choice(DESIGNATIONS)

    employee_status = random.choice(STATUS_LIST)

    joining_date = generate_joining_date()


    # ========================================================
    # Dirty Data Injection
    # ========================================================

    if random.random() < 0.05:

        employee_name = employee_name.upper()

    if random.random() < 0.05:

        employee_name = employee_name.lower()

    if random.random() < 0.04:

        employee_name = " " + employee_name

    if random.random() < 0.04:

        employee_name = employee_name + " "

    if random.random() < 0.05:

        employee_email = employee_email.replace("@", "")

    if random.random() < 0.03:

        employee_email = None

    if random.random() < 0.04:

        department = department.lower()

    if random.random() < 0.03:

        designation = designation.upper()

    if random.random() < 0.03:

        employee_status = None

# ============================================================
# Store Record
# ============================================================

    employee = {

        "employee_id": employee_id,

        "employee_name": employee_name,

        "employee_email": employee_email,

        "department": department,

        "designation": designation,

        "joining_date": joining_date,

        "employee_status": employee_status

    }

    employees.append(employee)


# ============================================================
# Create DataFrame
# ============================================================

employee_df = pd.DataFrame(employees)


# ============================================================
# Introduce Duplicate Records
#
# Purpose:
# Duplicate employee records are intentionally created
# to demonstrate SQL data cleaning techniques.
# ============================================================

duplicate_rows = employee_df.sample(

    frac=0.04,

    random_state=42

)

employee_df = pd.concat(

    [

        employee_df,

        duplicate_rows

    ],

    ignore_index=True

)


# ============================================================
# Shuffle Dataset
#
# Prevent duplicate records from appearing together.
# ============================================================

employee_df = employee_df.sample(

    frac=1,

    random_state=42

).reset_index(drop=True)


# ============================================================
# Export CSV
# ============================================================

employee_df.to_csv(

    OUTPUT_FILE,

    index=False

)


# ============================================================
# Summary Statistics
# ============================================================

print()

print("===============================================")
print(" Employee Master Data Generated Successfully")
print("===============================================")

print()

print(f"Total Records Generated : {len(employees)}")

print(f"Final Records in CSV    : {len(employee_df)}")

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

print(employee_df.isnull().sum())

print()

print("Duplicate Rows")

print()

print(

    employee_df.duplicated().sum()

)

print()

print("Department Distribution")

print()

print(

    employee_df["department"]

    .value_counts(

        dropna=False

    )

)

print()

print("Designation Distribution")

print()

print(

    employee_df["designation"]

    .value_counts(

        dropna=False

    )

)

print()

print("Employee Status Distribution")

print()

print(

    employee_df["employee_status"]

    .value_counts(

        dropna=False

    )

)

print()

print("===============================================")