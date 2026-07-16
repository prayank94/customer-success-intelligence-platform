/****************************************************************************************
PROJECT             : Customer Success Intelligence Platform

SCRIPT              : 02_create_tables.sql (Part 1)

AUTHOR              : Prayank Gupta

PURPOSE             : Creates master dimension tables for the Analytics and Reporting
                      schemas.

TABLES INCLUDED     :

                      1. analytics.dim_society
                      2. reporting.dim_society
                      3. analytics.dim_customers
                      4. reporting.dim_customers

DEPENDENCY          : 01_database_setup.sql

NOTES               :

• Execute 01_database_setup.sql before executing this script.
• Analytics schema stores raw / operational data.
• Reporting schema stores cleaned and validated data.
• Constraints are intentionally kept minimal to support dirty data generation.

****************************************************************************************/

USE CustomerSuccessAnalytics
GO


/****************************************************************************************
TABLE        : analytics.dim_society

PURPOSE      : Stores master information about societies.

SOURCE       : Internal Operational System

TARGET       : Analytics Layer

****************************************************************************************/

IF OBJECT_ID('analytics.dim_society', 'U') IS NULL
BEGIN

    CREATE TABLE analytics.dim_society
    (

        society_id          VARCHAR(10)      NOT NULL PRIMARY KEY,

        society_name        VARCHAR(100)     NULL,

        city                VARCHAR(50)      NULL,

        society_status      VARCHAR(20)      NULL,

        onboarding_date     DATE             NULL,

        total_flats         INT              NULL,

        monthly_revenue     DECIMAL(12,2)    NULL

    )

    PRINT 'Table analytics.dim_society created successfully.'

END
ELSE
BEGIN

    PRINT 'Table analytics.dim_society already exists.'

END
GO


/****************************************************************************************
TABLE        : reporting.dim_society

PURPOSE      : Stores cleaned and validated society master information.

SOURCE       : Analytics Layer

TARGET       : Reporting Layer

****************************************************************************************/

IF OBJECT_ID('reporting.dim_society', 'U') IS NULL
BEGIN

    CREATE TABLE reporting.dim_society
    (

        society_id          VARCHAR(10)      NOT NULL PRIMARY KEY,

        society_name        VARCHAR(100)     NULL,

        city                VARCHAR(50)      NULL,

        society_status      VARCHAR(20)      NULL,

        onboarding_date     DATE             NULL,

        total_flats         INT              NULL,

        monthly_revenue     DECIMAL(12,2)    NULL

    )

    PRINT 'Table reporting.dim_society created successfully.'

END
ELSE
BEGIN

    PRINT 'Table reporting.dim_society already exists.'

END
GO


/****************************************************************************************
TABLE        : analytics.dim_customers

PURPOSE      : Stores customer master information.

SOURCE       : Internal Operational System

TARGET       : Analytics Layer

****************************************************************************************/

IF OBJECT_ID('analytics.dim_customers', 'U') IS NULL
BEGIN

    CREATE TABLE analytics.dim_customers
    (

        customer_id         VARCHAR(10)      NOT NULL PRIMARY KEY,

        customer_name       VARCHAR(100)     NULL,

        customer_type       VARCHAR(30)      NULL,

        customer_email      VARCHAR(150)     NULL,

        customer_contact    VARCHAR(20)      NULL,

        society_id          VARCHAR(10)      NULL

    )

    PRINT 'Table analytics.dim_customers created successfully.'

END
ELSE
BEGIN

    PRINT 'Table analytics.dim_customers already exists.'

END
GO


/****************************************************************************************
TABLE        : reporting.dim_customers

PURPOSE      : Stores cleaned and validated customer master information.

SOURCE       : Analytics Layer

TARGET       : Reporting Layer

****************************************************************************************/

IF OBJECT_ID('reporting.dim_customers', 'U') IS NULL
BEGIN

    CREATE TABLE reporting.dim_customers
    (

        customer_id         VARCHAR(10)      NOT NULL PRIMARY KEY,

        customer_name       VARCHAR(100)     NULL,

        customer_type       VARCHAR(30)      NULL,

        customer_email      VARCHAR(150)     NULL,

        customer_contact    VARCHAR(20)      NULL,

        society_id          VARCHAR(10)      NULL

    )

    PRINT 'Table reporting.dim_customers created successfully.'

END
ELSE
BEGIN

    PRINT 'Table reporting.dim_customers already exists.'

END
GO


/****************************************************************************************
TABLE        : analytics.dim_employees

PURPOSE      : Stores employee master information.

SOURCE       : Internal Operational System

TARGET       : Analytics Layer

****************************************************************************************/

IF OBJECT_ID('analytics.dim_employees', 'U') IS NULL
BEGIN

    CREATE TABLE analytics.dim_employees
    (

        employee_id         VARCHAR(10)      NOT NULL PRIMARY KEY,

        employee_name       VARCHAR(100)     NULL,

        employee_email      VARCHAR(150)     NULL,

        department          VARCHAR(50)      NULL,

        designation         VARCHAR(50)      NULL

    )

    PRINT 'Table analytics.dim_employees created successfully.'

END
ELSE
BEGIN

    PRINT 'Table analytics.dim_employees already exists.'

END
GO


/****************************************************************************************
TABLE        : reporting.dim_employees

PURPOSE      : Stores cleaned and validated employee master information.

SOURCE       : Analytics Layer

TARGET       : Reporting Layer

****************************************************************************************/

IF OBJECT_ID('reporting.dim_employees', 'U') IS NULL
BEGIN

    CREATE TABLE reporting.dim_employees
    (

        employee_id         VARCHAR(10)      NOT NULL PRIMARY KEY,

        employee_name       VARCHAR(100)     NULL,

        employee_email      VARCHAR(150)     NULL,

        department          VARCHAR(50)      NULL,

        designation         VARCHAR(50)      NULL

    )

    PRINT 'Table reporting.dim_employees created successfully.'

END
ELSE
BEGIN

    PRINT 'Table reporting.dim_employees already exists.'

END
GO


/****************************************************************************************
TABLE        : analytics.dim_ticket_category

PURPOSE      : Stores ticket category master information.

SOURCE       : Internal Operational System

TARGET       : Analytics Layer

****************************************************************************************/

IF OBJECT_ID('analytics.dim_ticket_category', 'U') IS NULL
BEGIN

    CREATE TABLE analytics.dim_ticket_category
    (

        category_id         VARCHAR(10)      NOT NULL PRIMARY KEY,

        category_name       VARCHAR(100)     NULL,

        category_group      VARCHAR(50)      NULL

    )

    PRINT 'Table analytics.dim_ticket_category created successfully.'

END
ELSE
BEGIN

    PRINT 'Table analytics.dim_ticket_category already exists.'

END
GO


/****************************************************************************************
TABLE        : reporting.dim_ticket_category

PURPOSE      : Stores cleaned and validated ticket category master information.

SOURCE       : Analytics Layer

TARGET       : Reporting Layer

****************************************************************************************/

IF OBJECT_ID('reporting.dim_ticket_category', 'U') IS NULL
BEGIN

    CREATE TABLE reporting.dim_ticket_category
    (

        category_id         VARCHAR(10)      NOT NULL PRIMARY KEY,

        category_name       VARCHAR(100)     NULL,

        category_group      VARCHAR(50)      NULL

    )

    PRINT 'Table reporting.dim_ticket_category created successfully.'

END
ELSE
BEGIN

    PRINT 'Table reporting.dim_ticket_category already exists.'

END
GO


/****************************************************************************************
TABLE        : analytics.dim_date

PURPOSE      : Stores calendar attributes for time-series analysis.

SOURCE       : System Generated

TARGET       : Analytics Layer

****************************************************************************************/

IF OBJECT_ID('analytics.dim_date', 'U') IS NULL
BEGIN

    CREATE TABLE analytics.dim_date
    (

        date_key            INT              NOT NULL PRIMARY KEY,

        full_date           DATE             NULL,

        calendar_year       INT              NULL,

        calendar_quarter    INT              NULL,

        calendar_month      INT              NULL,

        month_name          VARCHAR(20)      NULL,

        week_number         INT              NULL,

        day_number          INT              NULL,

        day_name            VARCHAR(20)      NULL,

        is_weekend          VARCHAR(5)       NULL

    )

    PRINT 'Table analytics.dim_date created successfully.'

END
ELSE
BEGIN

    PRINT 'Table analytics.dim_date already exists.'

END
GO


/****************************************************************************************
TABLE        : reporting.dim_date

PURPOSE      : Stores cleaned calendar attributes for reporting and time-series analysis.

SOURCE       : Analytics Layer

TARGET       : Reporting Layer

****************************************************************************************/

IF OBJECT_ID('reporting.dim_date', 'U') IS NULL
BEGIN

    CREATE TABLE reporting.dim_date
    (

        date_key            INT              NOT NULL PRIMARY KEY,

        full_date           DATE             NULL,

        calendar_year       INT              NULL,

        calendar_quarter    INT              NULL,

        calendar_month      INT              NULL,

        month_name          VARCHAR(20)      NULL,

        week_number         INT              NULL,

        day_number          INT              NULL,

        day_name            VARCHAR(20)      NULL,

        is_weekend          VARCHAR(5)       NULL

    )

    PRINT 'Table reporting.dim_date created successfully.'

END
ELSE
BEGIN

    PRINT 'Table reporting.dim_date already exists.'

END
GO


/****************************************************************************************
TABLE        : analytics.fact_customer_tickets

PURPOSE      : Stores ticket level information raised by customers.

SOURCE       : Internal Operational System

TARGET       : Analytics Layer

****************************************************************************************/

IF OBJECT_ID('analytics.fact_customer_tickets', 'U') IS NULL
BEGIN

    CREATE TABLE analytics.fact_customer_tickets
    (

        ticket_id               VARCHAR(15)      NOT NULL PRIMARY KEY,

        customer_id             VARCHAR(10)      NULL,

        society_id              VARCHAR(10)      NULL,

        category_id             VARCHAR(10)      NULL,

        employee_id             VARCHAR(10)      NULL,

        ticket_created_date     DATETIME         NULL,

        ticket_closed_date      DATETIME         NULL,

        priority                VARCHAR(20)      NULL,

        status                  VARCHAR(20)      NULL,

        resolution_time_hours   DECIMAL(10,2)    NULL

    )

    PRINT 'Table analytics.fact_customer_tickets created successfully.'

END
ELSE
BEGIN

    PRINT 'Table analytics.fact_customer_tickets already exists.'

END
GO


/****************************************************************************************
TABLE        : reporting.fact_customer_tickets

PURPOSE      : Stores cleaned and validated ticket information.

SOURCE       : Analytics Layer

TARGET       : Reporting Layer

****************************************************************************************/

IF OBJECT_ID('reporting.fact_customer_tickets', 'U') IS NULL
BEGIN

    CREATE TABLE reporting.fact_customer_tickets
    (

        ticket_id               VARCHAR(15)      NOT NULL PRIMARY KEY,

        customer_id             VARCHAR(10)      NULL,

        society_id              VARCHAR(10)      NULL,

        category_id             VARCHAR(10)      NULL,

        employee_id             VARCHAR(10)      NULL,

        ticket_created_date     DATETIME         NULL,

        ticket_closed_date      DATETIME         NULL,

        priority                VARCHAR(20)      NULL,

        status                  VARCHAR(20)      NULL,

        resolution_time_hours   DECIMAL(10,2)    NULL

    )

    PRINT 'Table reporting.fact_customer_tickets created successfully.'

END
ELSE
BEGIN

    PRINT 'Table reporting.fact_customer_tickets already exists.'

END
GO


/****************************************************************************************
TABLE        : analytics.fact_ticket_conversations

PURPOSE      : Stores individual conversations for every customer ticket.

SOURCE       : Internal Operational System

TARGET       : Analytics Layer

****************************************************************************************/

IF OBJECT_ID('analytics.fact_ticket_conversations', 'U') IS NULL
BEGIN

    CREATE TABLE analytics.fact_ticket_conversations
    (

        conversation_id         VARCHAR(15)      NOT NULL PRIMARY KEY,

        ticket_id               VARCHAR(15)      NULL,

        conversation_datetime   DATETIME         NULL,

        communication_channel   VARCHAR(30)      NULL,

        sender                  VARCHAR(20)      NULL,

        conversation_text       VARCHAR(MAX)     NULL

    )

    PRINT 'Table analytics.fact_ticket_conversations created successfully.'

END
ELSE
BEGIN

    PRINT 'Table analytics.fact_ticket_conversations already exists.'

END
GO


/****************************************************************************************
TABLE        : reporting.fact_ticket_conversations

PURPOSE      : Stores cleaned and validated ticket conversations.

SOURCE       : Analytics Layer

TARGET       : Reporting Layer

****************************************************************************************/

IF OBJECT_ID('reporting.fact_ticket_conversations', 'U') IS NULL
BEGIN

    CREATE TABLE reporting.fact_ticket_conversations
    (

        conversation_id         VARCHAR(15)      NOT NULL PRIMARY KEY,

        ticket_id               VARCHAR(15)      NULL,

        conversation_datetime   DATETIME         NULL,

        communication_channel   VARCHAR(30)      NULL,

        sender                  VARCHAR(20)      NULL,

        conversation_text       VARCHAR(MAX)     NULL

    )

    PRINT 'Table reporting.fact_ticket_conversations created successfully.'

END
ELSE
BEGIN

    PRINT 'Table reporting.fact_ticket_conversations already exists.'

END
GO


/****************************************************************************************
TABLE        : analytics.fact_society_agreements

PURPOSE      : Stores agreement metadata extracted from society agreement documents.

SOURCE       : Agreement Management System

TARGET       : Analytics Layer

****************************************************************************************/

IF OBJECT_ID('analytics.fact_society_agreements', 'U') IS NULL
BEGIN

    CREATE TABLE analytics.fact_society_agreements
    (

        agreement_id            VARCHAR(15)      NOT NULL PRIMARY KEY,

        society_id              VARCHAR(10)      NULL,

        agreement_name          VARCHAR(200)     NULL,

        agreement_start_date    DATE             NULL,

        agreement_end_date      DATE             NULL,

        agreement_value         DECIMAL(18,2)    NULL,

        agreement_status        VARCHAR(30)      NULL,

        pdf_file_name           VARCHAR(255)     NULL,

        extraction_status       VARCHAR(30)      NULL

    )

    PRINT 'Table analytics.fact_society_agreements created successfully.'

END
ELSE
BEGIN

    PRINT 'Table analytics.fact_society_agreements already exists.'

END
GO


/****************************************************************************************
TABLE        : reporting.fact_society_agreements

PURPOSE      : Stores cleaned and validated agreement metadata.

SOURCE       : Analytics Layer

TARGET       : Reporting Layer

****************************************************************************************/

IF OBJECT_ID('reporting.fact_society_agreements', 'U') IS NULL
BEGIN

    CREATE TABLE reporting.fact_society_agreements
    (

        agreement_id            VARCHAR(15)      NOT NULL PRIMARY KEY,

        society_id              VARCHAR(10)      NULL,

        agreement_name          VARCHAR(200)     NULL,

        agreement_start_date    DATE             NULL,

        agreement_end_date      DATE             NULL,

        agreement_value         DECIMAL(18,2)    NULL,

        agreement_status        VARCHAR(30)      NULL,

        pdf_file_name           VARCHAR(255)     NULL,

        extraction_status       VARCHAR(30)      NULL

    )

    PRINT 'Table reporting.fact_society_agreements created successfully.'

END
ELSE
BEGIN

    PRINT 'Table reporting.fact_society_agreements already exists.'

END
GO


/****************************************************************************************
TABLE        : analytics.fact_ai_analysis

PURPOSE      : Stores AI generated insights for conversations and agreements.

SOURCE       : AI Processing Pipeline

TARGET       : Analytics Layer

****************************************************************************************/

IF OBJECT_ID('analytics.fact_ai_analysis', 'U') IS NULL
BEGIN

    CREATE TABLE analytics.fact_ai_analysis
    (

        analysis_id             VARCHAR(15)      NOT NULL PRIMARY KEY,

        source_type             VARCHAR(30)      NULL,

        source_id               VARCHAR(15)      NULL,

        sentiment               VARCHAR(20)      NULL,

        summary                 VARCHAR(MAX)     NULL,

        detected_issue          VARCHAR(200)     NULL,

        confidence_score        DECIMAL(5,2)     NULL,

        analysis_date           DATETIME         NULL

    )

    PRINT 'Table analytics.fact_ai_analysis created successfully.'

END
ELSE
BEGIN

    PRINT 'Table analytics.fact_ai_analysis already exists.'

END
GO


/****************************************************************************************
TABLE        : reporting.fact_ai_analysis

PURPOSE      : Stores cleaned and validated AI generated insights.

SOURCE       : Analytics Layer

TARGET       : Reporting Layer

****************************************************************************************/

IF OBJECT_ID('reporting.fact_ai_analysis', 'U') IS NULL
BEGIN

    CREATE TABLE reporting.fact_ai_analysis
    (

        analysis_id             VARCHAR(15)      NOT NULL PRIMARY KEY,

        source_type             VARCHAR(30)      NULL,

        source_id               VARCHAR(15)      NULL,

        sentiment               VARCHAR(20)      NULL,

        summary                 VARCHAR(MAX)     NULL,

        detected_issue          VARCHAR(200)     NULL,

        confidence_score        DECIMAL(5,2)     NULL,

        analysis_date           DATETIME         NULL

    )

    PRINT 'Table reporting.fact_ai_analysis created successfully.'

END
ELSE
BEGIN

    PRINT 'Table reporting.fact_ai_analysis already exists.'

END
GO