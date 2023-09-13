# diffie_hellman.py

import sys
import sympy


class DiffieHellman:
    def __init__(self):
        self.P = None
        self.G = None
        self.a = None
        self.b = None
        self.x = None
        self.y = None
        self.ka = None
        self.kb = None

    def generate_public_key(self, private_key):
        return pow(self.G, private_key, self.P)

    def generate_secret_key(self, public_key, private_key):
        return pow(public_key, private_key, self.P)

    def perform_key_exchange(self):
        self.P = self.get_prime_input("Enter a prime number for P: ")
        self.G = self.get_prime_input("Enter a prime number for G: ")

        if not self.primitive_root_check(self.P, self.G):
            print(f"{self.G} is not a primitive root of {self.P}.")
            sys.exit(1)

        self.a = self.get_valid_input("Enter a number for A (0 to P-1): ", self.P - 1)
        self.b = self.get_valid_input("Enter a number for B (0 to P-1): ", self.P - 1)

        self.x = self.generate_public_key(self.a)
        self.y = self.generate_public_key(self.b)

        self.ka = self.generate_secret_key(self.y, self.a)
        self.kb = self.generate_secret_key(self.x, self.b)

    @staticmethod
    def primitive_root_check(P, G):
        prim_root_list = []
        for i in range(2, P):
            mod_list = []
            for k in range(1, P):
                mod_num = pow(i, k) % P
                mod_list.append(mod_num)
            if len(set(mod_list)) == P - 1:
                prim_root_list.append(i)

        return G in prim_root_list

    @staticmethod
    def get_prime_input(prompt):
        while True:
            try:
                prime = int(input(prompt).strip())
                if not sympy.isprime(prime):
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

    def display_results(self):
        print("\nSecret Key Exchange Results")
        print("===========================")

        if self.ka == self.kb:
            print("Secret key for Alice:", self.ka)
            print("Secret key for Bob:", self.kb)
        else:
            print("Key exchange failed. Secret keys do not match.")
