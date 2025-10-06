# Laboratory assignment 3

This is a small web application project that I created while studying cloud computing course in the Master's program for Software Engineering at Vilnius University. I deployed this application using Render at (<https://render.com/>) with free to use cloud services.

## Requirements

- Make web application with CRUD (Create, Read, Update Delete + list data) functionality of any kind of entities on any PaaS. Create and update functions should check input of at least 4 different data types.

## Solution

- I developed a web application using the MVC architectural pattern and the Flask web framework.
- The application supports creating, editing, viewing, and deleting tasks.
- Four task properties can be modified: title, description, due date, and completion status.
- Data validation rules include: the title and due date cannot be blank, the title must contain non-numeric characters, and the due date cannot be in the past.
- The database layer is implemented using SQLAlchemy ORM.
- The application leverages an API to perform CRUD operations, with API routes also used on the front end.
- The front end is built using the Jinja2 templating engine, without any additional front-end libraries.
- Unit tests for all API routes were implemented using pytest, achieving 100% test coverage.
- The application was deployed using Render's Web hosting service.
- The database was hosted on Render's free PostgreSQL service.

## How to run this project locally

1. **Create folder for your project (you can use any name)**:

    ```sh
    mkdir project
    cd project
    ```

2. **Create and activate virtual environment**:

    ```sh
    python -m venv venv
    source venv/bin/activate
    ```

3. **Clone github repository**:

    ```sh
    git clone git@github.com:Dronzillla/vu_cloud_lab3.git
    cd vu_cloud_lab3/
    ```

4. **Install requirements**:

    ```sh
    pip install -r requirements.txt
    ```

5. **Run docker image for local database**:

    ```sh
    docker-compose up -d
    ```

6. **Run the application**:

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

- Dominykas (<https://github.com/Dronzillla>)
