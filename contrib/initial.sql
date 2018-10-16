CREATE TABLE IF NOT EXISTS candidates
(
  user_id SERIAL PRIMARY KEY,
  user_name text
);

CREATE TABLE IF NOT EXISTS interviewers
(
  user_id SERIAL PRIMARY KEY,
  user_name text
);

CREATE TABLE IF NOT EXISTS candidates_times
(
  user_id integer REFERENCES candidates (user_id) ON UPDATE CASCADE ON DELETE CASCADE,
  date date,
  start_time integer,
  UNIQUE (user_id, date, start_time)
);

CREATE TABLE IF NOT EXISTS interviewers_times
(
  user_id integer REFERENCES interviewers (user_id) ON UPDATE CASCADE ON DELETE CASCADE,
  date date,
  start_time integer,
  UNIQUE (user_id, date, start_time)
);

INSERT INTO candidates(user_name) VALUES('Carl');
INSERT INTO interviewers(user_name) VALUES('John');
INSERT INTO interviewers(user_name) VALUES('Emily');
