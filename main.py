""" https://www.youtube.com/@PythonCodeCampOrg """

import argon2

password = "MySecurePassword"

# Create a PasswordHasher object
ph = argon2.PasswordHasher()

# Hash the password using Argon2
hashed_password = ph.hash(password)

print("Hashed Password:", hashed_password)


# Authenticate the password

input_password = "MySecurePassword"

try:
    ph.verify(hashed_password, input_password)
    print("Password verified successfully!")
except argon2.exceptions.VerifyMismatchError:
    print("Password verification failed.")
