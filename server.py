from flask import Flask
from flask import request
import psycopg2



@app.route('/pets', methods=['GET'])
def handlePets():
    if request.method == "GET":
        # make database call
        try:
            connection = psycopg2.connect(host="127.0.0.1", port="5432", database="pet_hotel")
            cursor = conn.cursor()
            queryText = 'SELECT "pets"."id", "pets"."name", "pets"."color", "pets"."breed", "pets"."checked_in", 
                "owners"."name" FROM "pets" JOIN "owners" ON "owner_id" = "owners"."id";'
            cursor.execute(queryText)
            pet_records = cursor.fetchall()
        print("Get successful")
        for row in pet_records:
            print("id=", row[0])
    except (Exception, psycopg2.Error) as error :
        print ("Error while fetching data from PostgreSQL", error)