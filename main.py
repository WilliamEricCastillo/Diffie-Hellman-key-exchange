# main.py

from diffie_hellman import DiffieHellman
from prime_generator import PrimeGenerator

if __name__ == '__main__':
    dh = DiffieHellman()
    prime_gen = PrimeGenerator()

    print("\nDiffie-Hellman Key Exchange")
    print("===========================")

    dh.perform_key_exchange()
    dh.display_results()
