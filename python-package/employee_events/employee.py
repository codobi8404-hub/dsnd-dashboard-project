# Import the QueryBase class
from python_package.employee_events.query_base import QueryBase

# Now you can use the QueryBase class in your code
query_base_instance = QueryBase()

# Import dependencies needed for sql execution
# from the `sql_execution` module
import sqlite3  # For SQLite database connections and execution
from contextlib import closing  # To ensure proper resource management


# Define a subclass of QueryBase
# called Employee
class QueryBase:
    def __init__(self, db_connection):
        self.db_connection = db_connection 

    def execute_query(self, query):
        with self.db_connection:
            cursor = self.db_connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()

# Define the Employee subclass
class Employee(QueryBase):
    def __init__(self, db_connection):
        super().__init__(db_connection)  # Call the constructor of QueryBase

    def get_employee_names(self):
        query = "SELECT name FROM employees;"  # Example SQL query
        return self.execute_query(query)

    def get_employee_by_id(self, employee_id):
        query = f"SELECT * FROM employees WHERE id = {employee_id};"  # Example SQL query
        return self.execute_query(query)


    # Set the class attribute `name`
    # to the string "employee"

class Employee:
    # Set the class attribute `name`
    name = "employee"

    def __init__(self):
        # You can also define instance attributes here if needed
        pass

# Example of how to access the class attribute
print(YourClassName.name)

    # Define a method called `names`
    # that receives no arguments
    # This method should return a list of tuples
    # from an sql execution


class QueryBase:
    def __init__(self, db_path):
        self.db_path = db_path

    def execute_query(self, query):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(query)
            return cursor.fetchall()

class Employee(QueryBase):
    def __init__(self, db_path):
        super().__init__(db_path)

    def names(self):
        # Define the SQL query to retrieve names
        query = "SELECT name FROM employees;"  # Replace 'employees' with your actual table name
        return self.execute_query(query)

# Example usage
if __name__ == "__main__":
    db_path = 'path/to/your/database.db'  # Update this with your actual database path
    employee = Employee(db_path)
    names_list = employee.names()
    print(names_list)
       
    # Query 3
        # Write an SQL query
        # that selects two columns 
        # 1. The employee's full name
        # 2. The employee's id
        # This query should return the data
        # for all employees in the database

# Connect to the SQLite database
connection = sqlite3.connect('employee_events.db')  # Update with your actual database path

# Create a cursor object
cursor = connection.cursor()

# Define the SQL query
query = """
SELECT 
    CONCAT(first_name, ' ', last_name) AS full_name, 
    id 
FROM 
    employees;
"""

# Execute the query
cursor.execute(query)

# Fetch all results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)

# Close the connection
connection.close()    

    # Define a method called `username`
    # that receives an `id` argument
    # This method should return a list of tuples
    # from an sql execution
        
        # Query 4
        # Write an SQL query
        # that selects an employees full name
        # Use f-string formatting and a WHERE filter
        # to only return the full name of the employee
        # with an id equal to the id argument
class QueryBase:
    def __init__(self, db_path):
        self.db_path = db_path

    def execute_query(self, query, params=()):
        with sqlite3.connect(self.db_path) as connection:
            cursor = connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

class Employee(QueryBase):
    def __init__(self, db_path):
        super().__init__(db_path)

    def username(self, id):
        # Define the SQL query to retrieve the username based on the provided id
        query = "SELECT username FROM employees WHERE id = ?;"  # Replace 'employees' with your actual table name
        return self.execute_query(query, (id,))  # Pass the id as a parameter

# Example usage
if __name__ == "__main__":
    db_path = 'path/to/your/database.db'  # Update this with your actual database path
    employee = Employee(db_path)
    user_id = 1  # Replace with the actual id you want to query
    username_result = employee.username(user_id)
    print(username_result)  # This will print the list of tuples with the username

    # Below is method with an SQL query
    # This SQL query generates the data needed for
    # the machine learning model.
    # Without editing the query, alter this method
    # so when it is called, a pandas dataframe
    # is returns containing the execution of
    # the sql query
    #### YOUR CODE HERE
    def model_data(self, id):

        return f"""
                    SELECT SUM(positive_events) positive_events
                         , SUM(negative_events) negative_events
                    FROM {self.name}
                    JOIN employee_events
                        USING({self.name}_id)
                    WHERE {self.name}.{self.name}_id = {id}
                """
