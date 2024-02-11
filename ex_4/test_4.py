import sqlite3

from flask import Flask, request

app = Flask(__name__)

@app.route('/search')
def search():
    product_name = request.args.get('product')

    query = f"SELECT * FROM products WHERE name = '{product_name}'"

    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()

    return str(results)

if __name__ == '__main__':
    app.run(debug=True)
