# Keylogger Detection Tool

A host-based defensive tool that monitors processes, file system activity, and network connections to detect potential keylogger activity in real time.

## Features

- **Process Monitoring** — detects suspicious processes by known name signatures
- **File System Monitoring** — watches configured directories for suspicious file creation (e.g. `.log` files)
- **Network Monitoring** — flags established outbound connections to untrusted IPs
- **Alerting** — sends email (SMTP) and SMS (Twilio) notifications on detection
- **Logging** — writes all events and alerts to a timestamped log file

## Requirements

- Python 3.13+
- pip

## Installation

```bash
git clone https://github.com/yourusername/Key-Logger-Detection-Tool.git
cd Key-Logger-Detection-Tool

python3.13 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt
```

## Configuration

All settings are read from environment variables. Copy the example file and fill in your values:

```bash
cp .env.example .env
```

| Variable | Description |
|---|---|
| `MONITOR_DIRECTORIES` | Colon-separated paths to watch (e.g. `/home:/tmp`) |
| `TRUSTED_IPS` | Comma-separated IPs that won't trigger network alerts |
| `LOG_FILE` | Path for the detection log (default: `keylogger_detection.log`) |
| `SMTP_SERVER` / `SMTP_PORT` | SMTP server for email alerts |
| `FROM_EMAIL` / `EMAIL_PASSWORD` / `TO_EMAIL` | Email credentials |
| `TWILIO_ACCOUNT_SID` / `TWILIO_AUTH_TOKEN` | Twilio credentials |
| `TWILIO_FROM_NUMBER` / `TWILIO_TO_NUMBER` | SMS numbers |

## Usage

```bash
# Scan running processes once
python run_tool.py --scan-processes

# Watch configured directories for suspicious file activity
python run_tool.py --monitor-files

# Check network connections against trusted IPs
python run_tool.py --monitor-network

# Run all monitors
python run_tool.py --scan-processes --monitor-files --monitor-network
```

Logs are written to the path set in `LOG_FILE` (default: `keylogger_detection.log`).

## Testing

```bash
python -m pytest tests/ -v
```

## Docker

```bash
docker build -t keylogger-detection-tool .
docker run --env-file .env keylogger-detection-tool
```

## License

MIT — see `LICENSE` for details.
