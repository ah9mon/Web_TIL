CREATE TABLE contacts (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  email TEXT NOT NULL UNIQUE
);

CREATE TABLE contacts (
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  email TEXT NOT NULL UNIQUE
);


ALTER TABLE contacts RENAME TO new_contacts;
ALTER TABLE new_contacts RENAME COLUMN name TO last_name;

ALTER TABLE new_contacts ADD COLUMN address TEXT NOT NULL;

ALTER TABLE new_contacts DROP COLUMN address;

-- DROP TABLE new_contacts
-- DROP TABLE new_contacts2
-- DROP TABLE contacts2s

SELECT COUNT(*) FROM users;

SELECT avg(balance) FROM users;

SELECT DISTINCT country, avg(balance) FROM users GROUP BY country ORDER BY avg(balance) DESC;

SELECT AVG(age) FROM users WHERE age >= 30;  

SELECT country,COUNT(country) FROM users GROUP BY country;

SELECT last_name, COUNT(*) AS the_number_of_name  FROM users GROUP BY last_name;

SELECT last_name, COUNT(*) AS the_number_of_name  FROM users GROUP BY last_name ORDER BY COUNT(*) DESC;

SELECT country, AVG(age) FROM users GROUP BY country;

CREATE TABLE classmates (
name TEXT NOT NULL,
age INTEGER NOT NULL,
address TEXT NOT NULL
);

INSERT INTO classmates (name, age, address) VALUES ('엄한결', 27, '서울');
INSERT INTO classmates VALUES ('어무해', 27, '장고');
INSERT INTO classmates 
VALUES 
('상재우', 27, '서울'),
('중재우', 27, '서울'),
('하재우', 27, '서울')
;

UPDATE classmates
SET 
name = '김철수',
address = '제주'
WHERE 
name = '어무해';

DELETE FROM classmates
WHERE rowid = 5;

DELETE FROM classmates
WHERE name LIKE '%우%';

DELETE FROM classmates;

CREATE TABLE zoo (
  name TEXT NOT NULL,
  eat TEXT NOT NULL,
  weight INT NOT NULL,
  height INT,
  age INT
);

INSERT INTO zoo VALUES 
('gorilla', 'omnivore', 215, 180, 5),
('tiger', 'carnivore', 220, 115, 3),
('elephant', 'herbivore', 3800, 280, 10),
('dog', 'omnivore', 8, 20, 1),
('panda', 'herbivore', 80, 90, 2),
('pig', 'omnivore', 70, 45, 5);

BEGIN;
  DELETE FROM zoo
  WHERE weight < 100;
ROLLBACK;

BEGIN;
  DELETE FROM zoo
  WHERE eat = 'omnivore';
COMMIT;

SELECT COUNT(*)
FROM zoo;
