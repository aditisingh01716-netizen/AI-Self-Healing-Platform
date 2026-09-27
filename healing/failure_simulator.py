import os

from healing.simulation_state import (
    set_simulation,
    clear_simulation
)


def create_test_failure():

    os.makedirs(
        "logs",
        exist_ok=True
    )

    with open(
        "logs/system.log",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(
            "[CRITICAL] "
            "Simulated application failure\n"
        )

    return {
        "status": "FAILURE_CREATED",
        "message":
            "Test application failure created successfully."
    }


def simulate_risk(mode):

    valid_modes = [
        "MEDIUM",
        "HIGH",
        "CRITICAL",
        "AI_ANOMALY"
    ]


    if mode not in valid_modes:

        return {
            "status": "ERROR",
            "message": "Invalid simulation mode."
        }


    result = set_simulation(mode)


    return {
        "status": "SIMULATION_ENABLED",
        "mode": result["mode"],
        "message":
            f"{mode} risk simulation enabled."
    }


def reset_simulation():

    result = clear_simulation()


    return {
        "status": "SIMULATION_RESET",
        "mode": result["mode"],
        "message":
            "System simulation returned to normal."
    }