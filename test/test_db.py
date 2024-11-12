import unittest
from app import create_app, db
import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()
    
    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()
    
    def test_db_connection(self):
        conn = psycopg2.connect(dbname=os.getenv("DB_NAME"),
                        user=os.getenv("DB_USER"),
                        host=os.getenv("DB_HOST"),
                        password=os.getenv("DB_PASSWORD"),
                        port=os.getenv("DB_PORT"))
        self.assertTrue(conn)