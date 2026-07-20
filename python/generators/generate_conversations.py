# ============================================================
# Project : Customer Success Intelligence Platform
# File    : generate_conversations.py
# Purpose : Generate Realistic Customer Support Conversations
#
# Author  : Prayank Gupta
#
# Description
#
# This script generates realistic customer support
# conversations from fact_ticket.csv.
#
# Features
#
# • Dynamic conversation flow
# • Multiple customer messages
# • Multiple employee replies
# • System generated events
# • Random response delays
# • English
# • Hinglish
# • Broken English
# • Typos
# • Emojis
# • WhatsApp style messages
# • CRM style messages
# • Dirty Data
#
# Input
#
# data/raw/fact_ticket.csv
#
# Output
#
# data/raw/fact_conversation.csv
#
# ============================================================



# ============================================================
# Import Libraries
# ============================================================

import random

import pandas as pd

from datetime import timedelta

from datetime import datetime



# ============================================================
# Configuration
# ============================================================

RANDOM_SEED = 42

OUTPUT_FILE = "C:/AnalyticsProjects/customer-success-intelligence-platform/data/raw/fact_conversation.csv"

MIN_MESSAGES = 3

MAX_MESSAGES = 18

SYSTEM_MESSAGE_PROBABILITY = 0.25

MULTIPLE_CUSTOMER_MESSAGE_PROBABILITY = 0.35

MULTIPLE_EMPLOYEE_MESSAGE_PROBABILITY = 0.25

REOPEN_PROBABILITY = 0.08

random.seed(RANDOM_SEED)



# ============================================================
# Read Ticket Data
# ============================================================

ticket_df = pd.read_csv(

    "C:/AnalyticsProjects/customer-success-intelligence-platform/data/raw/fact_ticket.csv"

)

category_df = pd.read_csv(
    "C:/AnalyticsProjects/customer-success-intelligence-platform/data/raw/dim_ticket_category.csv"
)

category_lookup = dict(

    zip(

        category_df["category_id"],

        category_df["category_name"]

    )

)

# ============================================================
# Conversation Scenarios
#
# Every ticket first chooses one scenario.
#
# Scenario decides
#
# • number of replies
# • delay
# • reopen
# • escalation
# • system messages
# ============================================================

SCENARIOS = [

    "Quick Resolution",

    "Customer Follow Up",

    "Delayed Resolution",

    "Escalation",

    "Reopened",

    "Waiting For Customer",

    "Waiting For Internal Team",

    "Long Conversation"

]



# ============================================================
# Sender Types
# ============================================================

SENDER_TYPES = [

    "Customer",

    "Employee",

    "System"

]



# ============================================================
# Employee Personas
# ============================================================

EMPLOYEE_PERSONAS = [

    "Customer Support",

    "Finance Team",

    "Operations Team",

    "Security Team",

    "Technical Team",

    "Facility Team",

    "Supervisor"

]



# ============================================================
# System Events
# ============================================================

SYSTEM_EVENTS = [

    "Ticket Created.",

    "Ticket Assigned.",

    "Ticket Escalated.",

    "Ticket Reassigned.",

    "Status Changed to In Progress.",

    "Status Changed to Waiting For Customer.",

    "Status Changed to Waiting For Internal Team.",

    "Status Changed to Resolved.",

    "Ticket Closed.",

    "Ticket Reopened."

]



# ============================================================
# Display Summary
# ============================================================

print()

print("========================================")

print(" Ticket Data Loaded")

print("========================================")

print()

print(

    f"Tickets Loaded : {len(ticket_df)}"

)

print()

print("========================================")

# ============================================================
# Delay Engine
# ============================================================

def generate_delay(

    scenario,

    sender

):

    if sender == "System":

        return random.randint(

            1,

            5

        )

    if scenario == "Quick Resolution":

        return random.randint(

            2,

            15

        )

    elif scenario == "Customer Follow Up":

        return random.randint(

            10,

            90

        )

    elif scenario == "Delayed Resolution":

        return random.randint(

            120,

            720

        )

    elif scenario == "Escalation":

        return random.randint(

            60,

            360

        )

    elif scenario == "Reopened":

        return random.randint(

            300,

            1440

        )

    elif scenario == "Waiting For Customer":

        return random.randint(

            600,

            2880

        )

    elif scenario == "Waiting For Internal Team":

        return random.randint(

            240,

            1440

        )

    return random.randint(

        5,

        60

    )


# ============================================================
# Speaker Engine
# ============================================================

def choose_sender(

    previous_sender

):

    probability = random.random()

    if probability < SYSTEM_MESSAGE_PROBABILITY:

        return "System"

    if previous_sender == "Customer":

        if probability < MULTIPLE_CUSTOMER_MESSAGE_PROBABILITY:

            return "Customer"

        return "Employee"

    if previous_sender == "Employee":

        if probability < MULTIPLE_EMPLOYEE_MESSAGE_PROBABILITY:

            return "Employee"

        return "Customer"

    return "Customer"


# ============================================================
# Employee Persona
# ============================================================

def choose_employee_persona():

    return random.choice(

        EMPLOYEE_PERSONAS

    )


# ============================================================
# Conversation Scenario
# ============================================================

def choose_scenario():

    return random.choice(

        SCENARIOS

    )


# ============================================================
# Random Emoji
# ============================================================

def add_emoji(

    message

):

    if random.random() < 0.15:

        message = (

            message

            + " "

            + random.choice(

                [

                    "🙂",

                    "🙏",

                    "😞",

                    "👍",

                    "😡",

                    "😊"

                ]

            )

        )

    return message


# ============================================================
# Random Typo
# ============================================================

def introduce_typo(

    message

):

    if random.random() > 0.10:

        return message

    words = message.split()

    if len(words) == 0:

        return message

    word_index = random.randint(

        0,

        len(words)-1

    )

    word = words[word_index]

    if len(word) > 4:

        char = random.randint(

            1,

            len(word)-2

        )

        word = (

            word[:char]

            +

            word[char+1:]

        )

        words[word_index] = word

    return " ".join(

        words

    )


# ============================================================
# Broken English
# ============================================================

def broken_english(

    message

):

    if random.random() > 0.12:

        return message

    replacements = {

        "please":"plz",

        "because":"bcoz",

        "message":"msg",

        "application":"app",

        "transaction":"txn",

        "payment":"paymnt",

        "tomorrow":"tmrw",

        "today":"tdy",

        "yesterday":"ystrdy",

        "before":"bfr"

    }

    for old,new in replacements.items():

        message = message.replace(

            old,

            new

        )

    return message


# ============================================================
# Random Capitalization
# ============================================================

def random_case(

    message

):

    probability = random.random()

    if probability < 0.05:

        return message.upper()

    elif probability < 0.10:

        return message.lower()

    return message


# ============================================================
# WhatsApp Formatting
# ============================================================

def whatsapp_style(

    message

):

    if random.random() < 0.30:

        message = message.replace(

            ". ",

            "\n"

        )

    return message

# ============================================================
# Customer Opening Messages
# ============================================================

CUSTOMER_OPENING = [

    "Hi Team.",

    "Hello.",

    "Need your help.",

    "Please check this issue.",

    "Can someone assist me?",

    "Facing an issue.",

    "Need urgent help.",

    "Issue still exists.",

    "Hello Support Team.",

    "Good Morning."

]


# ============================================================
# Customer Follow Up
# ============================================================

CUSTOMER_FOLLOWUP = [

    "Any update?",

    "Please update.",

    "Still waiting.",

    "Can someone check?",

    "Issue not resolved yet.",

    "Please respond.",

    "Waiting for your reply.",

    "Please help urgently.",

    "Following up.",

    "Need status."

]


# ============================================================
# Customer Frustration
# ============================================================

CUSTOMER_FRUSTRATION = [

    "Nobody has replied.",

    "This is taking too long.",

    "Very disappointed.",

    "Still facing the same issue.",

    "Issue has become frustrating.",

    "Already raised multiple complaints.",

    "This is affecting everyone.",

    "Support is very slow.",

    "Need immediate attention.",

    "Can this be escalated?"

]


# ============================================================
# Customer Information
# ============================================================

CUSTOMER_INFORMATION = [

    "Transaction ID shared.",

    "Screenshot attached.",

    "Visitor name shared.",

    "Vehicle number shared.",

    "Payment details attached.",

    "Flat details shared.",

    "Sharing requested information.",

    "Please find details below."

]


# ============================================================
# Customer Closing
# ============================================================

CUSTOMER_CLOSING = [

    "Thanks.",

    "Thank you.",

    "Issue resolved now.",

    "Everything is working.",

    "Appreciate your support.",

    "Thanks for the help.",

    "Closing this ticket.",

    "Problem solved."

]


# ============================================================
# Employee Greeting
# ============================================================

EMPLOYEE_GREETING = [

    "Hello.",

    "Greetings.",

    "Dear Customer.",

    "Hi.",

    "Good Morning.",

    "Good Evening."

]


# ============================================================
# Employee Investigation
# ============================================================

EMPLOYEE_INVESTIGATION = [

    "We are checking the issue.",

    "Our team is investigating.",

    "We are verifying the records.",

    "Backend team is checking.",

    "Issue has been assigned.",

    "Allow us some time.",

    "Checking with the concerned team.",

    "Looking into the issue."

]


# ============================================================
# Employee Request
# ============================================================

EMPLOYEE_REQUEST = [

    "Please share transaction ID.",

    "Kindly share screenshot.",

    "Please confirm payment amount.",

    "Please confirm flat number.",

    "Please share visitor name.",

    "Please share vehicle number.",

    "Need additional information.",

    "Kindly confirm date and time."

]


# ============================================================
# Employee Escalation
# ============================================================

EMPLOYEE_ESCALATION = [

    "Escalating to senior team.",

    "Forwarding to technical team.",

    "Finance team has been informed.",

    "Operations team is checking.",

    "Supervisor has been notified.",

    "Escalation completed.",

    "Issue sent for priority handling."

]


# ============================================================
# Employee Resolution
# ============================================================

EMPLOYEE_RESOLUTION = [

    "Issue resolved.",

    "Payment updated successfully.",

    "Visitor approved.",

    "Parking access restored.",

    "Issue fixed.",

    "Changes completed.",

    "Everything should work now.",

    "Kindly verify once."

]


# ============================================================
# Employee Closing
# ============================================================

EMPLOYEE_CLOSING = [

    "Thank you.",

    "Have a great day.",

    "Happy to help.",

    "Regards.",

    "Please contact us again if required.",

    "Ticket will now be closed."

]

# ============================================================
# Message Selector
# ============================================================

def get_customer_message(message_type):

    if message_type == "opening":

        return random.choice(CUSTOMER_OPENING)

    elif message_type == "followup":

        return random.choice(CUSTOMER_FOLLOWUP)

    elif message_type == "frustration":

        return random.choice(CUSTOMER_FRUSTRATION)

    elif message_type == "information":

        return random.choice(CUSTOMER_INFORMATION)

    elif message_type == "closing":

        return random.choice(CUSTOMER_CLOSING)

    return random.choice(CUSTOMER_FOLLOWUP)


# ============================================================
# Employee Message Selector
# ============================================================

def get_employee_message(message_type):

    if message_type == "greeting":

        return random.choice(EMPLOYEE_GREETING)

    elif message_type == "investigation":

        return random.choice(EMPLOYEE_INVESTIGATION)

    elif message_type == "request":

        return random.choice(EMPLOYEE_REQUEST)

    elif message_type == "escalation":

        return random.choice(EMPLOYEE_ESCALATION)

    elif message_type == "resolution":

        return random.choice(EMPLOYEE_RESOLUTION)

    elif message_type == "closing":

        return random.choice(EMPLOYEE_CLOSING)

    return random.choice(EMPLOYEE_INVESTIGATION)


# ============================================================
# System Message Selector
# ============================================================

def get_system_message():

    return random.choice(

        SYSTEM_EVENTS

    )

# ============================================================
# Generate Number Of Messages
# ============================================================

def generate_message_count():

    return random.randint(

        MIN_MESSAGES,

        MAX_MESSAGES

    )

# ============================================================
# Build Conversation
# ============================================================

def build_conversation(

    category,

    scenario

):

    messages = []

    previous_sender = "Customer"

    total_messages = generate_message_count()

    for sequence in range(total_messages):

        sender = choose_sender(

            previous_sender

        )

        previous_sender = sender


        # --------------------------------------------
        # Customer Messages
        # --------------------------------------------

        if sender == "Customer":

            probability = random.random()

            if sequence == 0:

                message = get_customer_message(

                    "opening"

                )

            elif probability < 0.25:

                message = get_customer_message(

                    "information"

                )

            elif probability < 0.60:

                message = get_customer_message(

                    "followup"

                )

            elif probability < 0.90:

                message = get_customer_message(

                    "frustration"

                )

            else:

                message = get_customer_message(

                    "closing"

                )


        # --------------------------------------------
        # Employee Messages
        # --------------------------------------------

        elif sender == "Employee":

            probability = random.random()

            if probability < 0.20:

                message = get_employee_message(

                    "greeting"

                )

            elif probability < 0.50:

                message = get_employee_message(

                    "investigation"

                )

            elif probability < 0.70:

                message = get_employee_message(

                    "request"

                )

            elif probability < 0.90:

                message = get_employee_message(

                    "escalation"

                )

            else:

                message = get_employee_message(

                    "resolution"

                )


            persona = choose_employee_persona()

            message = f"{persona}: {message}"


        # --------------------------------------------
        # System Messages
        # --------------------------------------------

        else:

            message = get_system_message()


        # --------------------------------------------
        # AI Noise Engine
        # --------------------------------------------

        message = broken_english(

            message

        )

        message = introduce_typo(

            message

        )

        message = add_emoji(

            message

        )

        message = whatsapp_style(

            message

        )

        message = random_case(

            message

        )

        messages.append(

            {

                "sender": sender,

                "message": message

            }

        )

    return messages

# ============================================================
# Category Knowledge Base
# ============================================================

CATEGORY_CONTEXT = {

    "maintenance payment": {

        "keywords": [

            "payment",

            "maintenance",

            "amount",

            "deducted",

            "receipt",

            "transaction",

            "gateway",

            "refund",

            "upi",

            "bank"

        ],

        "customer_information": [

            "Transaction ID is TXN{txn}.",

            "Amount deducted is ₹{amount}.",

            "Payment was made yesterday.",

            "Money got deducted twice.",

            "Bank shows success.",

            "Application still shows pending.",

            "Receipt not generated.",

            "UPI payment completed."

        ],

        "employee_request": [

            "Please share Transaction ID.",

            "Kindly share payment screenshot.",

            "Can you confirm the payment amount?",

            "Please share payment time."

        ],

        "employee_resolution": [

            "Payment has now been updated.",

            "Gateway has confirmed the transaction.",

            "Receipt has been generated.",

            "Refund has been initiated.",

            "Issue has been resolved."

        ]

    },


    "visitor management": {

        "keywords": [

            "visitor",

            "gate",

            "approval",

            "otp",

            "entry",

            "security"

        ],

        "customer_information": [

            "Visitor name is {visitor}.",

            "Visitor is waiting at Gate 2.",

            "Approval request not received.",

            "OTP has not arrived.",

            "Visitor has been waiting for 20 minutes."

        ],

        "employee_request": [

            "Please share visitor name.",

            "Kindly confirm gate number.",

            "Please resend visitor request."

        ],

        "employee_resolution": [

            "Visitor approval completed.",

            "OTP regenerated successfully.",

            "Security has been informed.",

            "Visitor may now enter."

        ]

    },


    "parking": {

        "keywords": [

            "parking",

            "vehicle",

            "sticker",

            "entry",

            "car"

        ],

        "customer_information": [

            "Vehicle number is {vehicle}.",

            "Parking sticker already approved.",

            "Security denied entry.",

            "Vehicle details updated."

        ],

        "employee_request": [

            "Please confirm vehicle number.",

            "Kindly share parking sticker."

        ],

        "employee_resolution": [

            "Parking access restored.",

            "Vehicle details updated.",

            "Sticker has been activated."

        ]

    },


    "security": {

        "keywords": [

            "security",

            "guard",

            "gate",

            "entry"

        ],

        "customer_information": [

            "Guard denied entry.",

            "Security behaved rudely.",

            "Entry delayed."

        ],

        "employee_request": [

            "Please share incident time.",

            "Kindly provide more details."

        ],

        "employee_resolution": [

            "Supervisor has been informed.",

            "Security team has been notified.",

            "Matter has been resolved."

        ]

    },


    "amenities": {

        "keywords": [

            "gym",

            "pool",

            "clubhouse",

            "garden"

        ],

        "customer_information": [

            "Gym is closed.",

            "Swimming pool unavailable.",

            "Clubhouse locked."

        ],

        "employee_request": [

            "Please confirm the facility name."

        ],

        "employee_resolution": [

            "Maintenance completed.",

            "Facility is operational again."

        ]

    },


    "account": {

        "keywords": [

            "login",

            "password",

            "otp",

            "account"

        ],

        "customer_information": [

            "Unable to login.",

            "Password reset failed.",

            "OTP not received."

        ],

        "employee_request": [

            "Please confirm registered email.",

            "Kindly verify your mobile number."

        ],

        "employee_resolution": [

            "Password reset completed.",

            "Account unlocked.",

            "OTP issue fixed."

        ]

    }

}

# ============================================================
# Conversation Context Engine
#
# Every ticket gets its own context.
# This context remains constant throughout the conversation.
# ============================================================

def build_ticket_context(ticket):

    context = {}

    context["ticket_id"] = ticket["ticket_id"]

    context["customer_id"] = ticket["customer_id"]

    context["society_id"] = ticket["society_id"]

    context["category_id"] = ticket["category_id"]

    context["category_name"] = str(

    category_lookup.get(

        ticket["category_id"],

        "other"

    )

    ).strip().lower()

    context["created_date"] = pd.to_datetime(
        ticket["ticket_creation_date"]
    )

    context["amount"] = random.randint(
        1500,
        8000
    )

    context["transaction_id"] = (
        "TXN"
        +
        str(
            random.randint(
                10000000,
                99999999
            )
        )
    )

    context["visitor"] = random.choice(

        [

            "Rahul Sharma",

            "Amit Kumar",

            "Neha Patel",

            "Pooja Singh",

            "Rakesh Jain"

        ]

    )

    context["vehicle"] = (

        random.choice(

            [

                "KA",

                "MH",

                "DL",

                "TN"

            ]

        )

        +

        str(

            random.randint(

                10,

                99

            )

        )

        +

        random.choice(

            [

                "AB",

                "CD",

                "EF",

                "GH"

            ]

        )

        +

        str(

            random.randint(

                1000,

                9999

            )

        )

    )

    return context

# ============================================================
# Replace Dynamic Values
# ============================================================

def populate_message(

    message,

    context

):

    message = message.replace(

        "{txn}",

        context["transaction_id"]

    )

    message = message.replace(

        "{amount}",

        str(

            context["amount"]

        )

    )

    message = message.replace(

        "{visitor}",

        context["visitor"]

    )

    message = message.replace(

        "{vehicle}",

        context["vehicle"]

    )

    return message

# ============================================================
# Generate Conversations
# ============================================================

conversation_records = []

conversation_number = 1

for _, ticket in ticket_df.iterrows():

    # --------------------------------------------------------
    # Skip Dirty Tickets
    # --------------------------------------------------------

    if pd.isna(ticket["ticket_id"]):

        continue

    if pd.isna(ticket["ticket_creation_date"]):

        continue

    # --------------------------------------------------------
    # Build Context
    # --------------------------------------------------------

    context = build_ticket_context(

        ticket

    )

    # --------------------------------------------------------
    # Scenario
    # --------------------------------------------------------

    scenario = choose_scenario()

    # --------------------------------------------------------
    # Conversation
    # --------------------------------------------------------

    conversation = build_conversation(

        context["category_name"],

        scenario

    )

    # --------------------------------------------------------
    # Timestamp
    # --------------------------------------------------------

    current_timestamp = context["created_date"]

    # --------------------------------------------------------
    # Sequence Number
    # --------------------------------------------------------

    sequence = 1

    # --------------------------------------------------------
    # Every Message
    # --------------------------------------------------------

    for row in conversation[1:]:

        sender = row["sender"]

        message = row["message"]

        if sender == "Customer":

            if message in CUSTOMER_OPENING:

                continue

        # --------------------------------------------
        # Replace Dynamic Values
        # --------------------------------------------

        message = populate_message(

            message,

            context

        )

        # --------------------------------------------
        # Delay
        # --------------------------------------------

        delay = generate_delay(

            scenario,

            sender

        )

        current_timestamp = (

            current_timestamp +

            timedelta(

                minutes=delay

            )

        )

        # --------------------------------------------
        # Create Record
        # --------------------------------------------

        record = {

            "conversation_id":f"CONV{conversation_number:07d}",

            "ticket_id":

                context["ticket_id"],

            "message_sequence":

                sequence,

            "sender_type":

                sender,

            "message_timestamp":

                current_timestamp,

            "message_text":

                message

        }

        conversation_records.append(

            record

        )

        conversation_number += 1

        sequence += 1

    # --------------------------------------------------------
    # First Message
    #
    # Always use original ticket complaint
    # --------------------------------------------------------

    first_message = ticket["conversation_text"]

    if pd.isna(first_message):

        first_message = random.choice(

            CUSTOMER_OPENING

        )

    else:

        first_message = str(first_message)

        first_message = broken_english(

            first_message

        )

        first_message = introduce_typo(

            first_message

        )

        first_message = add_emoji(

            first_message

        )

        first_message = whatsapp_style(

            first_message

        )

        first_message = random_case(

            first_message

        )


    record = {

        "conversation_id": f"CONV{conversation_number:07d}",

        "ticket_id":

            context["ticket_id"],

        "message_sequence":1,

        "sender_type":"Customer",

        "message_timestamp":

            context["created_date"],

        "message_text":

            first_message

    }

    conversation_records.append(

        record

    )

    conversation_number += 1

    sequence = 2

        # =====================================================
        # Dirty Data Injection
        # =====================================================

if random.random() < 0.02:

    record["sender_type"] = None

if random.random() < 0.02:

    record["message_timestamp"] = None

if random.random() < 0.02:

    record["message_text"] = None

if random.random() < 0.03 and record["message_text"] is not None:

    record["message_text"] = " " + record["message_text"]

if random.random() < 0.03 and record["message_text"] is not None:

    record["message_text"] = record["message_text"] + " "

if random.random() < 0.02:

    record["conversation_id"] = record["conversation_id"].lower()

if random.random() < 0.02:

    record["ticket_id"] = record["ticket_id"].lower()

if random.random() < 0.02:

    record["message_sequence"] = None 


# ============================================================
# Create DataFrame
# ============================================================

conversation_df = pd.DataFrame(

    conversation_records

)


# ============================================================
# Introduce Duplicate Records
# ============================================================

duplicate_rows = conversation_df.sample(

    frac=0.02,

    random_state=RANDOM_SEED

)

conversation_df = pd.concat(

    [

        conversation_df,

        duplicate_rows

    ],

    ignore_index=True

)


# ============================================================
# Shuffle Dataset
# ============================================================

conversation_df = conversation_df.sample(

    frac=1,

    random_state=RANDOM_SEED

).reset_index(

    drop=True

)


# ============================================================
# Export CSV
# ============================================================

conversation_df.to_csv(

    OUTPUT_FILE,

    index=False

)

# ============================================================
# Summary
# ============================================================

print()

print("===================================================")

print(" Conversation Dataset Generated Successfully")

print("===================================================")

print()

print(

    f"Conversation Records : {len(conversation_records)}"

)

print(

    f"Duplicate Records    : {len(duplicate_rows)}"

)

print(

    f"Final Records        : {len(conversation_df)}"

)

print()

print("Output File")

print()

print(OUTPUT_FILE)

print()

print("===================================================")


# ============================================================
# Missing Values
# ============================================================

print()

print("Missing Values")

print()

print(

    conversation_df.isnull().sum()

)

print()

print("Duplicate Rows")

print()

print(

    conversation_df.duplicated().sum()

)

print()

print("Sender Distribution")

print()

print(

    conversation_df["sender_type"]

    .value_counts(

        dropna=False

    )

)

print()

print("===================================================")