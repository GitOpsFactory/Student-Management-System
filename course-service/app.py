from flask import Flask,jsonify
import psycopg2

app=Flask(__name__)

@app.route("/courses")
def courses():

    conn=psycopg2.connect(
        host="postgres-service",
        database="school",
        user="admin",
        password="admin123"
    )

    cur=conn.cursor()
    cur.execute("select * from courses")

    return jsonify(cur.fetchall())

app.run(host="0.0.0.0",port=5002)