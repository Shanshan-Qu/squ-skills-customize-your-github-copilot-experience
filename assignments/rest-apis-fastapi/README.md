# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a fully functional REST API using the FastAPI framework, learning how to define routes, handle request data, and return structured JSON responses.

## 📝 Tasks

### 🛠️ Define API Routes and Return JSON Responses

#### Description
Set up a FastAPI application and create several GET endpoints that return structured data as JSON responses.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Define at least three GET endpoints with meaningful paths (e.g. `/`, `/items`, `/items/{item_id}`)
- Return JSON responses using Python dictionaries or Pydantic models
- Use a path parameter in at least one route to return a specific item by ID
- Run the app with Uvicorn and confirm responses in the browser or with a tool like `curl`

### 🛠️ Handle POST Requests with Request Body Validation

#### Description
Extend the API to accept POST requests that create new items, using Pydantic models to validate incoming request data.

#### Requirements
Completed program should:

- Define a Pydantic `BaseModel` class representing an item (e.g. with `name`, `price`, and `description` fields)
- Create a POST endpoint at `/items` that accepts a request body matching the model
- Validate that required fields are present and return a `422` error automatically for invalid input
- Return the newly created item as a JSON response with an appropriate status code (e.g. `201`)
- Store created items in an in-memory list and allow retrieval via the existing GET `/items` endpoint
