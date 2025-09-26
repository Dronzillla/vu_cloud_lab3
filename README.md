# Laboratory assignment 1
This is a small web application project using APIs that I completed while studying the "Software Systems Architecture and Design" course in the Master's program for Software Engineering at Vilnius University.

## Laboratory assignment 1.A requirements
- Create MVC, MVU or MVVM architectural pattern driven web site
- Site should allow creating, editing, viewing and deleting of at least one entity that is the main focus of business aplication (no persistence required)
- Business entity should contain at least 4 editable properties
- Implement validation for all editable properties in create and update scenarios
- Demonstrate usage of DI+IOC

## Laboratory assignment 1.B requirements
- Create Web service as API
- Demonstrate 1 business entity creation, reading, editing, deleting, use 4 HTTP verbs (no persistence required)
- Business entity should contain at least 4 editable properties
- Unit tests for all API public contracts (100% coverage)

## Laboratory assignment 1.C requirements
- Implement DB layer by using ORM or plain SQL with Repository pattern
- Demonstrate 1 business entity creation, reading, editing, deleting
- Business entity should contain at least 4 editable properties
- Integrate 1.A, 1.B and 1.C alltogether (website uses API to manipulate data, where API uses DB layer to manipulate data in database)

## Solution
- I developed a web application using the MVC architectural pattern and the Flask web framework.
- The application supports creating, editing, viewing, and deleting tasks.
- Four task properties can be modified: title, description, due date, and completion status.
- Data validation rules include: the title and due date cannot be blank, the title must contain non-numeric characters, and the due date cannot be in the past.
- The database layer is implemented using SQLAlchemy ORM.
- The application leverages an API to perform CRUD operations, with API routes also used on the front end.
- The front end is built using the Jinja2 templating engine, without any additional front-end libraries.
- Unit tests for all API routes were implemented using pytest, achieving 100% test coverage.

## How to run this project locally
1. **Create folder for your project (you can use any name)**:
    ```sh
    mkdir project_api
    cd project_api
    ```

2. **Create and activate virtual environment**:
    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. **Clone github repository**:
    ```sh
    git clone git@github.com:Dronzillla/vu_sa_lab1.git
    cd vu_sa_lab1/
    ```

4. **Install requirements**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Initialize the database**:
    ```sh
    cd blueprintapp/
    flask db init
    flask db migrate
    flask db upgrade
    ```

7. **Run the application**:
    ```sh
    cd ../
    python3 run.py
    ```

## Testing
To run tests or generate a test coverage report, change the current working directory to the project github repository folder and run the respective commands: 
1. **To run tests**: 
    ```sh
    pytest
    ```
2. **To generate test coverage report for api bp**:
    ```sh
    pytest --cov=blueprintapp/blueprints/api
    ```

## Credits
Contributors' names and contact info:
* Dominykas (https://github.com/Dronzillla)