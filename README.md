
# Keylogger Detection Tool

## Overview

The Keylogger Detection Tool is designed to monitor processes, file system activity, and network connections on a system to detect and alert users to potential keylogging activity. The tool provides real-time monitoring, alerting, and logging capabilities to help protect your system from malicious keyloggers.

## Features

- **Process Monitoring:** Detects suspicious processes that may be keyloggers based on known signatures and behavior patterns.
- **File System Monitoring:** Watches for suspicious file creation and modification activities, particularly in sensitive directories.
- **Network Monitoring:** Monitors network connections for unusual outbound traffic that may indicate a keylogger sending captured data to a remote server.
- **Alerts:** Sends email and SMS alerts when suspicious activity is detected, allowing for immediate action.
- **Logging:** Logs all detected events and alerts to a file for further analysis and auditing.

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository:**

   \`\`\`bash
   git clone https://github.com/yourusername/keylogger_detection_tool.git
   cd keylogger_detection_tool
   \`\`\`

2. **Create and activate a virtual environment:**

   \`\`\`bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scriptsctivate
   \`\`\`

3. **Install dependencies:**

   \`\`\`bash
   pip install -r requirements.txt
   \`\`\`

## Usage

The Keylogger Detection Tool can be run from the command line with various options for process scanning, file monitoring, and network monitoring.

### Running the Tool

To run the tool with all monitoring features enabled:

\`\`\`bash
python run_tool.py --scan-processes --monitor-files --monitor-network
\`\`\`

### Command-Line Options

- \`--scan-processes\`: Scan the system for suspicious processes.
- \`--monitor-files\`: Monitor specified directories for suspicious file activity.
- \`--monitor-network\`: Monitor network connections for suspicious outbound activity.

### Monitoring Logs and Alerts

- Logs are stored in \`keylogger_detection.log\` in the root directory of the project.
- Alerts are sent via email and SMS as configured in \`config.py\`.

## Configuration

The tool's behavior can be customized through the \`config.py\` file.

### Directories to Monitor

Specify which directories should be monitored for suspicious file activity:

\`\`\`python
DIRECTORIES_TO_MONITOR = ["/path/to/monitor"]
\`\`\`

### Trusted IP Addresses

Define trusted IP addresses to avoid false positives in network monitoring:

\`\`\`python
TRUSTED_IPS = ['192.168.1.1', '127.0.0.1']
\`\`\`

### Email Alert Settings

Configure the SMTP settings for sending email alerts:

\`\`\`python
EMAIL_SETTINGS = {
    "smtp_server": "smtp.example.com",
    "port": 587,
    "from_email": "your_email@example.com",
    "password": "your_password",
    "to_email": "admin@example.com"
}
\`\`\`

### Twilio SMS Alert Settings

Configure Twilio settings for sending SMS alerts:

\`\`\`python
TWILIO_SETTINGS = {
    "account_sid": "your_account_sid",
    "auth_token": "your_auth_token",
    "from_number": "your_twilio_number",
    "to_number": "+1234567890"
}
\`\`\`

## Deployment

### Docker Deployment

The tool can be containerized using Docker for easy deployment.

1. **Build the Docker image:**

   \`\`\`bash
   docker build -t keylogger_detection_tool .
   \`\`\`

2. **Run the Docker container:**

   \`\`\`bash
   docker run -p 5000:5000 keylogger_detection_tool
   \`\`\`

### Executable Packaging

To create a standalone executable, you can use \`pyinstaller\`:

\`\`\`bash
pip install pyinstaller
pyinstaller --onefile run_tool.py
\`\`\`

The executable will be created in the \`dist\` directory.

## Testing

The tool includes unit tests to verify its functionality.

### Running Unit Tests

To run the unit tests:

\`\`\`bash
python -m unittest discover -s tests
\`\`\`

This command will discover and run all tests in the \`tests\` directory.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue on GitHub if you have any suggestions or find any bugs.

## License

This project is licensed under the MIT License. See the \`LICENSE\` file for more details.
