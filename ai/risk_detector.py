def calculate_risk(cpu, memory, disk):

    if cpu >= 90 or memory >= 90 or disk >= 90:

        return "CRITICAL"

    elif cpu >= 75 or memory >= 75 or disk >= 75:

        return "HIGH"

    elif cpu >= 60 or memory >= 60 or disk >= 60:

        return "MEDIUM"

    else:

        return "LOW"