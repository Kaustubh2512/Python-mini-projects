# Python Mini Projects

I'm currently learning Python with a focus on practical, core programming concepts that are directly applicable to Cybersecurity and Security Operations (SOC). This collection of mini projects revolves around SOC and cybersecurity-related use cases, allowing me to apply programming logic to real-world security scenarios while strengthening my foundational Python skills.

Each project is beginner-friendly, self-contained, and designed to simulate tasks that a SOC Analyst or security enthusiast might encounter, such as log analysis, brute force detection, IP tracking, and event monitoring.

## Table of Contents

- [Projects Overview](#projects-overview)
- [1. Authentication](#1-authentication)
- [2. IP Analysis](#2-ip-analysis)
- [3. Events Fail Check](#3-events-fail-check)
- [Technologies Used](#technologies-used)
- [How to Run These Projects](#how-to-run-these-projects)
- [Learning Takeaways](#learning-takeaways)

## Projects Overview

This repository contains three mini projects, each organized in its own folder. These projects were built while learning Python for Cybersecurity/SOC, with a heavy focus on security log analysis, threat detection, network monitoring, and event correlation.

---

## 1. Authentication

**Folder:** `authentication/`  
**Files:** `authentication.py`, `authlog.txt`

### What This Project Is About

This project simulates a basic SOC log analysis task for authentication events. It reads security logs containing login attempts and identifies users who have failed multiple login attempts. Based on that data, it generates a login report and raises a security alert if brute force attack behavior is detected - a common detection use case in cybersecurity monitoring.

### What I Have Used

- **Python Built-in Functions**: `open()`, `print()`, `strip()`, `split()`
- **Data Structures**: Dictionary (`failed_users`) to track failed attempt counts per user
- **File Handling**: Reading a CSV-style log file (`.txt` format) line by line
- **Control Flow**: Conditional statements (`if`, `elif`), loops (`for`)

### How I Have Used It

1. **Log Parsing**: The script opens `authlog.txt` in read mode and iterates through each line. For every line, it strips whitespace and splits by commas to extract fields: `timestamp`, `username`, `ip`, `event`, `os`, and `service`.
2. **Failed Attempt Tracking**: It checks if the `event` is `LOGIN_FAILED`. If it is, it either increments the count for that username in the `failed_users` dictionary, or initializes it to 1 if it's the first failed attempt.
3. **Report Generation**: After processing all logs, it prints a "LOGIN REPORT" showing each user and their total failed attempts.
4. **Security Alerting**: It then prints a "Security Alerts" section and flags any user with 3 or more failed attempts with a `[Alert] Brute force attack` message.
5. **Log Data**: The `authlog.txt` file contains sample authentication events with mixed successful and failed logins for multiple users (alice, bob, charlie, david) across different IPs, OSes, and services.

### Example Output

```
========LOGIN REPORT=========
charlie : 3 failed attempts
bob : 1 failed attempts
========Security Alerts=======
[Alert] Brute force attack
```

---

## 2. IP Analysis

**Folder:** `ip analysis/`  
**Files:** `ip_analysis.py`

### What This Project Is About

This project is a cybersecurity-focused IP analysis utility. It analyzes a list of IP addresses to identify duplicates and get frequency statistics. In a SOC environment, tracking source IPs, detecting repeated connection attempts, and identifying potential scanning or abuse from specific IPs are crucial tasks. This project mimics that logic on a small scale.

### What I Have Used

- **Python Built-in Functions**: `len()`, `print()`
- **Data Structures**: Lists (to store IPs), Sets (to get unique IPs), Dictionaries (to count occurrences)
- **Loops**: `for` loop to iterate through the list and count frequencies
- **Conditional Logic**: `if/else` to build the frequency map and identify repeated IPs

### How I Have Used It

1. **Data Collection**: A hardcoded list `ips` contains multiple IP address strings, with some duplicates intentionally included.
2. **Unique Count Calculation**: Converted the list to a `set()` to automatically eliminate duplicates, then calculated the count of unique IPs.
3. **Frequency Mapping**: Iterated through the list and built a dictionary where keys are IP addresses and values are the number of times they appear.
4. **Reporting**: Printed the total number of IPs, the number of unique IPs, the full frequency count dictionary, and finally listed only the repeated IPs (those with count > 1).
5. **Practical Use Case**: This mimics a basic log analysis task where you need to detect repeated connections or identify duplicate entries in network logs.

### Example Output

```
total ips: 6
unique ips: 3
{'192.168.1.10': 3, '10.0.0.5': 2, '172.16.0.20': 1}
Repeated ips
192.168.1.10
10.0.0.5
```

---

## 3. Events Fail Check

**Folder:** `events fail check/`  
**Files:** `loops.py`, `loops_deep.py`

### What This Project Is About

These scripts focus on security event monitoring and alerting, which is a core SOC function. They analyze event status logs (such as login/authentication events) and categorize them based on their outcome. The goal is to detect failed login attempts, account lockouts, successful logins, and unknown events, while also generating appropriate alerts based on the severity of failures. Two versions exist - a basic one and a more detailed one with expanded categorization and SOC-style alerting logic.

### What I Have Used

- **Python Built-in Functions**: `print()`, f-strings for formatted output
- **Data Structures**: Lists to store event sequences
- **Control Flow**: `if`, `elif`, `else` for categorization
- **Loops**: `for` loop to iterate through events
- **Counter Variables**: Track counts for different event types

### How I Have Used It

#### `loops.py` (Basic Version)

1. **Event Tracking**: Maintains a single counter `failed_events` to track failed login events.
2. **Event List**: Contains a hardcoded list of event statuses including `SUCCESS`, `FAILED`, and `LOCKED`.
3. **Detection Logic**: Loops through each event and if it's `"FAILED"`, increments the counter and prints `"Failed login detected"`.
4. **Summary**: After processing all events, prints the total number of failed logins detected.

#### `loops_deep.py` (Extended Version)

1. **Multi-Category Tracking**: Tracks four different event types using separate counters: `failed_events`, `succes_events`, `locked_events`, and `unknown_events`.
2. **Expanded Event Set**: Includes additional event types like `UNKNOWN` alongside `SUCCESS`, `FAILED`, and `LOCKED`.
3. **Categorized Processing**: Uses `if/elif/else` to categorize each event and take specific actions:
   - `FAILED` → increment counter, print `"Failed login detected"`
   - `SUCCESS` → increment counter, print `"SUCCESS LOgin"` (note: minor casing in output)
   - `LOCKED` → increment counter, print `"CRITICAL: Account locked"`
   - Any other value → increment `unknown_events`, print `"Unknown login"`
4. **Alerting Logic**: If the number of failed events is >= 3, it prints `"HIGH ALERT"`.
5. **Detailed Summary**: Provides a comprehensive summary showing counts for all tracked event categories.

### Example Outputs

**loops.py:**
```
Failed login detected
Failed login detected
Failed login detected
Failed login detected
total failed login detected: 4
```

**loops_deep.py:**
```
SUCCESS LOgin
Failed login detected
Failed login detected
SUCCESS LOgin
Failed login detected
CRITICAL: Account locked
Unknown login
Unknown login
Failed login detected
HIGH ALERT
=======summary=======
total failed login detected: 5
total success login detected: 2
total locked login detected: 1
total locked unkown detected: 2
```

---

## Technologies Used

- **Language**: Python 3.x
- **Domain**: Cybersecurity / Security Operations (SOC)
- **Core Concepts Used**: File I/O, Data Structures (Lists, Sets, Dictionaries), Loops, Conditional Statements, String Manipulation
- **No External Dependencies**: All projects use only Python's standard library

---

## How to Run These Projects

1. Ensure you have Python 3 installed on your system. You can check by running `python --version` in your terminal.
2. Navigate to the project directory (or run from the root with the correct path).
3. Run each script using Python:

```bash
# Authentication
python "authentication/authentication.py"

# IP Analysis
python "ip analysis/ip_analysis.py"

# Events Fail Check - Basic
python "events fail check/loops.py"

# Events Fail Check - Extended
python "events fail check/loops_deep.py"
```

> **Note:** Since folder names contain spaces, make sure to wrap the paths in quotes as shown above.

---

## Learning Takeaways

While learning Python for Cybersecurity and SOC, these mini projects helped reinforce:

- **Security Log Analysis**: Reading, parsing, and extracting meaningful information from structured security logs (CSV-style logs)
- **Threat Detection Basics**: Implementing simple detection logic for brute force attacks, suspicious IP activity, and abnormal event patterns
- **SOC Monitoring Concepts**: Practicing event categorization, alert generation, and identifying security-relevant events
- **File Handling**: Reading and processing log files - a crucial skill for working with SIEM logs and security data
- **Data Processing**: Counting, deduplicating, and correlating security events
- **Practical Problem Solving**: Translating real-world SOC and cybersecurity scenarios into actionable Python logic
- **Code Organization**: Keeping related files grouped in project-specific folders for better structure
- **Core Python Programming**: Strengthening fundamentals including dictionaries, sets, loops, conditionals, string manipulation, and file I/O - all with a practical security focus
