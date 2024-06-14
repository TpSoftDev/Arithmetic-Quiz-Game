import random 
import time

# Constants for the arithmetic quiz
OPERATORS = ["+", "-", "*"]  # List of operators to choose from
MIN_OPEAND = 3               # Minimum operand value
MAX_OPERAND = 12             # Maximum operand value
TOTAL_PROBLEMS = 10          # Total number of problems in the quiz

def generate_problem():
    """
    Generates a random arithmetic problem and computes the answer.
    
    Returns:
        expression (str): The arithmetic expression as a string.
        answer (int): The evaluated result of the arithmetic expression.
    """
    left = random.randint(MIN_OPEAND, MAX_OPERAND)  # Generate random left operand
    right = random.randint(MIN_OPEAND, MAX_OPERAND) # Generate random right operand
    operator = random.choice(OPERATORS)             # Randomly choose an operator
    
    expression = str(left) + " " + operator + " " + str(right)  # Create the arithmetic expression
    answer = eval(expression)  # Evaluate the expression to get the answer
    
    return expression, answer

# Initialize the count of wrong answers
wrong = 0

# Wait for user to start the quiz
input("Press enter to start!")
print("-----------------------")

# Record the start time
start_time = time.time()

# Loop through the total number of problems
for i in range(TOTAL_PROBLEMS):
    # Generate a problem
    expression, answer = generate_problem()
    
    # Continuously prompt the user until they provide the correct answer
    while True:
        guess = input(f"Problem #{i + 1}: {expression} = ")
        if guess == str(answer):
            break
        wrong += 1  # Increment wrong answer count if the guess is incorrect

# Record the end time
end_time = time.time()

# Calculate the total time taken to complete the quiz
total_time = round(end_time - start_time, 2)

print("-----------------------")
# Display the results
print(f"Nice work! You finished in {total_time} seconds and got {wrong} answers wrong!")
