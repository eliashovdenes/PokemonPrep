import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv('DATABASE_URL')

# SQL commands to create tables
create_users_table = """
CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL
);
"""

create_user_scores_table = """
CREATE TABLE IF NOT EXISTS user_scores (
    score_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    highest_streak INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE
);
"""

# New table for daily scores
create_user_daily_scores_table = """
CREATE TABLE IF NOT EXISTS user_daily_scores (
    daily_score_id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL,
    score_date DATE NOT NULL,
    daily_score INTEGER NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (user_id) ON DELETE CASCADE,
    UNIQUE (user_id, score_date)  -- Ensure one score per user per day
);
"""

def initialize_db():
    conn = psycopg2.connect(DATABASE_URL)
    cur = conn.cursor()
    # cur.execute(create_users_table)
    # cur.execute(create_user_scores_table)
    cur.execute(create_user_daily_scores_table)
    conn.commit()
    cur.close()
    conn.close()

if __name__ == "__main__":
    initialize_db()
    print("Database initialized successfully.")