# prime_generator.py

import sympy


class PrimeGenerator:
    @staticmethod
    def is_prime(number):
        return sympy.isprime(number)

    @staticmethod
    def get_prime_input(prompt):
        while True:
            try:
                prime = int(input(prompt).strip())
                if not PrimeGenerator.is_prime(prime):
                    print("ERROR: It is not a prime number!\n")
                else:
                    return prime
            except ValueError:
                print("ERROR: Invalid input! Please enter a valid prime number.\n")

    @staticmethod
    def get_valid_input(prompt, max_value):
        while True:
            try:
                value = int(input(prompt))
                if 0 <= value <= max_value:
                    return value
                else:
                    print(f"Input should be between 0 and {max_value}.\n")
            except ValueError:
                print("Please enter a valid number.\n")
