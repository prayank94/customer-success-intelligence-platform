# ============================================================
# Project : Customer Success Intelligence Platform
# File    : generate_tickets.py
# Purpose : Generate Realistic Customer Support Tickets
#
# Author  : Prayank Gupta
#
# Description:
#
# This script generates realistic customer support tickets
# using the existing master data.
#
# Master Data Used:
#
#   dim_society.csv
#   dim_customer.csv
#   dim_employee.csv
#   dim_ticket_category.csv
#
# The generated tickets contain:
#
# - realistic customer complaints
# - multilingual text
# - Hinglish
# - random spelling mistakes
# - transaction IDs
# - amounts
# - flat numbers
# - names
# - dirty data
#
# Output
#
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

RANDOM_SEED = 42

TOTAL_TICKETS = 50000

OUTPUT_FILE = "C:/AnalyticsProjects/customer-success-intelligence-platform/data/raw/fact_ticket.csv"

START_DATE = datetime(2024, 1, 1)

END_DATE = datetime(2026, 6, 30)

random.seed(RANDOM_SEED)


# ============================================================
# Read Master Data
# ============================================================

society_df = pd.read_csv(
    "C:/AnalyticsProjects/customer-success-intelligence-platform/data/raw/dim_society.csv"
)

customer_df = pd.read_csv(
    "C:/AnalyticsProjects/customer-success-intelligence-platform/data/raw/dim_customer.csv"
)

employee_df = pd.read_csv(
    "C:/AnalyticsProjects/customer-success-intelligence-platform/data/raw/dim_employee.csv"
)

category_df = pd.read_csv(
    "C:/AnalyticsProjects/customer-success-intelligence-platform/data/raw/dim_ticket_category.csv"
)


# ============================================================
# Display Summary
# ============================================================

print()

print("==========================================")
print(" Master Data Loaded Successfully")
print("==========================================")

print()

print(
    f"Societies       : {len(society_df)}"
)

print(
    f"Customers       : {len(customer_df)}"
)

print(
    f"Employees       : {len(employee_df)}"
)

print(
    f"Categories      : {len(category_df)}"
)

print()

print("==========================================")

# ============================================================
# Greetings
# ============================================================

GREETINGS = [

    "Hi Team,",

    "Hello Team,",

    "Hi Support Team,",

    "Hello Support,",

    "Dear Team,",

    "Hi,",

    "Hello,",

    "Good Morning Team,",

    "Good Evening Team,",

    "Namaste Team,"
]


# ============================================================
# Closings
# ============================================================

CLOSINGS = [

    "Thanks.",

    "Thank you.",

    "Regards,",    

    "Kind Regards,",

    "Awaiting your response.",

    "Please help.",

    "Please resolve this.",

    "Looking forward to your response.",

    "Thanks & Regards,",

    "Waiting for an update."
]


# ============================================================
# Hinglish Phrases
# ============================================================

HINGLISH_PHRASES = [

    "Please jaldi resolve kar dijiye.",

    "Issue abhi bhi aa raha hai.",

    "Payment ho gaya but app update nahi hua.",

    "Koi update hai kya?",

    "Please check once.",

    "Thoda urgent hai.",

    "Customer support se koi reply nahi mila.",

    "Issue ab tak resolve nahi hua.",

    "Please help ASAP.",

    "Kindly dekh lijiye."
]


# ============================================================
# Emojis
# ============================================================

EMOJIS = [

    "",

    "",

    "",

    "🙂",

    "😞",

    "😢",

    "🙏",

    "👍",

    "😡"
]


# ============================================================
# Urgency Phrases
# ============================================================

URGENCY = [

    "",

    "",

    "",

    "This is urgent.",

    "Kindly resolve today.",

    "Please check immediately.",

    "Need urgent assistance.",

    "Please treat this as high priority.",

    "This has been pending for two days.",

    "Issue is impacting daily activities."
]


# ============================================================
# Time References
# ============================================================

TIME_REFERENCES = [

    "today",

    "yesterday",

    "last night",

    "this morning",

    "two days ago",

    "last week",

    "around 8 PM",

    "around 10 AM",

    "few hours ago",

    "since yesterday"
]


# ============================================================
# Random Names
# ============================================================

PERSON_NAMES = [

    "Rahul",

    "Priya",

    "Ankit",

    "Neha",

    "Amit",

    "Pooja",

    "Rohit",

    "Sneha",

    "Vikram",

    "Nisha",

    "Arjun",

    "Meera",

    "Karan",

    "Divya",

    "Suresh",

    "Ramesh",

    "Ayesha",

    "Nikhil",

    "Harish",

    "Swati"
]


# ============================================================
# Payment Amounts
# ============================================================

PAYMENT_AMOUNTS = [

    1200,

    1800,

    2200,

    2500,

    2800,

    3000,

    3245,

    3500,

    4200,

    5000,

    6500,

    8200
]


# ============================================================
# Vehicle Prefix
# ============================================================

VEHICLE_PREFIX = [

    "KA",

    "MH",

    "DL",

    "TN",

    "TS",

    "AP",

    "GJ"
]


# ============================================================
# Visitor Names
# ============================================================

VISITOR_NAMES = [

    "Rahul Sharma",

    "Amit Kumar",

    "Rakesh Singh",

    "Pooja Sharma",

    "Priya Verma",

    "Anjali Gupta",

    "Vikas Jain",

    "Rohit Patil",

    "Neha Kapoor",

    "Sanjay Mishra"
]

# ============================================================
# Helper Functions
# ============================================================

def generate_ticket_id(ticket_number):

    return f"TKT{ticket_number:06d}"


# ============================================================
# Generate Random Date
# ============================================================

def generate_ticket_creation_date():

    random_days = random.randint(

        0,

        (END_DATE - START_DATE).days

    )

    random_hours = random.randint(0, 23)

    random_minutes = random.randint(0, 59)

    return (

        START_DATE +

        timedelta(

            days=random_days,

            hours=random_hours,

            minutes=random_minutes

        )

    )


# ============================================================
# Generate Closed Date
# ============================================================

def generate_ticket_closed_date(ticket_creation_date):

    if random.random() < 0.20:

        return None

    return (

        ticket_creation_date +

        timedelta(

            hours=random.randint(1, 120)

        )

    )


# ============================================================
# Generate Transaction ID
# ============================================================

def generate_transaction_id():

    return (

        "TXN"

        +

        str(

            random.randint(

                10000000,

                99999999

            )

        )

    )


# ============================================================
# Generate Random Payment Amount
# ============================================================

def generate_payment_amount():

    return random.choice(

        PAYMENT_AMOUNTS

    )


# ============================================================
# Generate Vehicle Number
# ============================================================

def generate_vehicle_number():

    state = random.choice(

        VEHICLE_PREFIX

    )

    district = random.randint(

        1,

        99

    )

    letters = "".join(

        random.choices(

            "ABCDEFGHIJKLMNOPQRSTUVWXYZ",

            k=2

        )

    )

    number = random.randint(

        1000,

        9999

    )

    return (

        f"{state}"

        f"{district:02d}"

        f"{letters}"

        f"{number}"

    )


# ============================================================
# Random Emoji
# ============================================================

def generate_emoji():

    return random.choice(

        EMOJIS

    )


# ============================================================
# Random Greeting
# ============================================================

def generate_greeting():

    return random.choice(

        GREETINGS

    )


# ============================================================
# Random Closing
# ============================================================

def generate_closing():

    return random.choice(

        CLOSINGS

    )


# ============================================================
# Random Hinglish Phrase
# ============================================================

def generate_hinglish():

    return random.choice(

        HINGLISH_PHRASES

    )


# ============================================================
# Random Urgency
# ============================================================

def generate_urgency():

    return random.choice(

        URGENCY

    )


# ============================================================
# Random Time Reference
# ============================================================

def generate_time_reference():

    return random.choice(

        TIME_REFERENCES

    )


# ============================================================
# Random Visitor
# ============================================================

def generate_visitor_name():

    return random.choice(

        VISITOR_NAMES

    )


# ============================================================
# Random Person Name
# ============================================================

def generate_person_name():

    return random.choice(

        PERSON_NAMES

    )


# ============================================================
# Random Typo Generator
# ============================================================

def introduce_typo(text):

    if text is None:

        return text

    if random.random() > 0.10:

        return text

    words = text.split()

    if len(words) == 0:

        return text

    index = random.randint(

        0,

        len(words)-1

    )

    word = words[index]

    if len(word) > 4:

        position = random.randint(

            1,

            len(word)-2

        )

        word = (

            word[:position]

            +

            word[position+1:]

        )

        words[index] = word

    return " ".join(words)


# ============================================================
# Random Extra Spaces
# ============================================================

def introduce_extra_spaces(text):

    if text is None:

        return text

    if random.random() < 0.10:

        text = " " + text

    if random.random() < 0.10:

        text = text + " "

    return text


# ============================================================
# Random Capitalization
# ============================================================

def random_case(text):

    if text is None:

        return text

    probability = random.random()

    if probability < 0.05:

        return text.upper()

    if probability < 0.10:

        return text.lower()

    return text

# ============================================================
# Payment Complaint Generator
# ============================================================

def generate_payment_complaint():

    amount = generate_payment_amount()

    txn = generate_transaction_id()

    greeting = generate_greeting()

    closing = generate_closing()

    urgency = generate_urgency()

    hinglish = generate_hinglish()

    time_reference = generate_time_reference()

    complaint = f"""{greeting}

I made a maintenance payment of ₹{amount} {time_reference}.

Transaction ID : {txn}

The amount has been deducted from my bank account but it is still showing as pending in the application.

{hinglish}

{urgency}

{closing}
"""

    complaint = introduce_typo(complaint)

    complaint = introduce_extra_spaces(complaint)

    complaint = random_case(complaint)

    return complaint


# ============================================================
# Visitor Complaint Generator
# ============================================================

def generate_visitor_complaint():

    visitor = generate_visitor_name()

    greeting = generate_greeting()

    closing = generate_closing()

    urgency = generate_urgency()

    complaint = f"""{greeting}

Visitor {visitor} has been waiting at the main gate for approval.

The visitor request is not appearing in the application.

Kindly check this issue.

{urgency}

{closing}
"""

    complaint = introduce_typo(complaint)

    complaint = introduce_extra_spaces(complaint)

    complaint = random_case(complaint)

    return complaint


# ============================================================
# Parking Complaint Generator
# ============================================================

def generate_parking_complaint():

    vehicle = generate_vehicle_number()

    greeting = generate_greeting()

    closing = generate_closing()

    urgency = generate_urgency()

    complaint = f"""{greeting}

Vehicle number {vehicle} is unable to enter the society.

Parking sticker is already approved but security is denying entry.

Please verify the parking records.

{urgency}

{closing}
"""

    complaint = introduce_typo(complaint)

    complaint = introduce_extra_spaces(complaint)

    complaint = random_case(complaint)

    return complaint

# ============================================================
# Complaint Generator
# ============================================================

def generate_complaint():

    greeting = generate_greeting()

    closing = generate_closing()

    urgency = generate_urgency()

    time_reference = generate_time_reference()

    complaint = f"""{greeting}

I had already raised a complaint {time_reference} but there has been no update from the support team.

The issue is still unresolved.

Kindly look into this.

{urgency}

{closing}
"""

    complaint = introduce_typo(complaint)

    complaint = introduce_extra_spaces(complaint)

    complaint = random_case(complaint)

    return complaint


# ============================================================
# Security Complaint Generator
# ============================================================

def generate_security_complaint():

    visitor = generate_visitor_name()

    greeting = generate_greeting()

    closing = generate_closing()

    urgency = generate_urgency()

    complaint = f"""{greeting}

Security staff did not allow visitor {visitor} to enter even after approval.

The visitor had to wait outside for a long time.

Kindly investigate this incident.

{urgency}

{closing}
"""

    complaint = introduce_typo(complaint)

    complaint = introduce_extra_spaces(complaint)

    complaint = random_case(complaint)

    return complaint


# ============================================================
# Amenities Complaint Generator
# ============================================================

def generate_amenities_complaint():

    greeting = generate_greeting()

    closing = generate_closing()

    urgency = generate_urgency()

    facility = random.choice(

        [

            "gym",

            "clubhouse",

            "swimming pool",

            "children's play area",

            "garden",

            "community hall"

        ]

    )

    complaint = f"""{greeting}

The {facility} has been unavailable for the last few days.

Residents are unable to use the facility.

Please let us know when it will become operational.

{urgency}

{closing}
"""

    complaint = introduce_typo(complaint)

    complaint = introduce_extra_spaces(complaint)

    complaint = random_case(complaint)

    return complaint

# ============================================================
# Account Complaint Generator
# ============================================================

def generate_account_complaint():

    greeting = generate_greeting()

    closing = generate_closing()

    urgency = generate_urgency()

    complaint = f"""{greeting}

I am unable to login to my account.

Even after resetting the password multiple times, the application is showing an invalid login error.

Kindly help me regain access to my account.

{urgency}

{closing}
"""

    complaint = introduce_typo(complaint)

    complaint = introduce_extra_spaces(complaint)

    complaint = random_case(complaint)

    return complaint


# ============================================================
# Other Complaint Generator
# ============================================================

def generate_other_complaint():

    greeting = generate_greeting()

    closing = generate_closing()

    urgency = generate_urgency()

    complaint = f"""{greeting}

I am facing an issue which does not fit into any available complaint category.

Kindly review my request and assign it to the appropriate team.

{urgency}

{closing}
"""

    complaint = introduce_typo(complaint)

    complaint = introduce_extra_spaces(complaint)

    complaint = random_case(complaint)

    return complaint


# ============================================================
# Complaint Router
#
# Generates complaint according to ticket category
# ============================================================

def generate_complaint_by_category(category_name):

    category = str(category_name).strip().lower()

    if category == "maintenance payment":

        return generate_payment_complaint()

    elif category == "visitor management":

        return generate_visitor_complaint()

    elif category == "parking":

        return generate_parking_complaint()

    elif category == "complaint":

        return generate_complaint()

    elif category == "security":

        return generate_security_complaint()

    elif category == "amenities":

        return generate_amenities_complaint()

    elif category == "account":

        return generate_account_complaint()

    else:

        return generate_other_complaint()
    
# ============================================================
# Generate Ticket Records
# ============================================================

tickets = []

for ticket_number in range(1, TOTAL_TICKETS + 1):

    # ========================================================
    # Generate Ticket ID
    # ========================================================

    ticket_id = generate_ticket_id(

        ticket_number

    )


    # ========================================================
    # Select Customer
    # ========================================================

    customer = customer_df.sample(

        n=1

    ).iloc[0]

    customer_id = customer["customer_id"]

    society_id = customer["society_id"]


    # ========================================================
    # Select Category
    # ========================================================

    category = category_df.sample(

        n=1

    ).iloc[0]

    category_id = category["category_id"]

    category_name = category["category_name"]


    # ========================================================
    # Select Employee
    #
    # (For now randomly selected.
    # Later we'll make department-wise assignment.)
    # ========================================================

    employee = employee_df.sample(

        n=1

    ).iloc[0]

    employee_id = employee["employee_id"]


    # ========================================================
    # Ticket Dates
    # ========================================================

    ticket_creation_date = generate_ticket_creation_date()

    ticket_closed_date = generate_ticket_closed_date(

        ticket_creation_date

    )

    conversation_date = ticket_creation_date


    # ========================================================
    # Ticket Channel
    # ========================================================

    ticket_channel = random.choice(

        [

            "Application",

            "WhatsApp",

            "Email",

            "Call",

            "Website",

            "Social Media"

        ]

    )


    # ========================================================
    # Generate Initial Complaint
    # ========================================================

    conversation_text = generate_complaint_by_category(

        category_name

    )

    # ========================================================
    # Dirty Data Injection
    # ========================================================

    if random.random() < 0.03:

        customer_id = None

    if random.random() < 0.02:

        society_id = None

    if random.random() < 0.02:

        employee_id = None

    if random.random() < 0.02:

        category_id = None

    if random.random() < 0.03:

        ticket_channel = ticket_channel.lower()

    if random.random() < 0.03:

        ticket_channel = ticket_channel.upper()

    if random.random() < 0.02:

        ticket_channel = None

    if random.random() < 0.03:

        conversation_text = None

    if random.random() < 0.03:

        ticket_creation_date = None

    if random.random() < 0.03:

        conversation_date = None

    if random.random() < 0.03:

        ticket_closed_date = None

    if random.random() < 0.03 and conversation_text is not None:

        conversation_text = " " + conversation_text

    if random.random() < 0.03 and conversation_text is not None:

        conversation_text = conversation_text + " "

    if random.random() < 0.02:

        ticket_id = ticket_id.lower()


    # ========================================================
    # Create Ticket Dictionary
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


    # ========================================================
    # Append Ticket
    # ========================================================

    tickets.append(ticket)

# ============================================================
# Create DataFrame
# ============================================================

ticket_df = pd.DataFrame(

    tickets

)


# ============================================================
# Introduce Duplicate Records
#
# Purpose:
# Used for SQL duplicate removal practice.
# ============================================================

duplicate_rows = ticket_df.sample(

    frac=0.02,

    random_state=RANDOM_SEED

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
# ============================================================

ticket_df = ticket_df.sample(

    frac=1,

    random_state=RANDOM_SEED

).reset_index(

    drop=True

)


# ============================================================
# Export CSV
# ============================================================

ticket_df.to_csv(

    OUTPUT_FILE,

    index=False

)

# ============================================================
# Generation Summary
# ============================================================

print()

print("=======================================================")

print(" Fact Ticket Data Generated Successfully")

print("=======================================================")

print()

print(

    f"Original Ticket Records : {len(tickets)}"

)

print(

    f"Duplicate Records Added : {len(duplicate_rows)}"

)

print(

    f"Final Records Exported  : {len(ticket_df)}"

)

print()

print("Output File")

print()

print(OUTPUT_FILE)

print()

print("=======================================================")


# ============================================================
# Data Quality Report
# ============================================================

print()

print("Missing Values")

print()

print(

    ticket_df.isnull().sum()

)

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

print("Category Distribution")

print()

print(

    ticket_df["category_id"]

    .value_counts(

        dropna=False

    )

)

print()

print("=======================================================")