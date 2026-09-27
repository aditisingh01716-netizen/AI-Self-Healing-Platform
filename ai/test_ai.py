from ai.anomaly_detector import detect_anomaly


print("Testing normal system...")

normal = detect_anomaly(
    30,
    45,
    50
)

print(normal)


print("\nTesting abnormal system...")

abnormal = detect_anomaly(
    98,
    97,
    95
)

print(abnormal)