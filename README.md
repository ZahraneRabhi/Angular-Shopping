# Angular-Flask Mock Server Integration
this guide will demonstrate the steps on how to setup and run the Angular front-end shopping app with a Flask mock server to simulate backend functionality for testing purposes.

# Prerequisites
Before running the project, ensure you have the following installed:

- Node.js and npm(Node Package Manager)/or Yarn
- Angular CLI
- Python (for Flask)

## Getting Started
Follow these steps to run the project:

1. Clone the repository:

   ```bash
   git clone https://github.com/ZahraneRabhi/Angular-Shopping.git
   ```

2. Install Angular dependencies:

   ```bash
   npm install
   ```

3. Start the Angular development server:
   ```bash
   ng serve
   ``` 

4. In a separate terminal, navigate to the mock-server directory:
   ```bash
   cd py-server
   ```

5. Install Flask dependencies (optional, if not already installed):

   ```bash
   pip install -r requirements.txt
   ```

6. IStart the Flask mock server:

   ```bash
   py mock.py
   ```
# Tips:
### It is a good practice to create a terminal for each specific task(I might be WRONG tho), the VsCode Terminals configuration below is my personal preference
- ***ANGULAR***: Angular development server
- ***CLI***: Angular command-line interface tool
- ***SERVER***: Javascript Or Python mock server for testing purposes
- ***GIT***: Version Control

# 

# Notes
- This project has similarities to a follow-along Angular course which i will add its reference later
- This projects uses a mock server developed in Flask to immitate an Api behaviours
- This project contains alot of unused Models, will be fixed/put-in-use at later stages

# ToDo
- Implement Login and Signup Forms

