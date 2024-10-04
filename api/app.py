from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)


def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="microservices_db",
        user="postgres",
        password="password",
    )
    return conn


@app.route("/contacts", methods=["GET"])
def contacts():
    conn = get_db_connection()
    cur = conn.cursor()

    limit = request.args.get("limit", default=10, type=int)

    # Get a random sample of contacts
    cur.execute(
        "SELECT name, address, email, phone, date_of_birth FROM contacts ORDER BY RANDOM() LIMIT %s;",
        (limit,),
    )
    rows = cur.fetchall()

    cur.close()
    conn.close()

    contacts_list = []
    for row in rows:
        contacts_list.append(
            {
                "name": row[0],
                "address": row[1],
                "email": row[2],
                "phone": row[3],
                "date_of_birth": row[4].strftime("%Y-%m-%d"),
            }
        )

    return jsonify(contacts_list)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
