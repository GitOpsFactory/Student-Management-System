from flask import Flask,jsonify
import psycopg2

app=Flask(__name__)

@app.route("/students")
def students():

    conn=psycopg2.connect(
        host="postgres-service",
        database="school",
        user="admin",
        password="admin123"
    )

    cur=conn.cursor()
    cur.execute("select * from students")

    data=[]

    for row in cur.fetchall():
        data.append({
            "id":row[0],
            "name":row[1]
        })

    return jsonify(data)

app.run(host="0.0.0.0",port=5001)