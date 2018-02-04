import sqlite3

conn = sqlite3.connect('games.sqlite')
cursor = conn.cursor()


def update_db(score: int, player: str):
    if player != "":
        cursor.execute("INSERT  INTO gameResults ( Score,Player) VALUES ('%d', '%s')" % (score, player))
        conn.commit()
        rows = cursor.execute("SELECT * FROM gameResults ORDER BY Score DESC").fetchall()
        print("score..player")
        for row in rows:
            print(row)
