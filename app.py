from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DATABASE = 'jarvis-database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return "Jarvis is running!" \
    "<a href='/view/morning_journal'>View Morning Journal</a> | " \
    "<a href='/view/evening_journal'>View Evening Journal</a> | " \
    "<a href='/view/morning_log'>View Morning Log</a> | " \
    "<a href='/view/evening_log'>View Evening Log</a>"


@app.route('/morning_journal', methods=['GET', 'POST'])
def morning_journal():
    if request.method == 'POST':
        date = request.form['date']
        questions = request.form['questions']
        answers = request.form['answers']
        mood_score = int(request.form['mood_score'])
        gratitude = request.form['gratitude']
        reflection = request.form['reflection']
        todays_goals = request.form['todays_goals']
        sleep_performance = int(request.form['sleep_performance'])

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO morning_journal (date, questions, answers, mood_score, gratitude, reflection, todays_goals, sleep_performance)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (date, questions, answers, mood_score, gratitude, reflection, todays_goals, sleep_performance))
        conn.commit()
        conn.close()

        return redirect('/morning_journal')

    return render_template('morning_journal.html')

@app.route('/evening_journal', methods=['GET', 'POST'])
def evening_journal():
    if request.method == 'POST':
        date = request.form['date']
        questions = request.form['questions']
        answers = request.form['answers']
        mood_score = int(request.form['mood_score'])
        reflection = request.form['reflection']
        todays_goals_completed = request.form['todays_goals_completed']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO evening_journal (date, questions, answers, mood_score, reflection, todays_goals_completed)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (date, questions, answers, mood_score, reflection, todays_goals_completed))
        conn.commit()
        conn.close()

        return redirect('/evening_journal')

    return render_template('evening_journal.html')

@app.route('/morning_log', methods=['GET', 'POST'])
def morning_log():
    if request.method == 'POST':
        date = request.form['date']
        walk = int(request.form['walk'])
        vitamins = int(request.form['vitamins'])
        meditation = int(request.form['meditation'])
        reading = int(request.form['reading'])
        japanese = int(request.form['japanese'])
        coffee = int(request.form['coffee'])
        starting_work = int(request.form['starting_work'])

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO morning_log (date, walk, vitamins, meditation, reading, japanese, coffee, starting_work)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (date, walk, vitamins, meditation, reading, japanese, coffee, starting_work))
        conn.commit()
        conn.close()

        return redirect('/morning_log')

    return render_template('morning_log.html')

@app.route('/evening_log', methods=['GET', 'POST'])
def evening_log():
    if request.method == 'POST':
        date = request.form['date']
        good_diet = int(request.form['good_diet'])
        followed_training = int(request.form['followed_training'])
        deep_work_blocks_3 = int(request.form['deep_work_blocks_3'])
        brush_teeth = int(request.form['brush_teeth'])
        sleep_preparation = int(request.form['sleep_preparation'])

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO evening_log (date, good_diet, followed_training, deep_work_blocks_3, brush_teeth, sleep_preparation)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (date, good_diet, followed_training, deep_work_blocks_3, brush_teeth, sleep_preparation))
        conn.commit()
        conn.close()

        return redirect('/evening_log')

    return render_template('evening_log.html')


@app.route('/view/morning_journal')
def view_morning_journal():
    conn = get_db_connection()
    entries = conn.execute('SELECT * FROM morning_journal ORDER BY date DESC').fetchall()
    conn.close()
    return render_template('view_morning_journal.html', entries=entries)

@app.route('/view/evening_journal')
def view_evening_journal():
    conn = get_db_connection()
    entries = conn.execute('SELECT * FROM evening_journal ORDER BY date DESC').fetchall()
    conn.close()
    return render_template('view_evening_journal.html', entries=entries)

@app.route('/view/morning_log')
def view_morning_log():
    conn = get_db_connection()
    entries = conn.execute('SELECT * FROM morning_log ORDER BY date DESC').fetchall()
    conn.close()
    return render_template('view_morning_log.html', entries=entries)

@app.route('/view/evening_log')
def view_evening_log():
    conn = get_db_connection()
    entries = conn.execute('SELECT * FROM evening_log ORDER BY date DESC').fetchall()
    conn.close()
    return render_template('view_evening_log.html', entries=entries)

@app.route('/api/morning_journal', methods=['POST'])
def api_morning_journal():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO morning_journal (date, questions, answers, mood_score, gratitude, reflection, todays_goals, sleep_performance)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['date'], data['questions'], data['answers'],
        int(data['mood_score']), data['gratitude'], data['reflection'],
        data['todays_goals'], int(data['sleep_performance'])
    ))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"}), 201

@app.route('/api/evening_journal', methods=['POST'])
def api_evening_journal():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO evening_journal (date, questions, answers, mood_score, reflection, todays_goals_completed)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        data['date'], data['questions'], data['answers'],
        int(data['mood_score']), data['reflection'], data['todays_goals_completed']
    ))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"}), 201

@app.route('/api/morning_log', methods=['POST'])
def api_morning_log():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO morning_log (date, walk, vitamins, meditation, reading, japanese, coffee, starting_work)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['date'], int(data['walk']), int(data['vitamins']),
        int(data['meditation']), int(data['reading']), int(data['japanese']),
        int(data['coffee']), int(data['starting_work'])
    ))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"}), 201

@app.route('/api/evening_log', methods=['POST'])
def api_evening_log():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO evening_log (date, good_diet, followed_training, deep_work_blocks_3, brush_teeth, sleep_preparation)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        data['date'], int(data['good_diet']), int(data['followed_training']),
        int(data['deep_work_blocks_3']), int(data['brush_teeth']), int(data['sleep_preparation'])
    ))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"}), 201

from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
from datetime import datetime

app = Flask(__name__)
DATABASE = 'jarvis-database.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def index():
    return "Jarvis is running!" \
    "<a href='/view/morning_journal'>View Morning Journal</a> | " \
    "<a href='/view/evening_journal'>View Evening Journal</a> | " \
    "<a href='/view/morning_log'>View Morning Log</a> | " \
    "<a href='/view/evening_log'>View Evening Log</a>"


@app.route('/morning_journal', methods=['GET', 'POST'])
def morning_journal():
    if request.method == 'POST':
        date = request.form['date']
        questions = request.form['questions']
        answers = request.form['answers']
        mood_score = int(request.form['mood_score'])
        gratitude = request.form['gratitude']
        reflection = request.form['reflection']
        todays_goals = request.form['todays_goals']
        sleep_performance = int(request.form['sleep_performance'])

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO morning_journal (date, questions, answers, mood_score, gratitude, reflection, todays_goals, sleep_performance)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (date, questions, answers, mood_score, gratitude, reflection, todays_goals, sleep_performance))
        conn.commit()
        conn.close()

        return redirect('/morning_journal')

    return render_template('morning_journal.html')

@app.route('/evening_journal', methods=['GET', 'POST'])
def evening_journal():
    if request.method == 'POST':
        date = request.form['date']
        questions = request.form['questions']
        answers = request.form['answers']
        mood_score = int(request.form['mood_score'])
        reflection = request.form['reflection']
        todays_goals_completed = request.form['todays_goals_completed']

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO evening_journal (date, questions, answers, mood_score, reflection, todays_goals_completed)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (date, questions, answers, mood_score, reflection, todays_goals_completed))
        conn.commit()
        conn.close()

        return redirect('/evening_journal')

    return render_template('evening_journal.html')

@app.route('/morning_log', methods=['GET', 'POST'])
def morning_log():
    if request.method == 'POST':
        date = request.form['date']
        walk = int(request.form['walk'])
        vitamins = int(request.form['vitamins'])
        meditation = int(request.form['meditation'])
        reading = int(request.form['reading'])
        japanese = int(request.form['japanese'])
        coffee = int(request.form['coffee'])
        starting_work = int(request.form['starting_work'])

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO morning_log (date, walk, vitamins, meditation, reading, japanese, coffee, starting_work)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (date, walk, vitamins, meditation, reading, japanese, coffee, starting_work))
        conn.commit()
        conn.close()

        return redirect('/morning_log')

    return render_template('morning_log.html')

@app.route('/evening_log', methods=['GET', 'POST'])
def evening_log():
    if request.method == 'POST':
        date = request.form['date']
        good_diet = int(request.form['good_diet'])
        followed_training = int(request.form['followed_training'])
        deep_work_blocks_3 = int(request.form['deep_work_blocks_3'])
        brush_teeth = int(request.form['brush_teeth'])
        sleep_preparation = int(request.form['sleep_preparation'])

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO evening_log (date, good_diet, followed_training, deep_work_blocks_3, brush_teeth, sleep_preparation)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (date, good_diet, followed_training, deep_work_blocks_3, brush_teeth, sleep_preparation))
        conn.commit()
        conn.close()

        return redirect('/evening_log')

    return render_template('evening_log.html')


@app.route('/view/morning_journal')
def view_morning_journal():
    conn = get_db_connection()
    entries = conn.execute('SELECT * FROM morning_journal ORDER BY date DESC').fetchall()
    conn.close()
    return render_template('view_morning_journal.html', entries=entries)

@app.route('/view/evening_journal')
def view_evening_journal():
    conn = get_db_connection()
    entries = conn.execute('SELECT * FROM evening_journal ORDER BY date DESC').fetchall()
    conn.close()
    return render_template('view_evening_journal.html', entries=entries)

@app.route('/view/morning_log')
def view_morning_log():
    conn = get_db_connection()
    entries = conn.execute('SELECT * FROM morning_log ORDER BY date DESC').fetchall()
    conn.close()
    return render_template('view_morning_log.html', entries=entries)

@app.route('/view/evening_log')
def view_evening_log():
    conn = get_db_connection()
    entries = conn.execute('SELECT * FROM evening_log ORDER BY date DESC').fetchall()
    conn.close()
    return render_template('view_evening_log.html', entries=entries)

@app.route('/api/morning_journal', methods=['POST'])
def api_morning_journal():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO morning_journal (date, questions, answers, mood_score, gratitude, reflection, todays_goals, sleep_performance)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['date'], data['questions'], data['answers'],
        int(data['mood_score']), data['gratitude'], data['reflection'],
        data['todays_goals'], int(data['sleep_performance'])
    ))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"}), 201

@app.route('/api/evening_journal', methods=['POST'])
def api_evening_journal():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO evening_journal (date, questions, answers, mood_score, reflection, todays_goals_completed)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        data['date'], data['questions'], data['answers'],
        int(data['mood_score']), data['reflection'], data['todays_goals_completed']
    ))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"}), 201

@app.route('/api/morning_log', methods=['POST'])
def api_morning_log():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO morning_log (date, walk, vitamins, meditation, reading, japanese, coffee, starting_work)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        data['date'], int(data['walk']), int(data['vitamins']),
        int(data['meditation']), int(data['reading']), int(data['japanese']),
        int(data['coffee']), int(data['starting_work'])
    ))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"}), 201

@app.route('/api/evening_log', methods=['POST'])
def api_evening_log():
    data = request.get_json()
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO evening_log (date, good_diet, followed_training, deep_work_blocks_3, brush_teeth, sleep_preparation)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (
        data['date'], int(data['good_diet']), int(data['followed_training']),
        int(data['deep_work_blocks_3']), int(data['brush_teeth']), int(data['sleep_preparation'])
    ))
    conn.commit()
    conn.close()
    return jsonify({"status": "success"}), 201

@app.route('/api/morning_journal', methods=['GET'])
def get_morning_journal():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM morning_journal ORDER BY date DESC")
    entries = cursor.fetchall()
    conn.close()

    data = [dict(row) for row in entries]
    return jsonify(data)

@app.route('/api/evening_journal', methods=['GET'])
def get_evening_journal():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM evening_journal ORDER BY date DESC")
    entries = cursor.fetchall()
    conn.close()

    data = [dict(row) for row in entries]
    return jsonify(data)

@app.route('/api/morning_log', methods=['GET'])
def get_morning_log():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM morning_log ORDER BY date DESC")
    entries = cursor.fetchall()
    conn.close()

    data = [dict(row) for row in entries]
    return jsonify(data)

@app.route('/api/evening_log', methods=['GET'])
def get_evening_log():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM evening_log ORDER BY date DESC")
    entries = cursor.fetchall()
    conn.close()

    data = [dict(row) for row in entries]
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)