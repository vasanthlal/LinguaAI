from app.database.base import Base
from app.database.connection import engine

# Import models so SQLAlchemy knows about them
from app.models.user import User

print("Creating database tables...")

Base.metadata.create_all(bind=engine)

print("All tables created successfully!")