.read data.sql


CREATE TABLE bluedog AS
	SELECT color, pet 
	FROM students
	WHERE color = 'blue' AND pet = 'dog';

CREATE TABLE bluedog_songs AS
	SELECT color, pet, song
	FROM students
	WHERE color = 'blue' AND pet = 'dog';


CREATE TABLE smallest_int_having AS
  SELECT time, smallest from students
	group by smallest having count(*) = 1;


CREATE TABLE matchmaker AS
  SELECT first.pet, first.song, first.color, second.color
	from students as first, students as second
	where first.pet = second.pet and first.song = second.song and first.time < second.time;


CREATE TABLE sevens AS
  SELECT seven from students, numbers 
	where students.time = numbers.time and numbers.'7' = 'True' and smallest <= 7;


