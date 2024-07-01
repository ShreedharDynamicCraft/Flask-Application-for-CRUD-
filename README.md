# Flask MongoDB CRUD Application

This is a simple Flask application that performs CRUD operations on a MongoDB database for a User resource using a REST API.

## Requirements

- Docker

## Setup and Run

1. Build the Docker image:

    ```sh
    docker build -t flask-mongo-crud .
    ```

2. Run the Docker container:

    ```sh
    docker run -p 5000:5000 flask-mongo-crud
    ```

3. The application will be accessible at `http://localhost:5000`.

## API Endpoints

- `GET /users` - Returns a list of all users.
- `GET /users/<id>` - Returns the user with the specified ID.
- `POST /users` - Creates a new user with the specified data.
- `PUT /users/<id>` - Updates the user with the specified ID with the new data.
- `DELETE /users/<id>` - Deletes the user with the specified ID.

## Testing

Use Postman to send requests to the endpoints and verify that the CRUD operations are working correctly.
# Flask-Application-for-CRUD-
