import unittest
from detection.process_monitor import detect_suspicious_processes
from detection.network_monitor import monitor_network_activity

class TestDetection(unittest.TestCase):
    def test_detect_suspicious_processes(self):
        suspicious_processes = detect_suspicious_processes()
        self.assertIsInstance(suspicious_processes, list)

    def test_monitor_network_activity(self):
        suspicious_connections = monitor_network_activity()
        self.assertIsInstance(suspicious_connections, list)

if __name__ == "__main__":
    unittest.main()
