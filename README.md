# Python SQL Query Engine

## Project Overview

The **Python SQL Query Enginer** is a Python-based interpreter designed to simulate the functionality of an SQL database management system. This project is built to parse and execute SQL-like queries, enabling users to create and manage tables, insert data, and perform queries without the need for an actual database engine. Instead, it utilizes Python dictionaries to store and organize data, offering a simplified, educational insight into how SQL operations are implemented.

### Key Features

1. **Table Creation**
   - Supports the creation of tables with various constraints including `NOTNULL`, `PRIMARY`, `UNIQUE`, `FOREIGN`, `CHECK`, and `DEFAULT`.
   - Allows defining column data types such as `VARCHAR` and `INT`.
   - Prevents the creation of duplicate tables, ensuring database integrity.

2. **Data Insertion**
   - Facilitates the insertion of records into tables based on predefined schemas.
   - Automatically aligns data with the appropriate columns, handling multiple data entries efficiently.

3. **Data Selection**
   - Implements the `SELECT` command to retrieve data from tables.
   - Supports both wildcard (`*`) selection to fetch all columns and specific column selection for more focused queries.
   - Provides a structured query results display, including table headers and data rows.

4. **Table Description**
   - Allows users to view the structure of any table using the `DESC` command.
   - Outputs the column names alongside their constraints, offering a clear schema overview.

5. **Show Tables**
   - Lists all the tables currently in the database, offering a snapshot of the available data structures.
   - Simplifies database management by providing a quick reference to all existing tables.

