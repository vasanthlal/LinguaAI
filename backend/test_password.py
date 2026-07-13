from app.database.session import SessionLocal
from app.repositories.user_repository import get_user_by_email
from app.utils.security import verify_password

db = SessionLocal()

user = get_user_by_email(
    db,
    "vasanth@test.com",
)

print(user.password_hash)

print(
    verify_password(
        "Password@123",
        user.password_hash,
    )
)

db.close()
