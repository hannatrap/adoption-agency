
DROP DATABASE IF EXISTS  pets_db;

CREATE DATABASE pets_db;



CREATE TABLE pets
(
  id SERIAL PRIMARY KEY,
  name TEXT NOT NULL,
  species TEXT NOT NULL,
  photo_url TEXT,
  age INT,
  notes TEXT,
  available BOOLEAN NOT NULL DEFAULT TRUE
);

INSERT INTO pets
  (name, species, photo_url, age, notes, available)
VALUES
  ('Hans', 'dog', 'https://cdn.pixabay.com/photo/2016/12/13/05/15/puppy-1903313_1280.jpg', 3, '10/10', 't'),
  ('Daisy', 'hamster', 'https://cdn.pixabay.com/photo/2016/10/26/22/00/hamster-1772742_1280.jpg', 8, 'Small and cute', 't'),
  ('Nick', 'cat', 'https://cdn.pixabay.com/photo/2017/07/25/01/22/cat-2536662_1280.jpg', null, 'meow', 't'),
  ('Hanna', 'snake', null, 10, null, 't');

