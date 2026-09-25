# AI Test Automation Project

A beginner-friendly QA automation project for testing an AI-style customer support chatbot built with Flask.

## Project Overview

This project demonstrates how automated testing can be used to identify and prevent common problems in AI-powered applications.

The chatbot provides answers to customer questions through a simple web interface and REST API.

The project focuses on:

- Functional API testing
- Negative testing
- Input validation
- AI hallucination prevention
- Prompt injection testing
- Regression testing
- HTML test reporting

## Technology Stack

- Python
- Flask
- Pytest
- pytest-html
- REST API
- HTML/CSS/JavaScript
- Git and GitHub
- GitHub Actions

## Project Structure

ai-test-project/
├── app.py
├── README.md
├── requirements.txt
├── report.html
├── templates/
│   └── index.html
├── tests/
│   └── test_api.py
├── .github/
│   └── workflows/
└── .gitignore

## Test Scenarios

The automated test suite currently contains 9 tests.

### Functional Tests

- Verify business hours response
- Verify opening-hours question
- Verify unknown questions
- Verify normal messages
- Verify case-insensitive input

### Validation Tests

- Verify missing message returns HTTP 400
- Verify empty request returns HTTP 400

### AI Safety Tests

- Verify the chatbot does not invent a warranty policy
- Verify the chatbot does not reveal confidential credentials when subjected to a prompt injection attempt

## Defects Found

During development, two intentional defects were introduced to demonstrate the testing process.

### 1. AI Hallucination

The chatbot originally responded to warranty questions with an unsupported claim:

Yes, all our products come with a 5-year warranty.

The automated test detected this behavior.

The application was then updated to provide a safe response when verified warranty information is unavailable.

### 2. Prompt Injection

The chatbot originally revealed a fake administrator password when given a prompt injection attempt.

The automated test detected the credential disclosure.

The application was then updated to refuse requests for confidential information or credentials.

## Test Results

The final regression test run produced:

9 passed
0 failed

An HTML test report is generated using pytest-html.

## How to Run the Project

### 1. Activate the virtual environment

source venv/bin/activate

### 2. Install dependencies

pip install -r requirements.txt

### 3. Start the Flask application

python app.py

The application runs locally at:

http://127.0.0.1:5000

### 4. Run the automated tests

Open another Terminal window and activate the virtual environment.

Then run:

PYTHONPATH=. pytest tests/test_api.py -v

### 5. Generate the HTML test report

PYTHONPATH=. pytest tests/test_api.py -v --html=report.html --self-contained-html

## QA Workflow

Application Development
        ↓
Test Case Creation
        ↓
Test Execution
        ↓
Defect Detection
        ↓
Defect Fix
        ↓
Regression Testing
        ↓
9/9 Tests Passed

## Future Improvements

Planned improvements include:

- UI automation using Selenium
- Additional negative test cases
- API response schema validation
- GitHub Actions CI/CD
- Cross-browser testing
- Additional AI safety test cases
- Test coverage reporting

## Author

Kavya P
