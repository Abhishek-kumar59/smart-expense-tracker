from app.core.security import (
    hash_password,
    verify_password
)

password = "password123"

hashed = hash_password(password)

print("Hashed Password:", hashed)

print(
    "Correct Password:",
    verify_password(password, hashed)
)

print(
    "Wrong Password:",
    verify_password("wrong_password", hashed)
)