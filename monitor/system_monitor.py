import psutil

from healing.simulation_state import get_simulation


def get_system_metrics():

    # --------------------------------------------------------
    # GET REAL SYSTEM METRICS
    # --------------------------------------------------------

    cpu = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory().percent

    disk = psutil.disk_usage("/").percent


    # --------------------------------------------------------
    # CHECK CONTROLLED SIMULATION
    # --------------------------------------------------------

    simulation = get_simulation()


    # --------------------------------------------------------
    # APPLY SIMULATED CONDITIONS
    # --------------------------------------------------------

    if simulation["enabled"]:

        mode = simulation["mode"]


        # ----------------------------------------------------
        # MEDIUM RISK
        # ----------------------------------------------------

        if mode == "MEDIUM":

            cpu = 65

            memory = 65

            disk = 60


        # ----------------------------------------------------
        # HIGH RISK
        # ----------------------------------------------------

        elif mode == "HIGH":

            cpu = 82

            memory = 85

            disk = 80


        # ----------------------------------------------------
        # CRITICAL RISK
        # ----------------------------------------------------

        elif mode == "CRITICAL":

            cpu = 96

            memory = 95

            disk = 94


        # ----------------------------------------------------
        # AI ANOMALY SIMULATION
        # ----------------------------------------------------

        elif mode == "AI_ANOMALY":

            cpu = 70

            memory = 72

            disk = 75


    # --------------------------------------------------------
    # RETURN SYSTEM METRICS
    # --------------------------------------------------------

    return {

        "cpu": cpu,

        "memory": memory,

        "disk": disk

    }


# ============================================================
# DIRECT TEST
# ============================================================

if __name__ == "__main__":

    metrics = get_system_metrics()


    print(
        "CPU:",
        metrics["cpu"],
        "%"
    )


    print(
        "Memory:",
        metrics["memory"],
        "%"
    )


    print(
        "Disk:",
        metrics["disk"],
        "%"
    )