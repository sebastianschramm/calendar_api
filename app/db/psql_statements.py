CREATE_CANDIDATES_TABLE = """
CREATE TABLE IF NOT EXISTS candidates
(
  user_id SERIAL PRIMARY KEY,
  user_name text
)
"""

CREATE_INTERVIEWERS_TABLE = """
CREATE TABLE IF NOT EXISTS interviewers
(
  user_id SERIAL PRIMARY KEY,
  user_name text
)
"""

CREATE_CANDIDATES_TIMES_TABLES = """
CREATE TABLE IF NOT EXISTS candidates_times
(
  user_id integer REFERENCES candidates (user_id) ON UPDATE CASCADE ON DELETE CASCADE,
  date date,
  start_time integer,
  UNIQUE (user_id, date, start_time)
)
"""

CREATE_INTERVIEWERS_TIMES_TABLES = """
CREATE TABLE IF NOT EXISTS interviewers_times
(
  user_id integer REFERENCES interviewers (user_id) ON UPDATE CASCADE ON DELETE CASCADE,
  date date,
  start_time integer,
  UNIQUE (user_id, date, start_time)
)
"""

INSERT_CANDIDATE = """
INSERT INTO candidates(user_name) VALUES($1)
"""

INSERT_INTERVIEWER = """
INSERT INTO interviewers(user_name) VALUES($1)
"""

DELETE_CANDIDATE = """
DELETE FROM candidates WHERE user_id = $1
"""

DELETE_INTERVIEWER = """
DELETE FROM interviewers WHERE user_id = $1
"""

GET_INTERVIEWERS = """
SELECT * from interviewers
"""

GET_CANDIDATES = """
SELECT * from candidates
"""

INSERT_CANDIDATE_TIMES = """
INSERT INTO candidates_times(date, start_time, user_id) VALUES($1, $2, $3) ON CONFLICT DO NOTHING
"""

INSERT_INTERVIEWER_TIMES = """
INSERT INTO interviewers_times(date, start_time, user_id) VALUES($1, $2, $3) ON CONFLICT DO NOTHING
"""

GET_CANDIDATE_TIMES = """
SELECT date, start_time from candidates_times WHERE user_id = $1
"""

GET_INTERVIEWER_TIMES = """
SELECT date, start_time from interviewers_times WHERE user_id = $1
"""

GET_MATCHES = """
SELECT  candidates_times.date, candidates_times.start_time FROM candidates_times 
INNER JOIN interviewers_times 
ON candidates_times.date = interviewers_times.date 
AND candidates_times.start_time = interviewers_times.start_time 
WHERE candidates_times.user_id = $1 and interviewers_times.user_id = ANY ($2)
"""
