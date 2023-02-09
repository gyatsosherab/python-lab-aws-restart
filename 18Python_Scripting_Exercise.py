"""
Challenge Lab: Python Scripting Exercise
"""

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

prime_numbers = []
for num in range(1, 126):
    if is_prime(num):
        prime_numbers.append(num)

print(prime_numbers)

with open("record.txt", "w") as file:
    for prime in prime_numbers:
        file.write(str(prime) + "\n")



# Open the file in write mode
with open("output.txt", "w") as file:
    # Write the string to the file 
    file.write("This is the output of my program")