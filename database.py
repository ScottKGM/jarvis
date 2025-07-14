import sqlite3

db = sqlite3.connect('jarvis-database.db')

def create_morning_journal_table():
    cursor = db.cursor()
    # mood_score = from 1-10
    # sleep_performance = score from Whoop 0-100
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS morning_journal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            questions TEXT NOT NULL,
            answers TEXT NOT NULL,
            mood_score INTEGER NOT NULL, 
            gratitude TEXT NOT NULL,
            reflection TEXT NOT NULL,
            todays_goals TEXT NOT NULL,
            sleep_performance INTEGER NOT NULL, 
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    db.commit()

def create_evening_journal_table():
    cursor = db.cursor()
    # mood_score = from 1-10
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS evening_journal (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            questions TEXT NOT NULL,
            answers TEXT NOT NULL,
            mood_score INTEGER NOT NULL,
            reflection TEXT NOT NULL,
            todays_goals_completed TEXT NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    db.commit()

def create_morning_log_table():
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS morning_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            walk INTEGER NOT NULL,
            vitamins INTEGER NOT NULL,
            meditation INTEGER NOT NULL,
            reading INTEGER NOT NULL,
            japanese INTEGER NOT NULL,
            coffee INTEGER NOT NULL,
            starting_work INTEGER NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    db.commit()

def create_evening_log_table():
    cursor = db.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS evening_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            good_diet INTEGER NOT NULL,
            followed_training INTEGER NOT NULL,
            deep_work_blocks_3 INTEGER NOT NULL,
            brush_teeth INTEGER NOT NULL,
            sleep_preparation INTEGER NOT NULL,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    db.commit()

# Create tables
create_morning_journal_table()
create_evening_journal_table()
create_morning_log_table()
create_evening_log_table()

db.close()
