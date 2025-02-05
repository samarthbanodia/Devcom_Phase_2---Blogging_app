# Blogging-app Backend

## Note:

#### http://localhost://5000 is frontend server, replace it as per needed

# Blog API Documentation

## Overview
This is a RESTful API for a blogging platform built with Django REST Framework. The API allows authenticated users to create, read, update, and delete blog posts.

## Features
- Full CRUD operations for blog posts
- Authentication required for all operations
- Author-based permissions (only authors can edit/delete their own posts)
- Automatic timestamp tracking for creation and updates

## API Endpoints

### 1. List and Create Blogs
**Endpoint:** `/api/blogs/`

#### GET (List all blogs)
- **Authentication:** Required
- **Response:** List of all blog posts
- **Example Response:**

## Setup and Running Locally

### Prerequisites
- Python 3.x
- pip (Python package manager)

### 1. Clone the Repository

## Testing with Postman

### Initial Setup
1. Download and install [Postman](https://www.postman.com/downloads/)
2. Create a new Collection called "Blog API"
3. Start your Django server: `python manage.py runserver`

### Authentication Testing

#### 1. User Signup
- Method: `POST`
- URL: `http://127.0.0.1:8000/api/signup/`
- Headers:  ```
  Content-Type: application/json  ```
- Body (raw JSON):  ```json
  {
      "username": "testuser",
      "password": "testpassword",
      "email": "test@example.com"
  }  ```

#### 2. User Login
- Method: `POST`
- URL: `http://127.0.0.1:8000/api/login/`
- Headers:  ```
  Content-Type: application/json  ```
- Body (raw JSON):  ```json
  {
      "username": "testuser",
      "password": "testpassword"
  }  ```
- Save the token from the response for subsequent requests

### Blog API Testing

#### 1. Create Blog Post
- Method: `POST`
- URL: `http://127.0.0.1:8000/api/blogs/`
- Headers:  ```
  Content-Type: application/json
  Authorization: Bearer <your-token>  ```
- Body (raw JSON):  ```json
  {
      "title": "My First Blog Post",
      "content": "This is the content of my first blog post."
  }  ```

#### 2. Get All Blogs
- Method: `GET`
- URL: `http://127.0.0.1:8000/api/blogs/`
- Headers:  ```
  Authorization: Bearer <your-token>  ```

#### 3. Get Single Blog
- Method: `GET`
- URL: `http://127.0.0.1:8000/api/blogs/1/`
- Headers:  ```
  Authorization: Bearer <your-token>  ```

#### 4. Update Blog
- Method: `PUT`
- URL: `http://127.0.0.1:8000/api/blogs/1/`
- Headers:  ```
  Content-Type: application/json
  Authorization: Bearer <your-token>  ```
- Body (raw JSON):  ```json
  {
      "title": "Updated Blog Title",
      "content": "This is the updated content."
  }  ```

#### 5. Delete Blog
- Method: `DELETE`
- URL: `http://127.0.0.1:8000/api/blogs/1/`
- Headers:  ```
  Authorization: Bearer <your-token>  ```

### Tips for Testing in Postman

1. **Environment Variables**
   - Create a new Environment in Postman
   - Add variables:
     - `base_url`: `http://127.0.0.1:8000`
     - `token`: (paste your token here after login)
   - Use variables in requests: 
     - URL: `{{base_url}}/api/blogs/`
     - Headers: `Authorization: Bearer {{token}}`

2. **Testing Workflow**
   1. Run signup request (only once)
   2. Run login request and copy token
   3. Set token in Environment variable
   4. Test other API endpoints

3. **Response Codes**
   - 200: Successful GET/PUT
   - 201: Successful POST
   - 204: Successful DELETE
   - 400: Bad Request
   - 401: Unauthorized
   - 403: Forbidden
   - 404: Not Found

4. **Common Issues and Solutions**
   - **401 Unauthorized**: Check if token is correct and properly formatted
   - **403 Forbidden**: Verify you're the owner of the resource
   - **400 Bad Request**: Check request body format
   - **CORS Error**: Ensure frontend origin is in CORS settings

5. **Collection Runner**
   - Create a test sequence:
     1. Login
     2. Create Blog
     3. Get Blog
     4. Update Blog
     5. Delete Blog
   - Run entire sequence to test full workflow

6. **Request Tests**
   Add these tests in Postman's "Tests" tab:   ```javascript
   // For Login
   pm.test("Login successful", function () {
       pm.response.to.have.status(200);
       pm.response.to.have.jsonBody("token");
   });

   // For Blog Creation
   pm.test("Blog created", function () {
       pm.response.to.have.status(201);
       pm.response.to.have.jsonBody("id");
   });   ```

### Best Practices
1. Always test with a fresh token
2. Verify response data matches request data
3. Test error cases (invalid data, unauthorized access)
4. Use different user accounts to test permissions
5. Clean up test data after testing
