import unittest

from ai.risk_detector import calculate_risk
from ai.anomaly_detector import detect_anomaly
from ai.incident_engine import analyze_incident
from healing.decision_engine import decide_action

from healing.simulation_state import (
    set_simulation,
    get_simulation,
    clear_simulation
)


class TestRiskDetector(unittest.TestCase):
    """
    Tests the basic resource risk detector.
    """

    def test_low_risk(self):

        result = calculate_risk(
            30,
            40,
            50
        )

        self.assertEqual(
            result,
            "LOW"
        )


    def test_medium_risk(self):

        result = calculate_risk(
            65,
            65,
            60
        )

        self.assertEqual(
            result,
            "MEDIUM"
        )


    def test_high_risk(self):

        result = calculate_risk(
            82,
            85,
            80
        )

        self.assertEqual(
            result,
            "HIGH"
        )


    def test_critical_risk(self):

        result = calculate_risk(
            96,
            95,
            94
        )

        self.assertEqual(
            result,
            "CRITICAL"
        )


class TestAIDetector(unittest.TestCase):
    """
    Tests the machine-learning anomaly detector.
    """

    def test_normal_system(self):

        result = detect_anomaly(
            30,
            45,
            50
        )

        self.assertIn(
            result["status"],
            ["NORMAL", "ANOMALY"]
        )

        self.assertIsInstance(
            result["score"],
            float
        )


    def test_abnormal_system(self):

        result = detect_anomaly(
            98,
            97,
            95
        )

        self.assertEqual(
            result["status"],
            "ANOMALY"
        )


class TestIncidentEngine(unittest.TestCase):
    """
    Tests the intelligent incident analysis engine.
    """

    def test_normal_incident(self):

        metrics = {

            "cpu": 30,

            "memory": 40,

            "disk": 50

        }

        errors = []

        result = analyze_incident(

            metrics,

            errors,

            True

        )

        self.assertEqual(
            result["risk"],
            "LOW"
        )

        self.assertEqual(
            result["recommended_action"],
            "NO_ACTION"
        )


    def test_high_risk_incident(self):

        metrics = {

            "cpu": 82,

            "memory": 85,

            "disk": 80

        }

        errors = []

        result = analyze_incident(

            metrics,

            errors,

            True

        )

        self.assertIn(

            result["risk"],

            ["HIGH", "CRITICAL"]

        )

        self.assertIsInstance(

            result["incident_score"],

            int

        )


    def test_critical_error(self):

        metrics = {

            "cpu": 30,

            "memory": 40,

            "disk": 50

        }

        errors = [

            "[CRITICAL] Application service stopped"

        ]

        result = analyze_incident(

            metrics,

            errors,

            True

        )

        self.assertEqual(

            result["risk"],

            "CRITICAL"

        )


    def test_unhealthy_service(self):

        metrics = {

            "cpu": 30,

            "memory": 40,

            "disk": 50

        }

        errors = []

        result = analyze_incident(

            metrics,

            errors,

            False

        )

        self.assertEqual(

            result["risk"],

            "CRITICAL"

        )

        self.assertEqual(

            result["recommended_action"],

            "RECOVER_SERVICE"

        )


class TestDecisionEngine(unittest.TestCase):
    """
    Tests the self-healing decision engine.
    """

    def test_no_action(self):

        result = decide_action(

            "LOW",

            "No problem detected",

            True

        )

        self.assertEqual(

            result,

            "NO_ACTION"

        )


    def test_monitor(self):

        result = decide_action(

            "MEDIUM",

            "Medium system resource usage",

            True

        )

        self.assertEqual(

            result,

            "MONITOR"

        )


    def test_high_risk_recovery(self):

        result = decide_action(

            "HIGH",

            "High system resource usage",

            True

        )

        self.assertEqual(

            result,

            "RECOVER_SERVICE"

        )


    def test_critical_restart(self):

        result = decide_action(

            "CRITICAL",

            "Critical system resource usage",

            True

        )

        self.assertEqual(

            result,

            "RESTART_SERVICE"

        )


    def test_unhealthy_service(self):

        result = decide_action(

            "LOW",

            "Application service is unhealthy",

            False

        )

        self.assertEqual(

            result,

            "RECOVER_SERVICE"

        )


class TestSimulationSystem(unittest.TestCase):
    """
    Tests the controlled failure simulation system.
    """

    def test_medium_simulation(self):

        result = set_simulation(
            "MEDIUM"
        )

        self.assertTrue(
            result["enabled"]
        )

        self.assertEqual(
            result["mode"],
            "MEDIUM"
        )


    def test_high_simulation(self):

        result = set_simulation(
            "HIGH"
        )

        self.assertTrue(
            result["enabled"]
        )

        self.assertEqual(
            result["mode"],
            "HIGH"
        )


    def test_critical_simulation(self):

        result = set_simulation(
            "CRITICAL"
        )

        self.assertTrue(
            result["enabled"]
        )

        self.assertEqual(
            result["mode"],
            "CRITICAL"
        )


    def test_ai_anomaly_simulation(self):

        result = set_simulation(
            "AI_ANOMALY"
        )

        self.assertTrue(
            result["enabled"]
        )

        self.assertEqual(
            result["mode"],
            "AI_ANOMALY"
        )


    def test_clear_simulation(self):

        set_simulation(
            "CRITICAL"
        )

        result = clear_simulation()

        self.assertFalse(
            result["enabled"]
        )

        self.assertEqual(
            result["mode"],
            "NORMAL"
        )


    def test_get_simulation(self):

        set_simulation(
            "HIGH"
        )

        result = get_simulation()

        self.assertTrue(
            result["enabled"]
        )

        self.assertEqual(
            result["mode"],
            "HIGH"
        )

        clear_simulation()


# ============================================================
# RUN ALL TESTS
# ============================================================

if __name__ == "__main__":

    print()
    print("==============================================")
    print(" AI SOFTWARE RELIABILITY PLATFORM TEST SUITE ")
    print("==============================================")
    print()

    unittest.main(
        verbosity=2
    )