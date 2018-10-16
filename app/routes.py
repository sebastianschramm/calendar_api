from app.handlers.handler_health import handler_health_check
from app.handlers.handler_matches import get_matches
from app.handlers.handler_users import get_candidates, get_interviewers
from app.handlers.handler_timeslots import get_timeslots_interviewers, get_timeslots_candidates
from app.handlers.handler_timeslots import add_timeslots_interviewers, add_timeslots_candidates


def setup_routes(app):

    service_base_url = '/api/v1'

    user_candidate = "{}/candidates".format(service_base_url)
    candidate_timeslots = "{}/{{user_id}}/timeslots".format(user_candidate)

    user_interviewer = "{}/interviewers".format(service_base_url)
    interviewer_timeslots = "{}/{{user_id}}/timeslots".format(user_interviewer)

    matching_timeslots = "{}/matches".format(service_base_url)

    # health check
    app.router.add_route('GET', '/health', handler_health_check)

    # users
    app.router.add_route('GET', user_candidate, get_candidates)
    #TODO: app.router.add_route('POST', user_candidate, default_handler)
    #TODO: app.router.add_route('DELETE', user_candidate, default_handler)

    app.router.add_route('GET', user_interviewer, get_interviewers)
    #TODO: app.router.add_route('POST', user_interviewer, default_handler)
    #TODO: app.router.add_route('DELETE', user_interviewer, default_handler)

    # timeslots
    app.router.add_route('GET', candidate_timeslots, get_timeslots_candidates)
    app.router.add_route('POST', candidate_timeslots, add_timeslots_candidates)
    #TODO: app.router.add_route('DELETE', candidate_timeslots, default_handler)

    app.router.add_route('GET', interviewer_timeslots, get_timeslots_interviewers)
    app.router.add_route('POST', interviewer_timeslots, add_timeslots_interviewers)
    #TODO: app.router.add_route('DELETE', interviewer_timeslots, default_handler)

    # matching timeslots
    app.router.add_route('POST', matching_timeslots, get_matches)
