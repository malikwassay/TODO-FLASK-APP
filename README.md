# Flask Todo API with JWT Authentication
## Features

- User registration and login with JWT authentication
- Create, read, update, and delete tasks
- Mark tasks as completed
- Secure routes with JWT authentication
- SQLite database for data persistence

## Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd todo_flask_app
```
2. Make .env file containing the following:.
- `SECRET_KEY= "REPLACE WITH YOUR SECRET KEY"`
- `JWT_SECRET_KEY="REPLACE WITH YOUR JWT SECRET KEY"`
- `DATABASE_URL=sqlite:///todo.db`
`

3. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

4. Install dependencies:
```bash
pip install -r requirements.txt
```

5. Run the application:
```bash
python run.py
```

The server will start running at `http://localhost:5000`

## API Endpoints

### Authentication

- `POST /auth/register` - Register a new user
  - Body: `{"username": "user", "password": "Pass123!"}`

- `POST /auth/login` - Login and get JWT token
  - Body: `{"username": "user", "password": "Pass123!"}`

### Tasks

All task endpoints require JWT authentication (Bearer token in Authorization header)

- `GET /api/tasks` - Get all tasks for authenticated user
- `POST /api/tasks` - Create a new task
  - Body: `{"title": "Task title", "description": "Task description"}`
- `PUT /api/tasks/<task_id>` - Update a task
  - Body: `{"title": "Updated title", "description": "Updated description", "completed": true}`
- `DELETE /api/tasks/<task_id>` - Delete a task

## Password Requirements

- Minimum 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one number
- At least one special character

## Testing

You can use tools like Postman or curl to test the API endpoints. Make sure to include the JWT token in the Authorization header for protected routes:

### **Step 4: Add Requests**

#### **1. User Registration**
- **Request Type**: `POST`
- **URL**: `http://localhost:5000/auth/register`
- **Headers**:
  - Key: `Content-Type`
  - Value: `application/json`
- **Body**:
  - Select **raw** and choose **JSON** from the dropdown.
  - Example Body:
    ```json
    {
      "username": "testuser",
      "password": "Test@1234"
    }
    ```

#### **2. User Login**
- **Request Type**: `POST`
- **URL**: `http://localhost:5000/auth/login`
- **Headers**:
  - Key: `Content-Type`
  - Value: `application/json`
- **Body**:
  - Select **raw** and choose **JSON** from the dropdown.
  - Example Body:
    ```json
    {
      "username": "testuser",
      "password": "Test@1234"
    }
    ```
- **Save the Token**:
  - After sending the request, copy the `access_token` from the response.

#### **3. Create a New Task**
- **Request Type**: `POST`
- **URL**: `http://localhost:5000/api/tasks`
- **Headers**:
  - Key: `Content-Type`
  - Value: `application/json`
  - Key: `Authorization`
  - Value: `Bearer <your-jwt-token>` (replace `<your-jwt-token>` with the token from the login response).
- **Body**:
  - Select **raw** and choose **JSON** from the dropdown.
  - Example Body:
    ```json
    {
      "title": "Sample Task",
      "description": "This is a sample task."
    }
    ```

#### **4. Get All Tasks**
- **Request Type**: `GET`
- **URL**: `http://localhost:5000/api/tasks`
- **Headers**:
  - Key: `Authorization`
  - Value: `Bearer <your-jwt-token>`

#### **5. Update a Task**
- **Request Type**: `PUT`
- **URL**: `http://localhost:5000/api/tasks/<task_id>` (replace `<task_id>` with the actual task ID).
- **Headers**:
  - Key: `Content-Type`
  - Value: `application/json`
  - Key: `Authorization`
  - Value: `Bearer <your-jwt-token>`
- **Body**:
  - Select **raw** and choose **JSON** from the dropdown.
  - Example Body:
    ```json
    {
      "title": "Updated Task",
      "completed": true
    }
    ```

#### **6. Delete a Task**
- **Request Type**: `DELETE`
- **URL**: `http://localhost:5000/api/tasks/<task_id>` (replace `<task_id>` with the actual task ID).
- **Headers**:
  - Key: `Authorization`
  - Value: `Bearer <your-jwt-token>`

---
