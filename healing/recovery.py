import subprocess
import sys
import time

from healing.health_check import check_application_health


SERVICE_FILE = "healing/test_service.py"


def start_test_service():

    try:

        subprocess.Popen(
            [
                sys.executable,
                SERVICE_FILE
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        return True

    except Exception as error:

        print("Recovery error:", error)

        return False


def verify_recovery():

    print("\n========== RECOVERY PROCESS ==========")

    # ------------------------------------------------
    # Check whether service is already running
    # ------------------------------------------------

    if check_application_health():

        return {
            "status": "ALREADY_HEALTHY",
            "message": "Service is already healthy."
        }


    print("Service is unhealthy.")

    print("Starting automatic recovery...")


    # ------------------------------------------------
    # Start service
    # ------------------------------------------------

    started = start_test_service()


    if not started:

        return {
            "status": "FAILED",
            "message": "Unable to start recovery service."
        }


    # ------------------------------------------------
    # Give service time to start
    # ------------------------------------------------

    time.sleep(3)


    # ------------------------------------------------
    # Verify recovery
    # ------------------------------------------------

    if check_application_health():

        return {
            "status": "RECOVERED",
            "message": "Service recovered successfully."
        }


    return {
        "status": "FAILED",
        "message": "Service failed to recover."
    }