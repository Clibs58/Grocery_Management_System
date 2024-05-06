import mysql.connector
from datetime import datetime

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
)
cursor = conn.cursor()

def create_database():
    cursor.execute("CREATE DATABASE IF NOT EXISTS grocery_management")
    cursor.execute("USE grocery_management")

def create_grocery_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS grocery (g_id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255) UNIQUE, category VARCHAR(30), price INT, quantity INT DEFAULT 0)")
    items = (
        ("Apple", "food", 52, 0),
        ("Banana", "food", 89, 0),
        ("Chicken Breast", "food", 165, 0),
        ("Egg", "food", 70, 0),
        ("Salmon", "food", 208, 0),
        ("Pasta", "food", 131, 0),
        ("Rice", "food", 130, 0),
        ("Broccoli", "food", 3, 0),
        ("Orange", "fruit", 45, 0),
        ("Milk", "dairy", 25, 0),
        ("Bread", "bakery", 15, 0),
        ("Cheese", "dairy", 50, 0),
        ("Tomato", "vegetable", 30, 0),
        ("Cucumber", "vegetable", 20, 0),
        ("Butter", "dairy", 35, 0),
        ("Carrot", "vegetable", 18, 0),
        ("Yogurt", "dairy", 40, 0),
        ("Coffee", "beverage", 60, 0),
        ("Spinach", "vegetable", 25, 0),
        ("Chicken Thighs", "meat", 70, 0),
        ("Applesauce", "canned goods", 15, 0),
        ("Peanut Butter", "spread", 40, 0),
        ("Cereal", "breakfast", 30, 0),
        ("Olive Oil", "cooking", 50, 0),
        ("Honey", "sweetener", 35, 0),
        ("Quinoa", "grains", 45, 0),
        ("Almonds", "snack", 55, 0),
        ("Hummus", "dip", 30, 0),
        ("Eggs", "dairy", 28, 0),
        ("Salmon", "seafood", 90, 0),
        ("Pasta", "grains", 18, 0),
        ("Rice", "grains", 22, 0),
        ("Broccoli", "vegetable", 25, 0),
        ("Lettuce", "vegetable", 15, 0),
        ("Ground Beef", "meat", 65, 0),
        ("Avocado", "fruit", 60, 0),
        ("Strawberries", "fruit", 40, 0),
        ("Green Beans", "vegetable", 30, 0),
        ("Greek Yogurt", "dairy", 50, 0),
        ("Cheddar Cheese", "dairy", 55, 0),
        ("Onion", "vegetable", 12, 0),
        ("Garlic", "vegetable", 8, 0),
        ("Pepper", "vegetable", 15, 0),
        ("Mushrooms", "vegetable", 28, 0),
        ("Soy Milk", "dairy", 30, 0),
        ("Cottage Cheese", "dairy", 38, 0),
        ("Blueberries", "fruit", 45, 0),
        ("Bacon", "meat", 50, 0),
        ("Sausages", "meat", 42, 0),
        ("Tofu", "protein", 20, 0),
        ("Shrimp", "seafood", 75, 0),
        ("Salsa", "condiment", 18, 0),
        ("Lemon", "fruit", 12, 0),
        ("Lime", "fruit", 10, 0),
        ("Coconut Milk", "canned goods", 28, 0),
        ("Pineapple", "fruit", 30, 0),
        ("Peaches", "fruit", 35, 0),
        ("Raspberries", "fruit", 48, 0),
        ("Cucumber", "vegetable", 18, 0),
        ("Cantaloupe", "fruit", 25, 0),
        ("Watermelon", "fruit", 20, 0),
        ("Kiwi", "fruit", 22, 0),
        ("Grapes", "fruit", 28, 0),
        ("Zucchini", "vegetable", 16, 0),
        ("Artichoke", "vegetable", 40, 0),
        ("Cauliflower", "vegetable", 25, 0),
        ("Celery", "vegetable", 12, 0),
        ("Pomegranate", "fruit", 55, 0),
        ("Asparagus", "vegetable", 30, 0),
        ("Bell Pepper", "vegetable", 20, 0),
        ("Pumpkin", "vegetable", 18, 0),
        ("Sour Cream", "dairy", 30, 0),
        ("Cream Cheese", "dairy", 40, 0),
        ("Pears", "fruit", 38, 0),
        ("Plums", "fruit", 32, 0),
        ("Apricots", "fruit", 28, 0),
        ("Cherries", "fruit", 50, 0),
        ("Radishes", "vegetable", 15, 0),
        ("Cabbage", "vegetable", 20, 0),
        ("Cilantro", "herb", 8, 0),
        ("Thyme", "herb", 10, 0),
        ("Basil", "herb", 12, 0),
        ("Rosemary", "herb", 15, 0),
        ("Oregano", "herb", 10, 0),
        ("Sage", "herb", 12, 0),
        ("Parsley", "herb", 8, 0),
        ("Dill", "herb", 10, 0),
        ("Mint", "herb", 10, 0),
        ("Coriander", "herb", 8, 0),
        ("Nutmeg", "spice", 12, 0),
        ("Cinnamon", "spice", 10, 0),
        ("Cumin", "spice", 8, 0),
        ("Turmeric", "spice", 10, 0),
        ("Paprika", "spice", 10, 0),
        ("Chili Powder", "spice", 10, 0)
    )
    cursor.executemany("INSERT IGNORE INTO grocery (name, category, price, quantity) VALUES (%s, %s, %s, %s)", items)
    

def create_user_list_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS user_list (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255) UNIQUE, password VARCHAR(255))")

def create_month_table(month):
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {month} (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), item VARCHAR(255), category VARCHAR(30), price varchar(20), quantity INT DEFAULT 1, time_consumed DATETIME DEFAULT CURRENT_TIMESTAMP)")

def create_count_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS count (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), timestamp DATETIME)")
def create_feedback_table():
    cursor.execute("CREATE TABLE IF NOT EXISTS feedback (id INT AUTO_INCREMENT PRIMARY KEY, username VARCHAR(255), comment TEXT, time_posted DATETIME DEFAULT CURRENT_TIMESTAMP)")
def admin_sign_in():
    admin_username = "admin"
    admin_password = "admin123"
    entered_username = input("Enter admin username: ")
    entered_password = input("Enter admin password: ")
    if entered_username == admin_username and entered_password == admin_password:
        return True
    else:
        print("Invalid admin credentials.")
        return False
def suggest_items_based_on_history(username, current_month, cursor):
 
    history_query = f"SELECT item FROM {current_month} WHERE username = '{username}' GROUP BY item ORDER BY COUNT(item) DESC LIMIT 5"
    cursor.execute(history_query)
    suggested_items = cursor.fetchall()

    if suggested_items:
        print("\nSuggested Items based on Your Purchase History:")
        for item in suggested_items:
            print(item[0])
    else:
        print("No suggested items at the moment.")
def search_by_category():
    category = input("Enter the category to search for: ")
    search_query = f"SELECT * FROM grocery WHERE category = '{category}'"
    cursor.execute(search_query)
    results = cursor.fetchall()

    if results:
        print(f"\nItems in the category '{category}':")
        for result in results:
            print(f"ID: {result[0]}, Name: {result[1]}, Category: {result[2]}, Price: {result[3]}")
    else:
        print(f"No items found in the category '{category}'.")

def post_feedback(username, comment):
    feedback_query = "INSERT INTO feedback (username, comment) VALUES (%s, %s)"
    cursor.execute(feedback_query, (username, comment))
    conn.commit()

def view_feedbacks():
    view_feedbacks_query = "SELECT username, comment, time_posted FROM feedback ORDER BY time_posted DESC"
    cursor.execute(view_feedbacks_query)
    feedbacks = cursor.fetchall()

    if feedbacks:
        print("\nUser Feedbacks:")
        for feedback in feedbacks:
            print(f"Username: {feedback[0]}, Comment: {feedback[1]}, Time Posted: {feedback[2]}")
    else:
        print("No feedbacks available.")
def generate_billing_system(username, cursor, conn):
    current_month = datetime.now().strftime("%B_%Y")
    create_month_table(current_month)

    print("Billing System Options:")
    print("1. Generate Bill for Today")
    print("2. Generate Bill for a Specific Date")
    print("3. Exit")

    billing_option = int(input("Enter option: "))

    if billing_option == 1:
        today = datetime.now().strftime("%Y-%m-%d")
        generate_bill(username, current_month, today, cursor, conn)

    elif billing_option == 2:
        date = input("Enter date (YYYY-MM-DD): ")
        generate_bill(username, current_month, date, cursor, conn)

    elif billing_option == 3:
        print("Exiting Billing System.")
        main(cursor, conn)  # Pass cursor and conn to main

    else:
        print("Invalid option.")

def generate_bill(username, current_month, date, cursor, conn):
    try:
        datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Please use YYYY-MM-DD.")
        return

    bill_query = f"SELECT item, price, quantity FROM {current_month} WHERE DATE(time_consumed) = '{date}' and username = '{username}'"
    cursor.execute(bill_query)
    records = cursor.fetchall()

    if records:
        total_price = 0
        print(f"\nBill for {date}:")
        for record in records:
            item, price, quantity = record[0], record[1], record[2]
            if price is not None and quantity is not None:
                try:
                    total_price += int(price) * int(quantity)
                    print(f"Item: {item}, Price: {price}, Quantity: {quantity}")
                except ValueError:
                    print(f"Item: {item}, Price or Quantity is not a valid integer.")
                    print(f"Record causing the issue: {record}")
            else:
                print(f"Item: {item}, Price or Quantity is None.")
        print(f"\nTotal Price: {total_price}")
    else:
        print(f"No records found for {date}")
    

def admin_report():
    print("Admin Report Options:")
    print("1. Date")
    print("2. Month")
    print("3. Year")
    admin_option = int(input("Enter option: "))
    current_month = datetime.now().strftime("%B_%Y")
    create_month_table(current_month)    
    if admin_option == 1:
        date = input("Enter date (YYYY-MM-DD): ")
        report_query = f"SELECT count(distinct username) FROM {current_month} WHERE DATE(time_consumed) = '{date}'"
        cursor.execute(report_query)
        records = cursor.fetchall()
        print(f"User active on {date} are {records[0][0]}")
    elif admin_option == 2:
        month = input("Enter month (MM-YYYY): ")
        report_query = f"SELECT count(distinct username) FROM {current_month} WHERE DATE_FORMAT(time_consumed, '%m-%Y') = '{month}'"
        cursor.execute(report_query)
        records = cursor.fetchall()
        print(f"User active in month {month} are {records[0][0]}")
    elif admin_option == 3:
        year = input("Enter year (YYYY): ")
        report_query = f"SELECT count(distinct username) FROM {current_month} WHERE YEAR(time_consumed) = '{year}'"
        cursor.execute(report_query)
        records = cursor.fetchall()
        print(f"User active in year {year} are {records[0][0]}")

def main(cursor, conn):
    create_database()
    create_grocery_table()
    create_user_list_table()
    create_count_table()
    create_feedback_table()

    print("Welcome to the Grocery management!")
    print("1. Sign In")
    print("2. Sign Up")
    print("3. Admin Sign In")

    user_option = int(input("Enter option: "))

    if user_option == 1:
        username = input("Enter your username: ")
        password = input("Enter your password: ")
        sign_in_query = f"SELECT * FROM user_list WHERE username = '{username}' AND password = '{password}'"
        cursor.execute(sign_in_query)
        user = cursor.fetchone()
        if user:
            print("Sign In Successful!")
            current_month = datetime.now().strftime("%B_%Y")
            create_month_table(current_month)
            while True:
                print("1. Add item")
                print("2. Update a record")
                print("3. Delete a record")
                print("4. Generate a Bill")
                print("5. Log Out")
                print("6. See Reports")
                print("7. Provide Feedback")
                print("8. Search by Category")
                print("9. Preferred Items")
    

                user_choice = int(input("Enter your choice: "))

                if user_choice == 1:
                    
                    mydb=mysql.connector.connect(host='localhost',username='root',passwd='root',database='grocery_management')
                    mycursor=mydb.cursor()
                    mycursor.execute("select * from grocery")
                    results=mycursor.fetchall()
                    print("\t Items available in store:")
                    for result in results:
                        print("{}, price={}".format(result[1],result[3]))
                                          
                    item_name = input("\n Enter item name: ")
                    check_item_query = f"SELECT * FROM grocery WHERE name = '{item_name}'"
                    cursor.execute(check_item_query)
                    item = cursor.fetchone()
                    
                    
                    if item:
                        quantity=int(input(" Enter Quantity: "))
                        price = item[3]
                        category=item[2]
                        time_consumed = input("Enter the time consumed (YYYY-MM-DD HH:MM:SS): ")
                        add_item_query = f"INSERT INTO {current_month} (username, item, price, category, time_consumed, quantity) VALUES (%s, %s, %s, %s, %s, %s)"
                        cursor.execute(add_item_query, (username, item_name, price, category, time_consumed, quantity))
                        conn.commit()
                        print("Item added successfully!")
                    else:
                        print("Invalid  item.")
                elif user_choice ==9:
                    suggest_items_based_on_history(username, current_month, cursor)

                elif user_choice == 2:
                    print("Update Record:")
                    view_records_query = f"SELECT id, item, price, category, time_consumed FROM {current_month} WHERE username = '{username}'"
                    cursor.execute(view_records_query)
                    records = cursor.fetchall()

                    if records:
                        print("Existing Records:")
                        for record in records:
                            print(f"ID: {record[0]}, Item: {record[1]}, price: {record[2]}, category:{record[3]} time_consumed {record[4]}")

                        record_id = int(input("Enter the ID of the record you want to update: "))
                        new_item_name = input("Enter new item name : ")
                        new_price = (input("Enter new price : "))
                        new_category=(input("Enter New Category: "))
                        new_time_consumed = input("Enter new time consumed (YYYY-MM-DD HH:MM:SS): ")
                        new_quantity=int(input("Enter New Quantity: "))

                        update_query = f"UPDATE {current_month} SET item = COALESCE(%s, item), price = COALESCE(%s, price), category = COALESCE(%s, category), time_consumed = COALESCE(%s, time_consumed), quantity = COALESCE(%s, quantity) WHERE id = %s AND username = '{username}'"
                        cursor.execute(update_query, (new_item_name, new_price, new_category, new_time_consumed, new_quantity, record_id))
                        conn.commit()
                        print("Record updated successfully!")

                    else:
                        print("No records found to update.")

                elif user_choice == 3:
                    print("Delete Record:")
                    view_records_query = f"SELECT id, item, price, category, time_consumed FROM {current_month} WHERE username = '{username}'"
                    cursor.execute(view_records_query)
                    records = cursor.fetchall()

                    if records:
                        print("Existing Records:")
                        for record in records:
                            print(f"ID: {record[0]}, item: {record[1]}, price: {record[2]}, category{record[3]}, time_consumed: {record[4]}")

                        record_id = int(input("Enter the ID of the record you want to delete: "))
                        delete_query = f"DELETE FROM {current_month} WHERE id = %s AND username = '{username}'"
                        cursor.execute(delete_query, (record_id,))
                        conn.commit()
                        print("Record deleted successfully!")

                    else:
                        print("No records found to delete.")

                elif user_choice == 5:
                    print("Logging out...")
                    main(cursor, conn)
                elif user_choice == 4:
                    generate_billing_system(username, cursor, conn)
                elif user_choice == 7:
                    comment = input("Enter your feedback/comment: ")
                    post_feedback(username, comment)
                    print("Thank you for your feedback!")
                elif user_choice == 8:
                    search_by_category()
                elif user_choice == 6:
                    print("Reports Options:")
                    print("1. Date")
                    print("2. Month")
                    print("3. Year")
                    report_option = int(input("Enter option: "))
                    if report_option == 1:
                        date = input("Enter date (YYYY-MM-DD): ")
                        report_query = f"SELECT item, price, category, time_consumed FROM {current_month} WHERE DATE(time_consumed) = '{date}' and username = '{username}'"
                        cursor.execute(report_query)
                        records = cursor.fetchall()
                        if records:
                            print(f" items consumed on {date}:")
                            for record in records:
                                print(f"item: {record[0]}, price: {record[1]}, category: {record[2]}, time_consumed{record[3]}")
                        else:
                            print(f"No records found for {date}")

                    elif report_option == 2:
                        month = input("Enter month (MM-YYYY): ")
                        report_query = f"SELECT item, price, time_consumed FROM {current_month} WHERE DATE_FORMAT(time_consumed, '%m-%Y') = '{month}' and username = '{username}'"
                        cursor.execute(report_query)
                        records = cursor.fetchall()
                        if records:
                            print(f" items consumed in {month}:")
                            for record in records:
                                print(f"item: {record[0]}, price: {record[1]}, time_consumed:{record[2]}")
                        else:
                            print(f"No records found for {month}")

                    elif report_option == 3:
                        year = input("Enter year (YYYY): ")
                        report_query = f"SELECT item, price, time_consumed FROM {current_month} WHERE YEAR(time_consumed) = '{year}' and username = '{username}'"
                        cursor.execute(report_query)
                        records = cursor.fetchall()
                        if records:
                            print(f" items consumed in {year}:")
                            for record in records:
                                print(f"item: {record[0]}, price: {record[1]}, time_consumed:{record[2]}")
                        else:
                            print(f"No records found for {year}")

                    else:
                        print("Invalid option.")

                else:
                    print("Invalid choice.")

        else:
            print("Invalid username or password.")

    elif user_option == 2:
        new_username = input("Enter a new username: ")
        new_password = input("Enter a new password: ")
        sign_up_query = f"INSERT INTO user_list (username, password) VALUES (%s, %s)"
        try:
            cursor.execute(sign_up_query, (new_username, new_password))
            conn.commit()
            print("Sign up successful!")
            main(cursor, conn)

        except mysql.connector.IntegrityError:
            print("Username already exists. Choose a different username.")
            main(cursor, conn)

    elif user_option == 3:
        if admin_sign_in():
            def admin_options():
                print("Admin Options:")
                print("1. Change  items in the item table")
                print("2. Delete  items in the item table")
                print("3. Add records in the  item table")
                print("4. See admin report")
                print("5. Admin Log Out")
                print("6. View feedback")
                print("7. Search by category")


            def change__items():
                print("Change  Items:")
                view__items_query = "SELECT g_id, name, category, price FROM grocery"
                cursor.execute(view__items_query)
                _items = cursor.fetchall()

                if _items:
                    print("Existing Items:")
                    for _item in _items:
                        print(f"g_ID: {_item[0]}, Name: {_item[1]}, category: {_item[2]}, time_consumed:{_item[3]}")

                    itemid = int(input("Enter the ID of the item you want to update: "))
                    newame = input("Enter new name : ")
                    new_category=input("Enter New Category: ")
                    new_price = (input("Enter new price : "))

                    update_grocery_query = "UPDATE grocery SET name = COALESCE(%s, name), category = COALESCE(%s, category), price = COALESCE(%s, price) WHERE g_id = %s"
                    cursor.execute(update_grocery_query, (newame,new_category, new_price, itemid))
                    conn.commit()
                    print("item updated successfully!")

                else:
                    print("No items found to update.")

            def delete_grocery_items():
                print("Delete grocery Items:")
                view_grocery_items_query = "SELECT g_id, name, category, price FROM grocery"
                cursor.execute(view_grocery_items_query)
                grocery_items = cursor.fetchall()

                if grocery_items:
                    print("Existing grocery Items:")
                    for grocery_item in grocery_items:
                        print(f"ID: {grocery_item[0]}, Name: {grocery_item[1]}, Category:{grocery_item[2]} price: {grocery_item[2]}")

                    grocery_id = int(input("Enter the ID of the grocery item you want to delete: "))
                    delete_grocery_query = "DELETE FROM grocery WHERE g_id = %s"
                    cursor.execute(delete_grocery_query, (grocery_id,))
                    conn.commit()
                    print("grocery item deleted successfully!")
                else:
                    print("No grocery items found to delete.")

            def add_grocery_items():
                grocery_name = input("Enter grocery name: ")
                price = input("Enter price: ")
                category=input("Enter New Category: ")
                add_grocery_query = "INSERT INTO grocery (name, category, price) VALUES (%s, %s,%s)"
                cursor.execute(add_grocery_query, (grocery_name, category, price))
                conn.commit()
                print("grocery item added successfully!")

            def admin_main():
                while True:
                    admin_options()
                    admin_choice = int(input("Enter your choice: "))

                    if admin_choice == 1:
                        change__items()
                    elif admin_choice == 2:
                        delete_grocery_items()
                    elif admin_choice == 3:
                        add_grocery_items()
                    elif admin_choice == 4:
                        admin_report()
                    elif admin_choice == 6:
                        view_feedbacks()
                    elif admin_choice == 7:
                        search_by_category()
                    elif admin_choice == 5:
                        print("Admin logging out...")
                        main(cursor, conn)
                    else:
                        print("Invalid choice.")
            admin_main()

    else:
        print("Invalid option.")

    cursor.close()
    conn.close()

main(cursor, conn)
