# Midterm_2024_IS218
Calculator Project Roadmap
This roadmap breaks down the functionality of the calculator project, focusing on the main components: operation classes, the factory pattern, REPL (Read-Eval-Print Loop) for user input, and logging.

1. Operation Classes
The Operation class hierarchy represents various calculator operations (addition, subtraction, etc.). It uses an abstract base class (ABC) to ensure each operation has a consistent interface (execute method).

Classes Overview
Operation (Abstract Base Class):
Methods:
execute(a, b): Abstract method all operations implement.
validate_operands(a, b): Validates the operands before the operation (each subclass customizes as needed).
__str__(): Returns the operation name, helping in error messages and logging.
Concrete Operation Classes:
Each of these classes (Addition, Subtraction, Multiplication, Division, Power, Root) implements execute to perform a specific operation.
Example: Addition.execute(a, b) returns a + b, while Division includes a validation to prevent division by zero.
Validation Handling
Subclasses like Division and Root override validate_operands to handle special cases, such as division by zero or taking a root of a negative number.
2. Factory Pattern with OperationFactory
OperationFactory simplifies the creation of Operation instances and centralizes the mapping of command names to operation classes.

Key Methods
_operations dictionary: Stores mappings from command names (e.g., 'add') to classes (Addition).
register_operation(name, operation_class): Allows adding new operations dynamically, ensuring flexibility.
create_operation(operation_type): Looks up the operation_type in _operations and returns the corresponding operation instance.
This pattern enables users to easily add or modify operations without altering core code.

3. REPL (Read-Eval-Print Loop)
The REPL handles user interaction, accepting commands in the format:

plaintext
Copy code
add 3 4
REPL Process
Command Parsing: Splits the input into command and operands.
Factory Use: Uses OperationFactory.create_operation to get the appropriate operation instance.
Execution and Output: Calls execute with the operands, returning the result or displaying error messages.
Help Command: Lists available commands.
Example REPL Workflow:

User types: add 3 4
REPL splits input into command = 'add' and args = [3, 4].
OperationFactory.create_operation('add') returns an Addition instance.
Addition.execute(3, 4) is called, returning 7.
Result (7) is displayed.
4. Logging Configuration
The logging configuration ensures that actions and errors are logged to both a file and the console. This uses a RotatingFileHandler to manage file size.

Logging Components
Handlers: fileHandler writes logs to logs/app.log, and consoleHandler outputs to the console.
Formatter: Defines the log format to include timestamp, logger name, log level, and message.
Logging Levels: Set to INFO, so only info and error messages are logged.
5. Error Handling
The project uses ValidationError exceptions to catch invalid operations (e.g., division by zero, negative roots).

Validation Checks: Before each operation, validate_operands checks for conditions like zero in division.
Error Messages: The REPL catches these exceptions and displays user-friendly error messages.
Putting It All Together
Example Workflow
Here's a breakdown of a typical interaction with the calculator:

User Input: The user types multiply 6 7 in the REPL.
Parsing: The REPL splits this input:
command = 'multiply'
args = ['6', '7']
Operation Creation:
Calls OperationFactory.create_operation('multiply'), which returns a Multiplication instance.
Execution:
Multiplication.execute(Decimal('6'), Decimal('7')) is called, resulting in 42.
Result Display: The result 42 is displayed to the user.
Adding a New Operation
To add a new operation (e.g., Modulus):

Define a Modulus class that inherits from Operation and implements execute for the modulus operation.
Register the operation in OperationFactory:
python
Copy code
OperationFactory.register_operation('mod', Modulus)
Users can now use mod a b in the REPL.

Video
URL - https://youtu.be/_ZG0R2LI2Kg
