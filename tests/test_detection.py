import unittest
from detection.process_monitor import detect_suspicious_processes
from detection.network_monitor import monitor_network_activity


class TestDetection(unittest.TestCase):
    def test_detect_suspicious_processes(self):
        result = detect_suspicious_processes()
        self.assertIsInstance(result, list)

    def test_monitor_network_activity(self):
        result = monitor_network_activity()
        self.assertIsInstance(result, list)


if __name__ == "__main__":
    unittest.main()
