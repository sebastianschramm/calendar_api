from collections import namedtuple

DBAccessVars = namedtuple('DBAccessVars', ['user', 'password', 'host', 'port', 'dbname'])

MatchInput = namedtuple('MatchInput', ['candidate_id', 'interviewers_ids'])

TimeslotsInput = namedtuple('TimeslotsInput', ['timeslots'])

TimeslotWithUser = namedtuple('TimeslotWithUser', ['date', 'start_time', 'user_id'])
