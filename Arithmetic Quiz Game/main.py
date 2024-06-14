import random 
import time

OPERATORS = ["+", "-", "*"]
MIN_OPEAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
        left = random.randint(MIN_OPEAND,MAX_OPERAND)
        right = random.randint(MIN_OPEAND,MAX_OPERAND)
        operator = random.choice(OPERATORS)
        
        expression = str(left) + " " + operator +" " + str(right)
        #Evalute a String as if it was a python expression.
        answer = eval(expression)
        return expression , answer


wrong = 0
input("Press enter to start!")
print("-----------------------")

start_time = time.time()

        
for i in range (TOTAL_PROBLEMS):
        expression, answer = generate_problem()
        while True:
                guess = input(f"Problem #{str(i+1)} : {expression} = ")
                if guess == str(answer):
                        break
                wrong += 1
                
end_time = time.time()
total_time = round(end_time- start_time,2)

print("-----------------------")
print(f"Nice work ! You finshed in, {total_time} seconds and got {wrong} answers wrong !")       

         