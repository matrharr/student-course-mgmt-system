# Student & Course Management System

## What is this?
- This codebase is a RESTful web API to manage students and their courses. It is built on Django, Postgres and Docker.

## Getting Started
- Follow these simple steps to set up the Django server locally.
1. Clone the repo using `git clone https://github.com/matrharr/student-course-mgmt-system.git`.
2. `cd student-course-mgmt-system/student-course-mgmt-system`.
3. Run `docker-compose up` to setup the database and run the server.
4. Visit `localhost:8000/students` to see a list of all students (more endpoints listed below).

## Endpoint Documentation

### Courses
#### GET `/courses`
- Return a list of all courses.
#### GET `/courses/:course_id`
- Return a single course.
#### GET `/courses?title=:course_title`
- Return all courses that match searched title.
#### POST `/courses`
- Create a new course.
#### DELETE `/courses/:course_id`
- Remove a course.

### Students
#### GET `/students`
- Return a list of all students.
#### GET `/students/:student_id`
- Return a single student.
#### GET `/students?name=:student_name`
- Return all students that match searched name.
#### POST `/students`
- Create a new student.
#### DELETE `/student/:student_id`
- Remove a student.
