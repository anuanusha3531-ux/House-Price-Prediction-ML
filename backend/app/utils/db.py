import sqlite3


# 🔹 CREATE TABLE (RUN ONCE AUTOMATICALLY)
def init_db():
    conn = sqlite3.connect("predictions.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predictions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            input_data TEXT,
            prediction INTEGER
        )
    """)

    conn.commit()
    conn.close()


# 🔹 SAVE PREDICTION
def save_prediction(input_data, prediction):
    conn = sqlite3.connect("predictions.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO predictions (input_data, prediction) VALUES (?, ?)",
        (str(input_data), int(prediction))
    )

    conn.commit()
    conn.close()


# 🔹 GET HISTORY
def get_all_predictions():
    conn = sqlite3.connect("predictions.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT input_data, prediction 
        FROM predictions 
        ORDER BY id DESC 
        LIMIT 10
    """)

    rows = cursor.fetchall()

    result = []
    for row in rows:
        result.append({
            "input": row[0],
            "prediction": row[1]
        })

    conn.close()
    return result