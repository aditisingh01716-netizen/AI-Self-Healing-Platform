import joblib


MODEL_PATH = "ai/model.pkl"


model = joblib.load(MODEL_PATH)


def detect_anomaly(cpu, memory, disk):

    data = [[
        cpu,
        memory,
        disk
    ]]

    prediction = model.predict(data)[0]

    score = model.decision_function(data)[0]

    if prediction == -1:

        return {
            "status": "ANOMALY",
            "score": float(score)
        }

    return {
        "status": "NORMAL",
        "score": float(score)
    }