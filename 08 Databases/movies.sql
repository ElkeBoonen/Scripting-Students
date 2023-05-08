CREATE DATABASE movies_db;
USE movies_db;

CREATE TABLE movies (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    synopsis TEXT
);

CREATE TABLE actors (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE movie_actor (
    actor_id INT,
    movie_id INT,
    PRIMARY KEY (actor_id, movie_id),
    FOREIGN KEY (actor_id) REFERENCES actors(id),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
);

CREATE TABLE awardshows (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(255) NOT NULL
);

CREATE TABLE awards (
    id INT PRIMARY KEY AUTO_INCREMENT,
    awardshow_id INT,
    year INT,
    movie_id INT,
    awards INT,
    nominations INT,
    FOREIGN KEY (awardshow_id) REFERENCES awardshows(id),
    FOREIGN KEY (movie_id) REFERENCES movies(id)
);

INSERT INTO movies (title, synopsis)
VALUES
    ('Everything Everywhere All at Once', 'A multiverse-spanning adventure'),
    ('All Quiet on the Western Front', 'A World War I drama'),
    ('The Whale', 'A man attempts to reunite with his estranged daughter'),
    ('Top Gun: Maverick', 'Maverick returns to train a new generation of fighter pilots');

INSERT INTO actors (name)
VALUES
    ('Michelle Yeoh'),
    ('Stephan James'),
    ('Jamie Lee Curtis'),
    ('Tom Cruise');

INSERT INTO movie_actor (actor_id, movie_id)
VALUES
    (1, 1),
    (2, 1),
    (3, 1),
    (4, 4);

INSERT INTO awardshows (name)
VALUES
    ('Academy Awards'),
    ('Golden Globe Awards'),
    ('Emmy Awards');

INSERT INTO awards (awardshow_id, year, movie_id, awards, nominations)
VALUES
    (1, 2022, 1, 7, 11),
    (2, 2022, 1, 4, 9),
    (3, 2022, 3, 2, 3),
    (2, 2022, 4, 1, 6);
