# ============================================================
# Project : Customer Success Intelligence Platform
# File    : generate_tickets.py
# Purpose : Generate Raw Customer Ticket Data
#
# Author  : Prayank Gupta
#
# Description:
# This script generates raw customer support tickets.
#
# The generated data intentionally contains dirty records,
# duplicate records and inconsistent values so that they
# can later be cleaned using SQL ETL scripts.
#
# Output:
# data/raw/fact_ticket.csv
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

TOTAL_TICKETS = 50000

TOTAL_CUSTOMERS = 8000

TOTAL_EMPLOYEES = 50

TOTAL_CATEGORIES = 8

TOTAL_SOCIETIES = 1000

OUTPUT_FILE = "C:/AnalyticsProjects/customer-success-intelligence-platform/data/raw/fact_customer_tickets.csv"


# ============================================================
# Reference Data
# ============================================================

TICKET_CHANNELS = [

    "Application",

    "Website",

    "WhatsApp",

    "Email",

    "Call",

    "Social Media"

]


CONVERSATIONS = [

    "Maintenance payment failed.",

    "Unable to make maintenance payment.",

    "Payment deducted twice.",

    "Visitor approval is not working.",

    "Unable to add visitor.",

    "Security denied visitor entry.",

    "Parking sticker not received.",

    "Parking slot incorrectly assigned.",

    "Water leakage in basement.",

    "Lift is not working.",

    "Clubhouse booking failed.",

    "Swimming pool access issue.",

    "Electricity issue in apartment.",

    "App is showing incorrect dues.",

    "Unable to login to application.",

    "Account verification pending.",

    "Maintenance receipt not generated.",

    "Intercom is not working.",

    "Garbage collection complaint.",

    "Common lights are not functioning."

]


# ============================================================
# Helper Function
# Generate Random Ticket Date
# ============================================================

def generate_ticket_creation_date():

    start_date = datetime(2024, 1, 1)

    end_date = datetime(2026, 6, 30)

    random_days = random.randint(

        0,

        (end_date - start_date).days

    )

    return start_date + timedelta(days=random_days)


# ============================================================
# Helper Function
# Generate Ticket Closed Date
# ============================================================

def generate_ticket_closed_date(ticket_creation_date):

    resolution_days = random.randint(

        0,

        7

    )

    resolution_hours = random.randint(

        0,

        23

    )

    return ticket_creation_date + timedelta(

        days=resolution_days,

        hours=resolution_hours

    )


# ============================================================
# Empty List
# ============================================================

tickets = []


# ============================================================
# Generate Ticket Records
# ============================================================

for i in range(1, TOTAL_TICKETS + 1):

    ticket_id = f"TKT{i:06d}"

    customer_id = f"CUST{random.randint(1,TOTAL_CUSTOMERS):05d}"

    employee_id = f"EMP{random.randint(1,TOTAL_EMPLOYEES):03d}"

    category_id = f"CAT{random.randint(1,TOTAL_CATEGORIES):03d}"

    society_id = f"SOC{random.randint(1,TOTAL_SOCIETIES):04d}"

    ticket_creation_date = generate_ticket_creation_date()

    ticket_closed_date = generate_ticket_closed_date(

        ticket_creation_date

    )

    conversation_date = ticket_creation_date

    ticket_channel = random.choice(

        TICKET_CHANNELS

    )

    conversation_text = random.choice(

        CONVERSATIONS

    )
    
    # ========================================================
    # Dirty Data Injection
    # ========================================================

    if random.random() < 0.03:

        customer_id = None

    if random.random() < 0.02 and customer_id!= None:

        customer_id = "CUST09001"

    if random.random() < 0.03 and customer_id!= None:

        customer_id = customer_id.lower()

    if random.random() < 0.03:

        employee_id = None

    if random.random() < 0.02 and employee_id!= None:

        employee_id = "EMP051"

    if random.random() < 0.03 and employee_id!= None:

        employee_id = employee_id.lower()

    if random.random() < 0.03:

        category_id = None

    if random.random() < 0.02 and category_id!= None:

        category_id = "CAT009"

    if random.random() < 0.03 and category_id!= None:

        category_id = category_id.lower()

    if random.random() < 0.03:

        society_id = None

    if random.random() < 0.02 and society_id!= None:

        society_id = "SOC1001"

    if random.random() < 0.03 and society_id!= None:

        society_id = society_id.lower()

    if random.random() < 0.04 and ticket_channel!= None:

        ticket_channel = ticket_channel.lower()

    if random.random() < 0.03 and ticket_channel!= None:

        ticket_channel = ticket_channel.upper()

    if random.random() < 0.02  and conversation_text!= None:

        ticket_channel = "Whatsapp"

    if random.random() < 0.02:

        ticket_channel = None

    if random.random() < 0.05 and conversation_text!= None:

        conversation_text = conversation_text.upper()

    if random.random() < 0.05:

        conversation_text = conversation_text.lower()

    if random.random() < 0.04 and conversation_text!= None:

        conversation_text = " " + conversation_text

    if random.random() < 0.04 and conversation_text!= None:

        conversation_text = conversation_text + " "

    if random.random() < 0.03:

        conversation_text = None

    if random.random() < 0.02 and ticket_closed_date!= None:

        ticket_closed_date = None

    if random.random() < 0.02 and ticket_creation_date!= None:

        ticket_creation_date = None

    if random.random() < 0.02 and conversation_date!= None:

        conversation_date = None

    # ========================================================
    # Store Record
    # ========================================================

    ticket = {

        "ticket_id": ticket_id,

        "customer_id": customer_id,

        "conversation_date": conversation_date,

        "ticket_creation_date": ticket_creation_date,

        "ticket_channel": ticket_channel,

        "conversation_text": conversation_text,

        "category_id": category_id,

        "ticket_closed_date": ticket_closed_date,

        "emp_id": employee_id,

        "society_id": society_id

    }

    tickets.append(ticket)


# ============================================================
# Create DataFrame
# ============================================================

ticket_df = pd.DataFrame(tickets)


# ============================================================
# Introduce Duplicate Records
#
# Purpose:
# Duplicate tickets are intentionally created to demonstrate
# SQL duplicate identification and removal techniques.
# ============================================================

duplicate_rows = ticket_df.sample(

    frac=0.02,

    random_state=42

)

ticket_df = pd.concat(

    [

        ticket_df,

        duplicate_rows

    ],

    ignore_index=True

)


# ============================================================
# Shuffle Dataset
#
# Prevent duplicate records from appearing together.
# ============================================================

ticket_df = ticket_df.sample(

    frac=1,

    random_state=42

).reset_index(drop=True)


# ============================================================
# Export CSV
# ============================================================

ticket_df.to_csv(

    OUTPUT_FILE,

    index=False

)


# ============================================================
# Summary Statistics
# ============================================================

print()

print("===============================================")
print(" Ticket Fact Data Generated Successfully")
print("===============================================")

print()

print(f"Total Tickets Generated : {len(tickets)}")

print(f"Final Records in CSV    : {len(ticket_df)}")

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

print(ticket_df.isnull().sum())

print()

print("Duplicate Rows")

print()

print(

    ticket_df.duplicated().sum()

)

print()

print("Ticket Channel Distribution")

print()

print(

    ticket_df["ticket_channel"]

    .value_counts(

        dropna=False

    )

)

print()

print("Top 10 Ticket Categories")

print()

print(

    ticket_df["category_id"]

    .value_counts(

        dropna=False

    )

    .head(10)

)

print()

print("Top 10 Assigned Employees")

print()

print(

    ticket_df["emp_id"]

    .value_counts(

        dropna=False

    )

    .head(10)

)

print()

print("===============================================")