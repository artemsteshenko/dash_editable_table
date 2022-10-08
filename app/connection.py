import sqlite3


def create_connection():
  conn = sqlite3.connect(':memory:', check_same_thread=False)
  return conn


conn = create_connection()


