# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Build a simple REST API using FastAPI to practice routing, request handling, and JSON responses in a modern Python web framework.

## 📝 Tasks

### 🛠️ Create a Basic API

#### Description
Set up a FastAPI application that exposes a few endpoints for managing a list of items.

#### Requirements
Completed program should:

- Create a FastAPI app instance
- Define a `GET /items` endpoint that returns a list of items in JSON format
- Define a `POST /items` endpoint that accepts JSON input and adds a new item
- Return appropriate status codes for successful requests
- Use a simple in-memory list to store item data

### 🛠️ Add Item Details and Validation

#### Description
Extend the API to support retrieving a single item and validating incoming data.

#### Requirements
Completed program should:

- Define a `GET /items/{item_id}` endpoint that returns one item by ID
- Accept item fields such as `id`, `name`, and `description`
- Validate request data using Pydantic models
- Return a 404-style response when an item is not found
- Display JSON data in a clean and readable format

### 🛠️ Improve the API Experience

#### Description
Add small improvements that make the API more realistic and easier to use.

#### Requirements
Completed program should:

- Include a root endpoint such as `GET /` that describes the API
- Use clear endpoint names and JSON response structures
- Handle invalid input gracefully
- Show how the API can be run locally with Uvicorn
- Document the expected behavior in your code comments or response examples
