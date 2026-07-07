/****************************************************************************************
Project      : Customer Success Inteligence Platform

Script       : 01_database_setup.sql

Purpose      : Creates the project database and required schemas

Author       : Prayank Gupta

Created on   : 06-Jul-2026
****************************************************************************************/



/****************************************************************************************
Step 1       : Create Database
Description  :Creates the CustomerSuccessAnalytics database if it does not already exist
********************************************************************************************

IF DB_ID('CustomerSuccessAnalytics') IS NULL
BEGIN
    CREATE DATABASE CustomerSuccessAnalytics
    PRINT 'Database CustomerSuccessAnalytics created successfully.'
END
ELSE
BEGIN
    PRINT 'Database CustomerSuccessAnalytics already exists.'
END
GO



/****************************************************************************************
Step 2       : Switch Database Context
Description  : Sets CustomerSuccessAnalytics as the active database.
********************************************************************************************/

USE CustomerSuccessAnalytics
GO



/****************************************************************************************
Step 3       : Create Analytics Schema
Description  : Creates the Analytics schema if it does not already exist.
********************************************************************************************/

IF NOT EXISTS
    (SELECT * FROM sys.schemas WHERE name = 'analytics')
    BEGIN
        EXEC('CREATE SCHEMA analytics')
        PRINT 'Schema analytics created successfully.'
    END
ELSE
    BEGIN
        PRINT 'Schema analytics already exists.'
    END
GO



/****************************************************************************************
Step 4       : Create Reporting Schema
Description  : Creates the Reporting schema if it foes not already exist.
********************************************************************************************/

IF NOT EXISTS
    (SELECT * FROM sys.schemas WHERE name = 'reporting')
    BEGIN
        EXEC('CREATE SCHEMA reporting')
        PRINT 'Schema reporting created succesfully.'
    END
ELSE
    BEGIN
        PRINT 'schema repoting already exists.'
    END
GO