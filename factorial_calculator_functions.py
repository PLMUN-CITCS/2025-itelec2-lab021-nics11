# ESPINO, NICHAELA
# ITELECT2
# Laboratory #21 - Guided Coding Exercise:
# Variables, Literals, and Case-Sensitivity in Python 

def get_non_negative_integer() -> int:
    while True:
        try:
            n = int(input("Enter a non-negative integer: "))
            if n < 0:
                print("Please enter a non-integer.")
            else:
                return n
        except ValueError:
            print("Invalid input. Please enter a valid non-negative integer.")
def calculate_factorial(n: int) -> int:
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result
def main():
    num = get_non_negative_integer()
    fact = calculate_factorial(num)
    print(f"The factorial of {num} is: {fact}")
if __name__ == "__main__":
    main()
