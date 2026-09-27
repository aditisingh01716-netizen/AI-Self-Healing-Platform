from ai.risk_detector import calculate_risk
from ai.anomaly_detector import detect_anomaly


def analyze_incident(metrics, errors, service_healthy=True):

    # ========================================================
    # STEP 1: Get system metrics
    # ========================================================

    cpu = metrics["cpu"]

    memory = metrics["memory"]

    disk = metrics["disk"]


    # ========================================================
    # STEP 2: Basic resource risk
    # ========================================================

    resource_risk = calculate_risk(
        cpu,
        memory,
        disk
    )


    # ========================================================
    # STEP 3: AI anomaly detection
    # ========================================================

    ai_result = detect_anomaly(
        cpu,
        memory,
        disk
    )


    ai_status = ai_result["status"]

    ai_score = ai_result["score"]


    # ========================================================
    # STEP 4: Count errors
    # ========================================================

    error_count = len(errors)

    critical_error_count = sum(
        1
        for error in errors
        if "[CRITICAL]" in error
    )


    normal_error_count = sum(
        1
        for error in errors
        if "[ERROR]" in error
    )


    # ========================================================
    # STEP 5: Calculate incident score
    # ========================================================

    incident_score = 0


    # --------------------------------------------------------
    # CPU contribution
    # --------------------------------------------------------

    if cpu >= 90:

        incident_score += 30

    elif cpu >= 75:

        incident_score += 20

    elif cpu >= 60:

        incident_score += 10


    # --------------------------------------------------------
    # Memory contribution
    # --------------------------------------------------------

    if memory >= 90:

        incident_score += 30

    elif memory >= 75:

        incident_score += 20

    elif memory >= 60:

        incident_score += 10


    # --------------------------------------------------------
    # Disk contribution
    # --------------------------------------------------------

    if disk >= 90:

        incident_score += 20

    elif disk >= 75:

        incident_score += 15

    elif disk >= 60:

        incident_score += 5


    # --------------------------------------------------------
    # Normal error contribution
    # --------------------------------------------------------

    incident_score += min(
        normal_error_count * 5,
        15
    )


    # --------------------------------------------------------
    # Critical error contribution
    # --------------------------------------------------------

    incident_score += min(
        critical_error_count * 20,
        40
    )


    # --------------------------------------------------------
    # AI anomaly contribution
    # --------------------------------------------------------

    if ai_status == "ANOMALY":

        incident_score += 20


    # --------------------------------------------------------
    # Service health contribution
    # --------------------------------------------------------

    if not service_healthy:

        incident_score += 30


    # Prevent score from exceeding 100

    incident_score = min(
        incident_score,
        100
    )


    # ========================================================
    # STEP 6: Determine intelligent risk
    # ========================================================

    if incident_score >= 70:

        risk = "CRITICAL"

    elif incident_score >= 45:

        risk = "HIGH"

    elif incident_score >= 20:

        risk = "MEDIUM"

    else:

        risk = "LOW"


    # ========================================================
    # STEP 7: Resource risk can raise severity
    # ========================================================

    risk_levels = {
        "LOW": 1,
        "MEDIUM": 2,
        "HIGH": 3,
        "CRITICAL": 4
    }


    if risk_levels[resource_risk] > risk_levels[risk]:

        risk = resource_risk


    # ========================================================
    # STEP 8: Critical errors always require critical risk
    # ========================================================

    if critical_error_count > 0:

        risk = "CRITICAL"


    # ========================================================
    # STEP 9: Unhealthy service requires critical risk
    # ========================================================

    if not service_healthy:

        risk = "CRITICAL"


    # ========================================================
    # STEP 10: Determine problem
    # ========================================================

    problem = "No problem detected"


    if critical_error_count > 0:

        problem = errors[-1]


    elif not service_healthy:

        problem = "Application service is unhealthy"


    elif ai_status == "ANOMALY":

        problem = (
            "AI detected abnormal system behaviour"
        )


    elif resource_risk == "CRITICAL":

        problem = (
            "Critical system resource usage"
        )


    elif resource_risk == "HIGH":

        problem = (
            "High system resource usage"
        )


    elif resource_risk == "MEDIUM":

        problem = (
            "Medium system resource usage"
        )


    elif normal_error_count > 0:

        problem = errors[-1]


    # ========================================================
    # STEP 11: Recommended action
    # ========================================================

    if not service_healthy:

        recommended_action = "RECOVER_SERVICE"

    elif risk == "CRITICAL":

        recommended_action = "RESTART_SERVICE"

    elif risk == "HIGH":

        recommended_action = "RECOVER_SERVICE"

    elif risk == "MEDIUM":

        recommended_action = "MONITOR"

    else:

        recommended_action = "NO_ACTION"


    # ========================================================
    # STEP 12: Return complete analysis
    # ========================================================

    return {

        "risk": risk,

        "problem": problem,

        "errors": errors,

        "error_count": error_count,

        "critical_error_count":
            critical_error_count,

        "ai_status": ai_status,

        "ai_score": ai_score,

        "incident_score":
            incident_score,

        "resource_risk":
            resource_risk,

        "service_healthy":
            service_healthy,

        "recommended_action":
            recommended_action

    }