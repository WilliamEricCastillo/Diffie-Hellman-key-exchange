# Diffie-Hellman Key Exchange

This is a Python program to demonstrate the Diffie-Hellman key exchange protocol. <br>
It allows two parties, Alice and Bob, to securely exchange a shared secret key over an insecure communication channel.

## Techniques Used
- **Diffie-Hellman Key Exchange:** The application implements the core principles of the Diffie-Hellman key exchange protocol, which involves modular exponentiation and prime number operations to generate shared secret keys.
- **Prime Number Validation:** User input validation ensures that the chosen prime numbers (P and G) are indeed prime, a fundamental requirement for the security of the protocol.


- **Primitive Root Detection:** The application checks whether the chosen values of P and G result in a primitive root. Primitive roots are essential for ensuring the security of the Diffie-Hellman key exchange.
- **Modular Arithmetic:** Modular arithmetic is utilized throughout the protocol to prevent integer overflow and ensure efficient computation of keys.

## How to Use
Follow these steps to run the application:

1. Clone the repository:
   ```bash
   https://github.com/WilliamEricCastillo/Diffie-Hellman-key-exchange.git

2. Ensure you have Python installed on your system. This application was developed using Python 3.
3. Run the `main.py` script to initiate the Diffie-Hellman key exchange.
   ``` bash
   python main.py

4. Follow the on-screen prompts to input prime numbers (P and G) and private numbers (A and B) for Alice and Bob.

5. The application will calculate and display the secret keys for both Alice and Bob, which should match.

6. If the secret keys match, the key exchange is successful. If they don't match, there is an issue with the inputs or calculations.

## Requirements
- Python 3 or higher
- SymPy library (for prime number checks)


## Contributors
- William Castillo
