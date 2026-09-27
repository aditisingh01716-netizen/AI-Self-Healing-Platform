from flask import Flask, render_template, jsonify

from database.database import (
    create_database,
    save_incident,
    get_incidents
)

from monitor.system_monitor import get_system_metrics
from monitor.log_monitor import detect_errors

from ai.incident_engine import analyze_incident

from healing.decision_engine import decide_action
from healing.health_check import check_application_health
from healing.recovery import verify_recovery

from healing.failure_simulator import (
    create_test_failure,
    simulate_risk,
    reset_simulation
)


app = Flask(__name__)


# ============================================================
# HOME / DASHBOARD
# ============================================================

@app.route("/")
def home():

    return render_template("index.html")


# ============================================================
# BASIC APPLICATION HEALTH
# ============================================================

@app.route("/health")
def health():

    return jsonify({

        "status": "healthy",

        "message":
            "Application is running"

    })


# ============================================================
# SYSTEM METRICS API
# ============================================================

@app.route("/api/metrics")
def metrics():

    data = get_system_metrics()

    return jsonify(data)


# ============================================================
# LOG MONITORING API
# ============================================================

@app.route("/api/logs")
def logs():

    errors = detect_errors()

    return jsonify({

        "error_count":
            len(errors),

        "errors":
            errors

    })


# ============================================================
# AI ANALYSIS API
# ============================================================

@app.route("/api/analyze")
def analyze():

    # --------------------------------------------------------
    # Collect system metrics
    # --------------------------------------------------------

    metrics = get_system_metrics()


    # --------------------------------------------------------
    # Collect application errors
    # --------------------------------------------------------

    errors = detect_errors()


    # --------------------------------------------------------
    # Check service health
    # --------------------------------------------------------

    service_healthy = check_application_health()


    # --------------------------------------------------------
    # Intelligent incident analysis
    # --------------------------------------------------------

    result = analyze_incident(

        metrics,

        errors,

        service_healthy

    )


    # --------------------------------------------------------
    # Return complete AI analysis
    # --------------------------------------------------------

    return jsonify({

        "cpu":
            metrics["cpu"],

        "memory":
            metrics["memory"],

        "disk":
            metrics["disk"],

        "risk":
            result["risk"],

        "problem":
            result["problem"],

        "ai_status":
            result["ai_status"],

        "ai_score":
            result["ai_score"],

        "incident_score":
            result["incident_score"],

        "resource_risk":
            result["resource_risk"],

        "error_count":
            result["error_count"],

        "critical_error_count":
            result["critical_error_count"],

        "service_healthy":
            result["service_healthy"],

        "recommended_action":
            result["recommended_action"],

        "errors":
            result["errors"]

    })


# ============================================================
# SELF-HEALING API
# ============================================================

@app.route("/api/heal")
def heal():

    # --------------------------------------------------------
    # STEP 1: Collect system metrics
    # --------------------------------------------------------

    metrics = get_system_metrics()


    # --------------------------------------------------------
    # STEP 2: Collect errors
    # --------------------------------------------------------

    errors = detect_errors()


    # --------------------------------------------------------
    # STEP 3: Check service health
    # --------------------------------------------------------

    service_healthy = check_application_health()


    # --------------------------------------------------------
    # STEP 4: AI incident analysis
    # --------------------------------------------------------

    result = analyze_incident(

        metrics,

        errors,

        service_healthy

    )


    risk = result["risk"]

    problem = result["problem"]


    # --------------------------------------------------------
    # STEP 5: Decide healing action
    # --------------------------------------------------------

    action = decide_action(

        risk,

        problem,

        service_healthy

    )


    # --------------------------------------------------------
    # STEP 6: Default recovery information
    # --------------------------------------------------------

    recovery_status = "NOT_STARTED"

    recovery_message = (
        "Recovery not required."
    )


    # --------------------------------------------------------
    # STEP 7: Perform recovery
    # --------------------------------------------------------

    if action in [

        "RECOVER_SERVICE",

        "RESTART_SERVICE"

    ]:

        recovery = verify_recovery()


        recovery_status = (
            recovery["status"]
        )


        recovery_message = (
            recovery["message"]
        )


    # --------------------------------------------------------
    # STEP 8: Monitoring
    # --------------------------------------------------------

    elif action == "MONITOR":

        recovery_status = "MONITORING"


        recovery_message = (
            "System requires monitoring."
        )


    # --------------------------------------------------------
    # STEP 9: No action
    # --------------------------------------------------------

    elif action == "NO_ACTION":

        recovery_status = "NOT_REQUIRED"


        recovery_message = (
            "No recovery action required."
        )


    # --------------------------------------------------------
    # STEP 10: Save incident
    # --------------------------------------------------------

    save_incident(

        metrics["cpu"],

        metrics["memory"],

        metrics["disk"],

        risk,

        problem,

        action,

        recovery_status

    )


    # --------------------------------------------------------
    # STEP 11: Return self-healing result
    # --------------------------------------------------------

    return jsonify({

        "message":
            "Self-healing process completed",

        "cpu":
            metrics["cpu"],

        "memory":
            metrics["memory"],

        "disk":
            metrics["disk"],

        "risk":
            risk,

        "problem":
            problem,

        "service_healthy":
            service_healthy,

        "action":
            action,

        "recovery_status":
            recovery_status,

        "recovery_message":
            recovery_message,

        "ai_status":
            result["ai_status"],

        "ai_score":
            result["ai_score"],

        "incident_score":
            result["incident_score"],

        "resource_risk":
            result["resource_risk"],

        "error_count":
            result["error_count"],

        "critical_error_count":
            result["critical_error_count"],

        "recommended_action":
            result["recommended_action"],

        "errors":
            result["errors"]

    })


# ============================================================
# INCIDENT HISTORY API
# ============================================================

@app.route("/api/incidents")
def incidents():

    records = get_incidents()

    data = []


    for record in records:

        data.append(
            dict(record)
        )


    return jsonify(data)


# ============================================================
# APPLICATION HEALTH CHECK API
# ============================================================

@app.route("/api/health-check")
def health_check():

    healthy = check_application_health()


    if healthy:

        return jsonify({

            "status":
                "HEALTHY",

            "message":
                "Application is responding normally."

        })


    return jsonify({

        "status":
            "UNHEALTHY",

        "message":
            "Application health check failed."

    })


# ============================================================
# FAILURE SIMULATION API
# ============================================================

@app.route("/api/simulate-failure")
def simulate_failure():

    result = create_test_failure()

    return jsonify(result)


# ============================================================
# RISK SIMULATION API
# ============================================================

@app.route("/api/simulate-risk/<mode>")
def simulate_risk_api(mode):

    result = simulate_risk(

        mode.upper()

    )

    return jsonify(result)


# ============================================================
# RESET SIMULATION API
# ============================================================

@app.route("/api/reset-simulation")
def reset_simulation_api():

    result = reset_simulation()

    return jsonify(result)


# ============================================================
# START APPLICATION
# ============================================================

if __name__ == "__main__":

    # Create SQLite database
    create_database()


    # Start Flask application
    #
    # 0.0.0.0 is required for Docker
    # so that the application can be
    # accessed from the Windows host.
    #
    # debug=False prevents Flask's
    # development reloader from
    # restarting the Docker container.

    app.run(

        host="0.0.0.0",

        port=5000,

        debug=False

    )