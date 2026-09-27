import os


LOG_FILE = "logs/system.log"


def write_log(level, message):

    os.makedirs("logs", exist_ok=True)

    with open(LOG_FILE, "a", encoding="utf-8") as file:

        file.write(
            f"[{level}] {message}\n"
        )


def read_logs():

    if not os.path.exists(LOG_FILE):

        return []

    with open(LOG_FILE, "r", encoding="utf-8") as file:

        return file.readlines()


def detect_errors():

    logs = read_logs()

    errors = []

    for log in logs:

        if "[ERROR]" in log or "[CRITICAL]" in log:

            errors.append(log.strip())

    return errors


if __name__ == "__main__":

    write_log(
        "INFO",
        "Application started successfully"
    )

    write_log(
        "WARNING",
        "CPU usage is increasing"
    )

    write_log(
        "ERROR",
        "Database connection failed"
    )

    write_log(
        "CRITICAL",
        "Application service stopped"
    )

    print("Test logs created.")

    errors = detect_errors()

    print("\nDetected errors:")

    for error in errors:

        print(error)