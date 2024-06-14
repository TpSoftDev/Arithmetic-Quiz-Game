# Arithmetic Quiz Game

This project is a simple arithmetic quiz game written in Python. It generates random arithmetic problems involving addition, subtraction, and multiplication. The player is prompted to solve these problems within a timed session, and the game keeps track of the number of incorrect answers.

## Features

- Randomly generates arithmetic problems using addition, subtraction, and multiplication.
- Allows the user to attempt each problem until the correct answer is given.
- Tracks the number of incorrect attempts.
- Records the total time taken to complete the quiz.

## Getting Started

### Prerequisites

- Python 3.x installed on your system.

### Running the Game

1. Clone the repository or download the script.
2. Open a terminal or command prompt.
3. Navigate to the directory where the script is located.
4. Run the script using the following command:
    ```sh
    python arithmetic_quiz_game.py
    ```
5. Follow the on-screen instructions to start the game.

### Example

When you run the script, you will see a prompt asking you to press enter to start the game. After pressing enter, you will be presented with arithmetic problems one by one. Enter your answer for each problem. The game will continue to prompt you until you provide the correct answer. Once all problems are solved, the game will display the total time taken and the number of incorrect attempts.

## Code Overview

### Constants

- `OPERATORS`: List of operators (`+`, `-`, `*`) used in the arithmetic problems.
- `MIN_OPEAND`: Minimum value for operands in the arithmetic problems.
- `MAX_OPERAND`: Maximum value for operands in the arithmetic problems.
- `TOTAL_PROBLEMS`: Total number of problems to be solved in the game.

### Functions

#### `generate_problem()`

Generates a random arithmetic problem and computes the answer.

**Returns:**

- `expression` (str): The arithmetic expression as a string.
- `answer` (int): The evaluated result of the arithmetic expression.

### Main Logic

1. The game waits for the user to press enter to start.
2. Records the start time.
3. Loops through the total number of problems:
    - Generates a problem using `generate_problem()`.
    - Prompts the user to solve the problem.
    - Continues to prompt until the correct answer is given.
    - Increments the count of incorrect attempts if the answer is wrong.
4. Records the end time.
5. Calculates the total time taken.
6. Displays the results, including the total time taken and the number of incorrect answers.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions or improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

If you have any questions or feedback, please feel free to contact the project maintainer.

