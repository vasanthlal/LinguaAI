from app.database.base import Base
from app.database.connection import engine

# Import models so SQLAlchemy knows about them
import app.models  # noqa: F401

print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("All tables created successfully!")
