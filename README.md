# Heart Rate Analysis

## Overview

This project enhances an existing codebase for querying health data from a database 
using SQLAlchemy. The primary focus was to make the code more efficient, readable, 
and secure. We improved the architecture by adopting Object-Oriented Programming (OOP)
principles, modularizing the code, and using ORM models to interact with the database.
For detailed project requirements, see the 
[task description](https://github.com/Srmrlt/Welltory_Challenge/blob/main/task/task_code.py).


## Technologies

- Python
- SQLAlchemy
- Pydantic
- Alembic
- Docker

## Key Improvements
- **Code Modularization**: The codebase has been divided into different modules, improving maintainability and readability.
- **OOP Approach**: Object-Oriented Programming principles have been implemented to structure the code more logically and make it easier to manage.
- **ORM Models**: SQLAlchemy ORM models are used instead of direct table definitions, which aids in better data handling and abstraction.
- **Database Migrations**: Alembic is used for database migrations rather than creating tables directly in the code, providing a robust way to handle database schema changes.
- **Enhanced Database Queries**: Queries are implemented using the SQLAlchemy ORM, which allows for more robust, secure, and maintainable database interactions. All queries are executed in accordance with the specific requirements outlined in the assignment.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/Srmrlt/Welltory_Challenge.git
    cd Welltory_Challenge
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Copy the example environment file and set up your environment variables:

    ```bash
    cp .env.example .env
    ```

5. Set up the database:

    ```bash
    docker compose up -d
    alembic upgrade head
    ```

## Running the Project

1. Start the Docker container (if not already started):

    ```bash
    docker-compose up
    ```

2. Load the test data into the database using the script 
located at `task/create_data.sql`.

3. Run the application:

    ```bash
    python app/example.py
    ```

## Thanks for Visiting!
