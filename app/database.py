from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from .core.config import settings  # Assuming your config file is named config.py
from sqlalchemy.orm import sessionmaker

# DATABASE_URL = "postgresql://postgres:1289@db/fastapicore"
# Create the SQLAlchemy engine
engine = create_engine(settings.DATABASE_URL)
# engine = create_engine(DATABASE_URL)

print(f"DATABASE_URL: {settings.DATABASE_URL}")
print(engine)


# Create a base class for your database models
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    except:
        db.rollback()
        raise
    finally:
        db.close()
