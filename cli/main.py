import argparse
from detection.process_monitor import detect_suspicious_processes
from detection.file_system_monitor import monitor_file_system
from detection.network_monitor import monitor_network_activity

def main():
    parser = argparse.ArgumentParser(description="Keylogger Detection Tool")
    parser.add_argument("--scan-processes", action="store_true", help="Scan for suspicious processes")
    parser.add_argument("--monitor-files", action="store_true", help="Monitor file system for suspicious activity")
    parser.add_argument("--monitor-network", action="store_true", help="Monitor network for suspicious activity")

    args = parser.parse_args()

    if args.scan_processes:
        detect_suspicious_processes()
    if args.monitor_files:
        monitor_file_system()
    if args.monitor_network:
        monitor_network_activity()

if __name__ == "__main__":
    main()
