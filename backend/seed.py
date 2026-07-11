from app.database.session import SessionLocal
from app.seeders.language_seeder import seed_languages


def run_seeders():
    db = SessionLocal()

    try:
        seed_languages(db)
        print("✅ Languages seeded successfully.")

    finally:
        db.close()


if __name__ == "__main__":
    run_seeders()