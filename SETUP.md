# Kali Linux Setup Guide

## Requirements
- Kali Linux (2023.x or later) — native or VirtualBox
- Python 3.8+
- Social Engineering Toolkit (SET)
- Wireshark

## Installation

### 1. Update System
```bash
sudo apt update && sudo apt upgrade -y
```

### 2. Install SET
```bash
sudo apt install set -y
```

### 3. Install Python Dependencies
```bash
pip install -r 03-osint-techniques/scripts/requirements.txt
```

### 4. Verify SET
```bash
sudo setoolkit
```

## Network Setup
- Use a host-only or NAT network in VirtualBox
- Never run labs on public or corporate networks
- Isolate all lab traffic to your local machine
