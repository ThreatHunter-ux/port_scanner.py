# Port Scanner

A simple and efficient port scanner tool written in Python that scans a specified range of ports on a target IP address or website and identifies open ports along with their services.

---

## Author

Shayan

---

## Features

- Scans a range of ports on a target IP or domain.
- Identifies open ports and attempts to detect the associated service.
- Uses multithreading for faster scanning.
- User-friendly command-line interface.

---

## Requirements

- Python 3.x
- Internet connection (for hostname resolution)

---

## Installation and Usage (Linux)

Follow these steps to get started with the port scanner on a Linux system:

1. **Clone the repository:**

```bash
git clone https://github.com/ThreatHunter-ux/port_scanner.py.git
Navigate to the cloned directory:
bash

Copy
cd port_scanner.py

Run the port scanner:
bash

Copy
python3 port_scanner.py
Provide input when prompted:
Enter the IP address or website URL (e.g., example.com or https://example.com)
Enter the start port number (e.g., 1)
Enter the end port number (e.g., 1024)
Example:


Copy
Enter IP address or website URL (e.g. example.com or https://example.com): example.com
Enter start port: 1
Enter end port: 1024
Important Notes
Ensure you have permission to scan the target IP or domain to avoid legal issues.
Scanning a large range of ports may take some time and consume system resources.
The tool uses threading to speed up the scanning process.
License
This project is licensed under the MIT License.

