from flask import Flask
from flask import request
from flask import jsonify
import psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)

# to get server running.
# export FLASK_APP=server.py
# or this: export FLASK_ENV=development


@app.route('/pets', methods=['GET', 'POST'])
def handlePets():
    if request.method == "GET":
        # make database call
        # opens up connection
        conn = psycopg2.connect(
            host="127.0.0.1", port="5432", database="pet_hotel")
        try:
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            queryText = '''
            SELECT "owners"."name" as "owner", "pets"."name" as "pet", "pets"."breed", "pets"."color", "pets"."checked_in", "owners"."id" as "owner_id", "pets"."id" as "pet_id"  
            FROM "pets"
            JOIN "owners" 
            ON "owner_id" = "owners"."id"
            ;'''
        # execute sql query
            cursor.execute(queryText)
        # data from databse
            pet_records = cursor.fetchall()
            print("Get successful")
         # equivalent to res.send hopefully?
            return jsonify(pet_records)
        except (Exception, psycopg2.Error) as error:
            print("Error while fetching data from PostgreSQL", error)
        finally:
            # closing database connection.
            if(conn):
                cursor.close()
                conn.close()
                print("PostgreSQL connection is closed")

    elif request.method == "POST":
        # open database post
        conn = psycopg2.connect(
            host="127.0.0.1", port="5432", database="pet_hotel")
        try:
            # connection = psycopg2.connect(host="127.0.0.1", port="5432", database="pet_hotel")
            cursor = conn.cursor()
            #request.get_json = req.body
            print(request.get_json())
            name = request.get_json()['name']
            color = request.get_json()['color']
            breed = request.get_json()['breed']
            owner_id = request.get_json()['owner_id']
            queryText = '''
            INSERT INTO pets ("name", "color", "breed", "owner_id") 
            VALUES (%s, %s, %s, %d)
            ;'''
            insertData = (name, color, breed, owner_id)
            #execute query (currently hardcoded)
            cursor.execute(queryText, insertData)
            #iffy about next stuff
            conn.commit()
            count = cursor.rowcount
            print(count, 'Post successful')
            return 'YOU HAVE POSTED!'
        except(Exception, psycopg2.Error) as error :
            if(conn):
                print('FAIL', error)
        finally: 
            #closing
            if(conn):
                cursor.close()
                conn.close()
                print('POSTGRESQL CLOSED')

