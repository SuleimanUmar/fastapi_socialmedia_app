# Set up FastAPI application with basic CRUD endpoints

- Created 'main.py' in the 'app' directory with CRUD operations:
  - GET /posts to retrieve all posts
  - POST /posts to create a new post
  - GET /posts/{id} to retrieve a specific post by ID
  - DELETE /posts/{id} to delete a post by ID
  - PUT /posts/{id} to update a post by ID
- Added 'Post' Pydantic model for request validation and serialization
- Added basic error handling for CRUD operations
- Set up 'run.py' to start the FastAPI application using Uvicorn
- Ensured proper project structure and package initialization with '__init__.py'
- Included initial sample posts for testing endpoints
