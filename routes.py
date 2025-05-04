from flask import Blueprint, render_template, request, redirect
import sqlite3

main = Blueprint('main', __name__)

@main.route('/')
def dashboard():
    with sqlite3.connect('database.db') as conn:
        total_customers = conn.execute('SELECT COUNT(*) FROM customers').fetchone()[0]
        total_sales = conn.execute('SELECT COUNT(*) FROM sales').fetchone()[0]
    return render_template('dashboard.html', total_customers=total_customers, total_sales=total_sales)

@main.route('/customers', methods=['GET', 'POST'])
def customers():
    with sqlite3.connect('database.db') as conn:
        if request.method == 'POST':
            conn.execute('INSERT INTO customers (name) VALUES (?)', (request.form['name'],))
            conn.commit()
        customers = conn.execute('SELECT * FROM customers').fetchall()
    return render_template('customers.html', customers=customers)

@main.route('/delete_customer/<int:id>')
def delete_customer(id):
    with sqlite3.connect('database.db') as conn:
        conn.execute('DELETE FROM customers WHERE id = ?', (id,))
        conn.commit()
    return redirect('/customers')

@main.route('/sales', methods=['GET', 'POST'])
def sales():
    with sqlite3.connect('database.db') as conn:
        if request.method == 'POST':
            conn.execute('INSERT INTO sales (item, amount) VALUES (?, ?)', (request.form['item'], request.form['amount']))
            conn.commit()
        sales = conn.execute('SELECT * FROM sales').fetchall()
    return render_template('sales.html', sales=sales)

@main.route('/delete_sale/<int:id>')
def delete_sale(id):
    with sqlite3.connect('database.db') as conn:
        conn.execute('DELETE FROM sales WHERE id = ?', (id,))
        conn.commit()
    return redirect('/sales')