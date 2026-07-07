from app.utils.security import hash_password, verify_password

password = "LinguaAI123"

hashed = hash_password(password)

print("Original :", password)
print("Hashed   :", hashed)

print("Verify :", verify_password(password, hashed))