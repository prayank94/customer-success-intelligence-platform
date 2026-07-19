# ============================================================
# Project : Customer Success Intelligence Platform
# File    : generate_customers.py
# Purpose : Generate Raw Customer Master Data
#
# Author  : Prayank Gupta
#
# Description:
# This script generates dirty customer master data which will
# later be cleaned using SQL scripts as part of the ETL process.
#
# Output:
# data/raw/dim_customer.csv
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

TOTAL_CUSTOMERS = 8000

TOTAL_SOCIETIES = 1000

OUTPUT_FILE = "C:/AnalyticsProjects/customer-success-intelligence-platform/data/raw/dim_customer.csv"


# ============================================================
# Reference Data
# ============================================================

CUSTOMER_TYPES = [

    "Owner",
    "Tenant",
    "Buyer",
    "Seller",
    "MC Member"

]


FIRST_NAMES = [

    "Rahul",
    "Amit",
    "Neha",
    "Priya",
    "Rohit",
    "Anjali",
    "Vikas",
    "Sneha",
    "Akash",
    "Pooja",
    "Karan",
    "Riya",
    "Arjun",
    "Megha",
    "Nikhil",
    "Divya"

]


LAST_NAMES = [

    "Sharma",
    "Gupta",
    "Patel",
    "Verma",
    "Singh",
    "Joshi",
    "Reddy",
    "Iyer",
    "Kapoor",
    "Nair",
    "Jain",
    "Malhotra"

]


EMAIL_DOMAINS = [

    "gmail.com",
    "yahoo.com",
    "outlook.com",
    "hotmail.com",
    "nobroker.in"

]


# ============================================================
# Helper Function
# Generate Random Registration Date
# ============================================================

def generate_registration_date():

    start_date = datetime(2018, 1, 1)

    end_date = datetime(2026, 6, 30)

    random_days = random.randint(

        0,

        (end_date - start_date).days

    )

    return start_date + timedelta(days=random_days)


# ============================================================
# Empty List
# ============================================================

customers = []


# ============================================================
# Generate Customer Records
# ============================================================

for i in range(1, TOTAL_CUSTOMERS + 1):

    customer_id = f"CUST{i:05d}"

    first_name = random.choice(FIRST_NAMES)

    last_name = random.choice(LAST_NAMES)

    customer_name = first_name + " " + last_name

    customer_type = random.choice(CUSTOMER_TYPES)

    email = (

        first_name.lower()

        + "."

        + last_name.lower()

        + str(random.randint(1,999))

        + "@"

        + random.choice(EMAIL_DOMAINS)

    )

    phone_number = str(

        random.randint(

            9000000000,

            9999999999

        )

    )

    society_id = f"SOC{random.randint(1,TOTAL_SOCIETIES):04d}"

    registration_date = generate_registration_date()


    # ========================================================
    # Dirty Data Injection
    # ========================================================

    if random.random() < 0.05:

        customer_name = customer_name.upper()

    if random.random() < 0.05:

        customer_name = customer_name.lower()

    if random.random() < 0.04:

        customer_name = " " + customer_name

    if random.random() < 0.04:

        customer_name = customer_name + " "

    if random.random() < 0.05:

        customer_type = customer_type.lower()

    if random.random() < 0.03:

        customer_type = customer_type.upper()

    if random.random() < 0.03:

        customer_type = None

    if random.random() < 0.04:

        email = email.replace("@","")

    if random.random() < 0.03:

        email = email.replace(".com",".co")

    if random.random() < 0.03:

        email = None

    if random.random() < 0.04:

        phone_number = phone_number[:-1]

    if random.random() < 0.03:

        phone_number = "0" + phone_number

    if random.random() < 0.03:

        phone_number = None

    if random.random() < 0.03:

        society_id = society_id.lower()

    if random.random() < 0.02:

        society_id = "SOC1001"

    if random.random() < 0.02:

        society_id = None

# ============================================================
# Store Record
# ============================================================

    customer = {

        "customer_id": customer_id,

        "customer_name": customer_name,

        "customer_type": customer_type,

        "email": email,

        "phone_number": phone_number,

        "society_id": society_id,

        "registration_date": registration_date

    }

    customers.append(customer)


# ============================================================
# Create DataFrame
# ============================================================

customer_df = pd.DataFrame(customers)


# ============================================================
# Introduce Duplicate Records
#
# Purpose:
# Duplicate records are intentionally created so they can
# later be identified and removed using SQL.
# ============================================================

duplicate_rows = customer_df.sample(

    frac=0.03,

    random_state=42

)

customer_df = pd.concat(

    [

        customer_df,

        duplicate_rows

    ],

    ignore_index=True

)


# ============================================================
# Shuffle Dataset
#
# This prevents duplicate rows from appearing together.
# ============================================================

customer_df = customer_df.sample(

    frac=1,

    random_state=42

).reset_index(drop=True)


# ============================================================
# Export CSV
# ============================================================

customer_df.to_csv(

    OUTPUT_FILE,

    index=False

)


# ============================================================
# Summary Statistics
# ============================================================

print()

print("===============================================")
print(" Customer Master Data Generated Successfully")
print("===============================================")

print()

print(f"Total Records Generated : {len(customers)}")

print(f"Final Records in CSV    : {len(customer_df)}")

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

print(customer_df.isnull().sum())

print()

print("Duplicate Rows")

print()

print(

    customer_df.duplicated().sum()

)

print()

print("Customer Type Distribution")

print()

print(

    customer_df["customer_type"]

    .value_counts(

        dropna=False

    )

)

print()

print("Society Distribution (Top 10)")

print()

print(

    customer_df["society_id"]

    .value_counts(

        dropna=False

    )

    .head(10)

)

print()

print("===============================================")