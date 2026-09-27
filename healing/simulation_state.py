import json
import os


SIMULATION_FILE = "logs/simulation_state.json"


def get_simulation():

    if not os.path.exists(SIMULATION_FILE):

        return {
            "enabled": False,
            "mode": "NORMAL"
        }

    try:

        with open(
            SIMULATION_FILE,
            "r",
            encoding="utf-8"
        ) as file:

            return json.load(file)

    except Exception:

        return {
            "enabled": False,
            "mode": "NORMAL"
        }


def set_simulation(mode):

    os.makedirs("logs", exist_ok=True)

    data = {
        "enabled": True,
        "mode": mode
    }

    with open(
        SIMULATION_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(data, file, indent=4)


    return data


def clear_simulation():

    os.makedirs("logs", exist_ok=True)

    data = {
        "enabled": False,
        "mode": "NORMAL"
    }

    with open(
        SIMULATION_FILE,
        "w",
        encoding="utf-8"
    ) as file:

        json.dump(data, file, indent=4)


    return data