from api_request import fetch_data
import json

import psycopg2

def formated_data():
    raw_data = fetch_data()
    result_data = raw_data['results'][0]
    
    data = {}
    data['name'] = result_data['name']['first'] + result_data['name']['last']
    data['gender'] = result_data['gender']
    data['email'] = result_data['email']
    data['phone'] =result_data['phone']
    data['address'] = f"{result_data['location']['street']['number']}, "\
                    f"{result_data['location']['street']['name']}, {result_data['location']['city']}, "\
                    f"{result_data['location']['state']}, {result_data['location']['country']}"
                    
    data['picture'] = result_data['picture']['medium']
    data['username'] = result_data['login']['username']
    data['registered_date'] = result_data['registered']['date']
    
    
    return(data)

def connect_to_db():
    print("Connecting to the PostgreSQL database......")
    try:
       conn=  psycopg2.connect(
            host= "db",
            port= 5432,
            dbname= "db",
            user= "db_user",
            password= "db_password"
        )
       return conn
    
    except psycopg2.Error as e:
        print(f"database connection failed: {e}")
        raise
    
def create_table(conn):
    print("Creating table ")
    try:
        cursor = conn.cursor()
        cursor.execute("""
        create schema if not exists dev;
        create table if not exists dev.user_data(
            id serial primary key,
            name text,
            gender text,
            address text,
            email text,
            phone text,
            picture text,
            user_name text,
            registered_date date,
            inserted_at timestamp default now()
        )
        """)
        conn.commit()
        print("Table was created")
    except psycopg2.Error as  e: 
        print(f"Failed to create table: {e}")

def insert_data(conn, data):
    print("Inserting data to table.....")
    try:
        cursor = conn.cursor()
        cursor.execute("""
            insert into dev.user_data(
                name,
                gender, 
                address,
                email,
                phone,
                picture,
                user_name,
                registered_date,
                inserted_at
            )
            values(%s ,%s ,%s, %s, %s, %s, %s, %s, now())         
                       
        """,(data['name'],
            data['gender'], 
            data['address'],
            data['email'], 
            data['phone'],
            data['picture'],
            data['username'],
            data['registered_date']))
        conn.commit()
        print("Inserted data successfully!")
    except psycopg2.Error as e :
        print(f"Failed to insert data: {e}")
        
        
def main():
    try:
        conn = connect_to_db()
        create_table(conn=conn)
        insert_data(conn, formated_data())
    except Exception as e:
        print(f"An error occured: {e}")
    finally: 
        if 'conn' in locals():
            conn.close()
            print("Connection was closed.")
