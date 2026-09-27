def decide_action(risk, problem, service_healthy=True):

    # Service is unavailable
    if not service_healthy:
        return "RECOVER_SERVICE"

    # Critical system condition
    if risk == "CRITICAL":
        return "RESTART_SERVICE"

    # High-risk condition
    elif risk == "HIGH":
        return "RECOVER_SERVICE"

    # Medium-risk condition
    elif risk == "MEDIUM":
        return "MONITOR"

    # Normal condition
    else:
        return "NO_ACTION"