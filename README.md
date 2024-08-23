`README.md` 

---

# Courses API Documentation

This API allows you to manage courses and course instances.

## Base URL

`http://127.0.0.1:8000/api/`

## Endpoints

### Courses

#### **1. List All Courses**

- **Endpoint**: `/courses/`
- **Method**: `GET`
- **Description**: Retrieve a list of all courses.
- **Response Example**:

  ```json
  [
      {
          "id": 1,
          "title": "Introduction to Programming",
          "course_code": "CS101",
          "description": "This course covers the basics of programming.",
          "year_of_delivery": 2024,
          "semester_of_delivery": 1
      },
      {
          "id": 2,
          "title": "Data Structures",
          "course_code": "CS102",
          "description": "This course covers the basics of Data Structures.",
          "year_of_delivery": 2024,
          "semester_of_delivery": 1
      }
  ]
  ```

#### **2. Create a New Course**

- **Endpoint**: `/courses/`
- **Method**: `POST`
- **Description**: Create a new course.
- **Request Body Example**:

  ```json
  {
      "title": "Advanced Algorithms",
      "course_code": "CS201",
      "description": "This course covers advanced algorithm design and analysis.",
      "year_of_delivery": 2024,
      "semester_of_delivery": 2
  }
  ```

- **Response Example**:

  ```json
  {
      "id": 3,
      "title": "Advanced Algorithms",
      "course_code": "CS201",
      "description": "This course covers advanced algorithm design and analysis.",
      "year_of_delivery": 2024,
      "semester_of_delivery": 2
  }
  ```

#### **3. Retrieve Course Details**

- **Endpoint**: `/courses/{id}/`
- **Method**: `GET`
- **Description**: Retrieve detailed information about a specific course by its ID.
- **URL Parameters**:
  - `{id}`: The ID of the course.
- **Response Example**:

  ```json
  {
      "id": 1,
      "title": "Introduction to Programming",
      "course_code": "CS101",
      "description": "This course covers the basics of programming.",
      "year_of_delivery": 2024,
      "semester_of_delivery": 1
  }
  ```

#### **4. Delete a Course**

- **Endpoint**: `/courses/{id}/`
- **Method**: `DELETE`
- **Description**: Delete a course by its ID.
- **URL Parameters**:
  - `{id}`: The ID of the course.
- **Response**: 
  - Status: `204 No Content` (indicates successful deletion without any content returned)

### Course Instances (If applicable)

#### **1. Create a Course Instance**

- **Endpoint**: `/instances/`
- **Method**: `POST`
- **Description**: Create a new instance of course delivery.
- **Request Body Example**:

  ```json
  {
      "course_id": 1,
      "year_of_delivery": 2024,
      "semester_of_delivery": 1
  }
  ```

- **Response Example**:

  ```json
  {
      "id": 1,
      "course_id": 1,
      "year_of_delivery": 2024,
      "semester_of_delivery": 1
  }
  ```

#### **2. List Course Instances by Year and Semester**

- **Endpoint**: `/instances/{year}/{semester}/`
- **Method**: `GET`
- **Description**: Retrieve a list of course instances delivered in a specific year and semester.
- **URL Parameters**:
  - `{year}`: The year of course delivery.
  - `{semester}`: The semester of course delivery (1 or 2).
- **Response Example**:

  ```json
  [
      {
          "id": 1,
          "course_id": 1,
          "year_of_delivery": 2024,
          "semester_of_delivery": 1
      }
  ]
  ```

#### **3. Retrieve Course Instance Details**

- **Endpoint**: `/instances/{year}/{semester}/{id}/`
- **Method**: `GET`
- **Description**: Retrieve detailed information about a specific course instance by its ID.
- **URL Parameters**:
  - `{year}`: The year of course delivery.
  - `{semester}`: The semester of course delivery.
  - `{id}`: The ID of the course instance.
- **Response Example**:

  ```json
  {
      "id": 1,
      "course_id": 1,
      "year_of_delivery": 2024,
      "semester_of_delivery": 1
  }
  ```

#### **4. Delete a Course Instance**

- **Endpoint**: `/instances/{year}/{semester}/{id}/`
- **Method**: `DELETE`
- **Description**: Delete a course instance by its ID.
- **URL Parameters**:
  - `{year}`: The year of course delivery.
  - `{semester}`: The semester of course delivery.
  - `{id}`: The ID of the course instance.
- **Response**: 
  - Status: `204 No Content` (indicates successful deletion without any content returned)

## Error Handling

- **400 Bad Request**: This status is returned when the request is malformed or contains invalid data. Example:

  ```json
  {
      "error": "Course with this course code already exists."
  }
  ```

- **404 Not Found**: This status is returned when a requested resource (course or instance) is not found. Example:

  ```json
  {
      "error": "Course not found."
  }
  ```

## Summary

This API allows you to manage courses and their instances effectively. The endpoints support creating, retrieving, and deleting courses and course instances with full error handling.

---

You can expand on this documentation as needed, especially if you implement additional features or endpoints. It’s also a good idea to update the documentation whenever you make changes to the API. Let me know if you need any further help, babe!