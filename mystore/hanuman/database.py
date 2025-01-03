# myapp/management/commands/populate_from_csv.py

from django.core.management.base import BaseCommand
from myapp.models import DummyModel  # Import your Django models here
import pandas as pd
import sqlite3

class Command(BaseCommand):
    help = 'Populate database from CSV'

    def handle(self, *args, **options):
        # Read the CSV file into a pandas DataFrame
        df = pd.read_csv('csv.csv')

        # Connect to the SQLite database
        conn = sqlite3.connect('hanuman.sqlite3')

        # Create a cursor object to execute SQL queries
        cursor = conn.cursor()

        # Define the SQL query to create the table
        create_table_query = '''
        CREATE TABLE IF NOT EXISTS DummyModel (
            id INTEGER PRIMARY KEY,
            name TEXT,
            description TEXT
        );
        '''

        # Execute the SQL query to create the table
        cursor.execute(create_table_query)

        # Iterate over rows in the DataFrame and insert data into the table
        for index, row in df.iterrows():
            # Define the SQL query to insert data into the table
            insert_query = '''
            INSERT INTO DummyModel (name, description) VALUES (?, ?);
            '''
            # Execute the SQL query to insert data into the table
            cursor.execute(insert_query, (row['name'], row['description']))

        # Commit the changes
        conn.commit()

        # Close the cursor and connection
        cursor.close()
        conn.close()

        self.stdout.write(self.style.SUCCESS('Successfully populated database from CSV.'))
