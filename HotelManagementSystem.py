import tkinter as tk
from tkinter import messagebox
from tkinter import ttk
import sqlite3
from datetime import datetime, timedelta


# Function to create a new user in the database
def create_user():
    username = new_username.get()
    password = new_password.get()

    if username == '' or password == '':
        messagebox.showerror("Error", "Please fill in all fields")
        return

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

    conn.close()

    messagebox.showinfo("Success", "User created successfully")

    new_username.delete(0, tk.END)
    new_password.delete(0, tk.END)

# Function to validate login credentials
def login():
    username = login_username.get()
    password = login_password.get()

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        messagebox.showinfo("Success", "Login successful")
        login_username.delete(0, tk.END)
        login_password.delete(0, tk.END)

        # # Close the login window
        # login_window.destroy()
        #
        # # Open the Hotel Management Software window
        # open_hotel_management_window()
    else:
        messagebox.showerror("Error", "Invalid credentials")

# Create a new tkinter window for sign up
def create_signup_window():
    signup_window = tk.Toplevel(root)
    signup_window.title("Sign Up")

    global new_username, new_password

    new_username = tk.Entry(signup_window)
    new_password = tk.Entry(signup_window, show="*")

    tk.Label(signup_window, text="Username").pack(pady=(10,0))
    new_username.pack(pady=(0,10))

    tk.Label(signup_window, text="Password").pack(pady=(10,0))
    new_password.pack(pady=(0,10))

    signup_button = tk.Button(signup_window, text="Sign Up", command=create_user)
    signup_button.pack(pady=(10,0))

# Create a new tkinter window for login
def create_login_window():
    login_window = tk.Toplevel(root)
    login_window.title("Login")

    global login_username, login_password

    login_username = tk.Entry(login_window)
    login_password = tk.Entry(login_window, show="*")

    tk.Label(login_window, text="Username").pack(pady=(10,0))
    login_username.pack(pady=(0,10))

    tk.Label(login_window, text="Password").pack(pady=(10,0))
    login_password.pack(pady=(0,10))

    login_button = tk.Button(login_window, text="Login", command=login)
    login_button.pack(pady=(10,0))

# Function to create a new user in the database
def create_user():
    username = new_username.get()
    password = new_password.get()

    if username == '' or password == '':
        messagebox.showerror("Error", "Please fill in all fields")
        return

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, password))
    conn.commit()

    conn.close()

    messagebox.showinfo("Success", "User created successfully")

    new_username.delete(0, tk.END)
    new_password.delete(0, tk.END)

# Function to validate login credentials
def login():
    username = login_username.get()
    password = login_password.get()

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()

    conn.close()

    if user:
        messagebox.showinfo("Success", "Login successful")
        login_username.delete(0, tk.END)
        login_password.delete(0, tk.END)

        # # Close the login window
        # login_window.destroy()
        #
        # # Open the Hotel Management Software window
        # open_hotel_management_window()
    else:
        messagebox.showerror("Error", "Invalid credentials")

    def open_hotel_management_window():
        root.withdraw()  # Hide the login window

        # Create Hotel Management Software window
        hotel_root = tk.Tk()
        hotel_root.title("Hotel Management System")

        # Create an instance of the HotelManagementApp class
        hotel_app = HotelManagementApp(hotel_root)

        # Set the size of the window
        hotel_root.geometry("800x600")

        # Run the Hotel Management Software window
        hotel_root.mainloop()

    class HotelManagementApp:
        def __init__(self, root):
            self.root = root
            self.root.title("Hotel Management System")

            # Create a SQLite database connection
            self.conn = sqlite3.connect("hotel_database.db")
            self.cursor = self.conn.cursor()

            # Create tables if they don't exist
            self.create_tables()

            # Create the GUI
            self.create_gui()

        def create_tables(self):
            # Create Customers table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Customers (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    room_number INTEGER,
                    check_in_date TEXT,
                    check_out_date TEXT
                )
            ''')

            # Create Sales table
            self.cursor.execute('''
                CREATE TABLE IF NOT EXISTS Sales (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    item TEXT,
                    quantity INTEGER,
                    amount REAL,
                    date TEXT
                )
            ''')

        def create_gui(self):
            # Create notebook for tabs
            self.notebook = ttk.Notebook(self.root)

            # Tab for customer management
            self.customer_tab = ttk.Frame(self.notebook)
            self.notebook.add(self.customer_tab, text="Customer Management")

            # Tab for sales and inventory
            self.sales_tab = ttk.Frame(self.notebook)
            self.notebook.add(self.sales_tab, text="Sales & Inventory")

            # Populate tabs
            self.create_customer_tab()
            self.create_sales_tab()

            # Pack the notebook
            self.notebook.pack(expand=True, fill=tk.BOTH)

        def create_customer_tab(self):
            # Customer Management UI
            frame = ttk.LabelFrame(self.customer_tab, text="Customer Management")
            frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

            # Customer Treeview
            columns = ("ID", "Name", "Room Number", "Check-In Date", "Check-Out Date")
            self.customer_tree = ttk.Treeview(frame, columns=columns, show="headings")

            for col in columns:
                self.customer_tree.heading(col, text=col)
                self.customer_tree.column(col, width=100)

            self.customer_tree.grid(row=0, column=0, padx=10, pady=10)

            # Add customer entry widgets and labels
            self.name_entry = ttk.Entry(frame)
            self.room_number_entry = ttk.Entry(frame)
            self.check_in_date_entry = ttk.Entry(frame)
            self.check_out_date_entry = ttk.Entry(frame)

            ttk.Label(frame, text="Name:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
            self.name_entry.grid(row=1, column=1, padx=5, pady=5)

            ttk.Label(frame, text="Room Number:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
            self.room_number_entry.grid(row=2, column=1, padx=5, pady=5)

            ttk.Label(frame, text="Check-In Date:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
            self.check_in_date_entry.grid(row=3, column=1, padx=5, pady=5)

            ttk.Label(frame, text="Check-Out Date:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
            self.check_out_date_entry.grid(row=4, column=1, padx=5, pady=5)

            # Add customer button
            add_customer_button = ttk.Button(frame, text="Add Customer", command=self.add_customer)
            add_customer_button.grid(row=1, column=0, pady=10)

        def create_sales_tab(self):
            # Sales and Inventory UI
            frame = ttk.LabelFrame(self.sales_tab, text="Sales & Inventory")
            frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

            # Sales Treeview
            columns = ("ID", "Item", "Quantity", "Amount", "Date")
            self.sales_tree = ttk.Treeview(frame, columns=columns, show="headings")

            for col in columns:
                self.sales_tree.heading(col, text=col)
                self.sales_tree.column(col, width=100)

            self.sales_tree.grid(row=0, column=0, padx=10, pady=10)

            # Add sale entry widgets and labels
            self.item_entry = ttk.Entry(frame)
            self.quantity_entry = ttk.Entry(frame)
            self.amount_entry = ttk.Entry(frame)
            self.date_entry = ttk.Entry(frame)

            ttk.Label(frame, text="Item:").grid(row=1, column=0, padx=5, pady=5, sticky="e")
            self.item_entry.grid(row=1, column=1, padx=5, pady=5)

            ttk.Label(frame, text="Quantity:").grid(row=2, column=0, padx=5, pady=5, sticky="e")
            self.quantity_entry.grid(row=2, column=1, padx=5, pady=5)

            ttk.Label(frame, text="Amount:").grid(row=3, column=0, padx=5, pady=5, sticky="e")
            self.amount_entry.grid(row=3, column=1, padx=5, pady=5)

            ttk.Label(frame, text="Date:").grid(row=4, column=0, padx=5, pady=5, sticky="e")
            self.date_entry.grid(row=4, column=1, padx=5, pady=5)

            # Add sale button
            add_sale_button = ttk.Button(frame, text="Add Sale", command=self.add_sale)
            add_sale_button.grid(row=1, column=0, pady=10)

        def add_customer(self):
            # Dummy function to add a customer to the Customers table
            name = self.name_entry.get()
            room_number = int(self.room_number_entry.get())
            check_in_date = self.check_in_date_entry.get()
            check_out_date = self.check_out_date_entry.get()

            self.cursor.execute('''
                INSERT INTO Customers (name, room_number, check_in_date, check_out_date)
                VALUES (?, ?, ?, ?)
            ''', (name, room_number, check_in_date, check_out_date))

            self.conn.commit()

            self.update_customer_tree()

        def add_sale(self):
            # Add a sale to the Sales table
            item = self.item_entry.get()
            quantity = int(self.quantity_entry.get())
            amount = float(self.amount_entry.get())
            date = self.date_entry.get()

            self.cursor.execute('''
                INSERT INTO Sales (item, quantity, amount, date)
                VALUES (?, ?, ?, ?)
            ''', (item, quantity, amount, date))

            self.conn.commit()

            self.update_sales_tree()

        def update_customer_tree(self):
            # Update the Customer Treeview with data from the Customers table
            self.customer_tree.delete(*self.customer_tree.get_children())

            self.cursor.execute('SELECT * FROM Customers')
            customers = self.cursor.fetchall()

            for customer in customers:
                self.customer_tree.insert("", "end", values=customer)

        def update_sales_tree(self):
            # Update the Sales Treeview with data from the Sales table
            self.sales_tree.delete(*self.sales_tree.get_children())

            self.cursor.execute('SELECT * FROM Sales')
            sales = self.cursor.fetchall()

            for sale in sales:
                self.sales_tree.insert("", "end", values=sale)

    if __name__ == "__main__":
        hotel_root = tk.Tk()
        hotel_app = HotelManagementApp(hotel_root)
        hotel_root.geometry("800x600")
        hotel_root.mainloop()

# Main tkinter window
root = tk.Tk()
root.title("Login System")

# Create a SQLite database
conn = sqlite3.connect('users.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS users
                (id INTEGER PRIMARY KEY,
                username TEXT NOT NULL,
                password TEXT NOT NULL)''')

conn.commit()
conn.close()

# Create buttons for sign up and login
signup_button = tk.Button(root, text="Sign Up", command=create_signup_window)
signup_button.pack(pady=(50,10))

login_button = tk.Button(root, text="Login", command=create_login_window)
login_button.pack(pady=(10,50))

root.mainloop()
