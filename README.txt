
Just a basic Python Grocery Management System.

Softwares Used: Python and DBMS
Modules Used: 'mysql.connector' and 'datetime'

Breakdown of code:

1.Importing Required Libraries: The code imports the mysql.connector module to interact with the MySQL database and the datetime module to work with date and time values.

2.Establishing Database Connection: The script establishes a connection to the MySQL server running on the local machine (localhost) with the username root and password root.

3.Creating Database and Tables: The code defines several functions to create the required database and tables:

*create_database(): Creates a database named grocery_management if it doesn't exist.

*create_grocery_table(): Creates a table named grocery with columns for item ID, name, category, price, and quantity. It also inserts some initial grocery items into the table.

*create_user_list_table(): Creates a table named user_list to store user credentials (username and password).

*create_month_table(month): Creates a table with the name passed as an argument (e.g., May_2023) to store user purchases for that specific month.

*create_count_table(): Creates a table named count to store user activity timestamp.

*create_feedback_table(): Creates a table named feedback to store user feedback and comments.


4.Admin Sign-In: The admin_sign_in() function prompts for admin credentials and verifies them.

5.Suggesting Items Based on History: The suggest_items_based_on_history(username, current_month, cursor) function suggests up to 5 items to the user based on their purchase history in the current month.

6.Searching by Category: The search_by_category() function allows users to search for items in the grocery table based on a specified category.

7.Posting and Viewing Feedback: The post_feedback(username, comment) function allows users to post feedback, and view_feedbacks() displays all the posted feedback.

8.Generating Billing System: The generate_billing_system(username, cursor, conn) function provides options to generate a bill for the current day or a specific date. It calls the generate_bill(username, current_month, date, cursor, conn) function to retrieve and display the bill details.

9.Admin Report: The admin_report() function allows the admin to view the number of active users on a specific date, month, or year.

10.Main Function: The main(cursor, conn) function is the entry point of the application. It creates the necessary tables, handles user sign-in and sign-up, and provides different options for users and admins based on their choices.

Breakdown of tables:

1.grocery:

This table stores information about grocery items available in the store.
Columns: g_id (auto-incrementing primary key), name (unique name of the item), category (category the item belongs to), price, and quantity (default value is 0).
The table is pre-populated with a list of grocery items, their categories, and prices.


2.user_list:

This table stores user credentials (username and password) for authentication purposes.
Columns: id (auto-incrementing primary key), username (unique username), and password.


3.[current_month] (e.g., May_2023):

This table is dynamically created based on the current month and year.
It stores the purchase history of users for the given month.
Columns: id (auto-incrementing primary key), username, item (name of the purchased item), category, price, quantity (default value is 1), and time_consumed (timestamp of when the item was consumed/purchased, with a default value of the current timestamp).


4.count:

This table is likely used for tracking user activity or counting user visits/sessions.
Columns: id (auto-incrementing primary key), username, and timestamp (to record the time of the user's activity or visit).


5.feedback:

This table stores feedback or comments submitted by users.
Columns: id (auto-incrementing primary key), username, comment (text of the feedback/comment), and time_posted (timestamp of when the feedback was posted, with a default value of the current timestamp).
