# Midterm_2024_IS218
Advanced Object-Oriented Calculator Project
Overview
This project is an educational example that demonstrates Object-Oriented Programming (OOP) principles, design patterns, and best practices in Python through the implementation of a calculator. The project includes a complete calculator with support for basic operations, advanced features like input validation, error handling, persistence (history saving/loading), and testing. It also uses several design patterns such as Singleton, Strategy, Observer, Factory, Command, and Memento.

Project Structure
The project is divided into several modules, each focusing on a specific aspect of the calculator. Below is an overview of the key files and directories in the project:

Directory Structure
calculator_project/
│
├── app/
│   ├── __init__.py                 # Marks the directory as a package
│   ├── calculator.py               # Main calculator logic
│   ├── calculator_config.py        # Configuration settings for the calculator
│   ├── input_validators.py         # Input validation logic
│   ├── exceptions.py               # Custom exception hierarchy
│   ├── history.py                  # Persistence: History saving/loading
│   └── logger.py                   # Logging setup
│
├── tests/                          # Unit tests for the project
│   ├── __init__.py                 # Marks the directory as a package
│   ├── test_calculator.py          # Tests for the main calculator logic
│   ├── test_input_validators.py    # Tests for input validation
│   ├── test_exceptions.py          # Tests for exceptions
│   └── test_history.py             # Tests for history persistence
│
├── requirements.txt                # Project dependencies
├── pytest.ini                      # Pytest configuration
└── README.md                       # Project documentation (this file)
Key Files and Their Purpose
app/calculator.py: Contains the core calculator logic, including methods for arithmetic operations (add, subtract, multiply, divide). This file also includes the integration of different design patterns, such as Strategy for operation handling.

app/calculator_config.py: Defines configuration settings, such as the maximum input value, for the calculator. It is used throughout the application for consistency in configuration.

app/input_validators.py: Responsible for validating input, ensuring that the user enters only valid numbers. It handles validation for integer and decimal numbers, as well as string-based inputs, with appropriate error handling.

app/exceptions.py: Custom exception hierarchy that defines various exceptions used throughout the calculator application. This allows for clear error messages and easier debugging.

app/history.py: Implements history saving and loading functionality, allowing users to persist their calculation history and load it back later.

app/logger.py: Configures a logging system for tracking errors, events, and application flow. Useful for debugging and monitoring the application.

tests/: Contains unit tests for the various components of the application. Each file corresponds to a specific module in the app and includes tests for functionality and edge cases.

requirements.txt: Lists the Python dependencies for the project. These libraries are required for the project to run correctly. You can install them using pip.

pytest.ini: Configuration file for pytest, specifying test paths, test patterns, logging level, and test markers.

README.md: This documentation file, providing an overview of the project, setup instructions, and usage guidelines.
Design Patterns Implemented
This project demonstrates the following design patterns:

Singleton: Ensures that certain objects, like the CalculatorConfig, are only instantiated once.
Strategy: Used for handling different calculation operations (addition, subtraction, etc.) in a flexible manner.
Observer: Used to track and log events that occur during calculations.
Factory: Used to instantiate different types of operations based on user input.
Command: Encapsulates requests as objects, allowing for parameterization and queuing of commands.
Memento: Saves the state of the calculator to allow for undo functionality or history tracking.

#Video
URL - https://youtu.be/_ZG0R2LI2Kg
