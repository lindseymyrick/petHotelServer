-- table for owners
CREATE TABLE owners (
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR (80)
);

-- table for pets
CREATE TABLE pets (
	"id" SERIAL PRIMARY KEY,
	"name" VARCHAR (80),
	"breed" VARCHAR (80),
	"color" VARCHAR (80),
	"checked_in" BOOLEAN DEFAULT 'false',
	"owner_id" INT
);

-- test data for owners table
INSERT INTO owners ("name")
VALUES ('Steve');
INSERT INTO owners ("name")
VALUES ('Heather');
INSERT INTO owners ("name")
VALUES ('Mohamed');
INSERT INTO owners ("name")
VALUES ('Shaokee');
INSERT INTO owners ("name")
VALUES ('Lindsey');

-- test data for pets table
INSERT INTO pets ("name", "color", "breed", "owner_id")
VALUES ('Frog', 'blue', 'leopard', '1');
INSERT INTO pets ("name", "color", "breed", "owner_id")
VALUES ('Horse', 'green', 'arabian', '1');
INSERT INTO pets ("name", "color", "breed", "owner_id")
VALUES ('T-rex', 'green', 'dilong', '1');
INSERT INTO pets ("name", "color", "breed", "owner_id")
VALUES ('Turtle', 'purple', 'wood', '2');
INSERT INTO pets ("name", "color", "breed", "owner_id")
VALUES ('Bear', 'white', 'black', '2');
INSERT INTO pets ("name", "color", "breed", "owner_id")
VALUES ('Scorpion', 'black', 'hairy', '3');
INSERT INTO pets ("name", "color", "breed", "owner_id")
VALUES ('Chipmunk', 'pink', 'california', '3');
INSERT INTO pets ("name", "color", "breed", "owner_id")
VALUES ('Dragon', 'gold', 'african', '4');
INSERT INTO pets ("name", "color", "breed", "owner_id")
VALUES ('Bunny', 'Red', 'dwarf', '5');
INSERT INTO pets ("name", "color", "breed", "owner_id")
VALUES ('Tiger', 'Yellow', 'siberian', '5');

-- selects owners names and their pets info
SELECT "owners"."name" as "owner", "pets"."name" as "pet", "pets"."breed", "pets"."color", "pets"."checked_in", "owners"."id" as "owner_id", "pets"."id" as "pet_id"  
FROM "pets"
JOIN "owners" 
ON "owner_id" = "owners"."id";

-- selects owners names and number of pets they own
SELECT "owners"."name" as "name", COUNT("pets"."name") as "number_of_pets", "owners"."id" as "owner_id"
FROM "owners" 
JOIN "pets" 
ON "owner_id" = "owners"."id"
GROUP BY "owners"."id";