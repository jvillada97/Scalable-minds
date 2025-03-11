import os

class Config:
    SQLALCHEMY_DATABASE_URI = f"postgresql://{os.environ.get('POSTGRES_USER')}:{os.environ.get('POSTGRES_PASSWORD')}@{os.environ.get('POSTGRES_HOST')}:{os.environ.get('POSTGRES_PORT')}/{os.environ.get('POSTGRES_DB')}"