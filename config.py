import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://username:password@postgres:5432/testdb'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    REDIS_URL = 'redis://redis:6379/0'