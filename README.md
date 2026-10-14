# Network Intrusion Detection System
<img width="808" height="680" alt="confusion_matrix" src="https://github.com/user-attachments/assets/c2b436c1-e9ae-4366-a71d-e00878bbebb1" />

## Project Overview

- **ID**: network-intrusion-detection
- **Number**: 02
- **Name**: Network Intrusion Detection System
- **Category**: Python & Wireshark
- **Description**: Captured and analyzed raw network traffic using Wireshark and Zeek. Built a Python‑based traffic classification model to detect malicious port scans and anomalous patterns, tuning rules to reduce false positives.
- **Tags**: Wireshark, Python, Zeek, Traffic Classification, Network Forensics, TCP/IP

## Goals

- Capture live network traffic using **pyshark** (Python bindings for Wireshark).
- Parse Zeek logs for enriched session information.
- Train a simple machine‑learning model (e.g., RandomForest) to classify traffic as benign or malicious.
- Provide utilities to generate PCAPs, extract features, and evaluate model performance.

## Repository Structure

```
network-intrusion-detection/
├─ README.md                # Project description (this file)
├─ requirements.txt        # Python dependencies
├─ src/
│   ├─ __init__.py
│   └─ classifier.py       # Traffic classification model
├─ scripts/
│   ├─ capture_packets.py  # Live capture utility using pyshark
│   └─ zeek_integration.py# Parse Zeek logs and enrich features
└─ data/
    ├─ raw/               # Raw PCAP files (git‑ignore)
    └─ processed/         # Extracted feature CSVs
```

## Getting Started

1. **Install dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   ```
2. **Capture traffic**
   ```bash
   python scripts/capture_packets.py --interface eth0 --duration 60 --output data/raw/capture.pcap
   ```
3. **Process Zeek logs** (run Zeek on the captured PCAP and then parse)
   ```bash
   zeek -r data/raw/capture.pcap local
   python scripts/zeek_integration.py --logdir . --output data/processed/features.csv
   ```
4. **Train & evaluate model**
   ```python
   from src.classifier import TrafficClassifier
   model = TrafficClassifier()
   model.train('data/processed/features.csv')
   model.evaluate()
   ```


## ▶️ How to run the demo

```bash
# Clone the repo
git clone https://github.com/ArjunKushwaha01/network-intrusion-detector.git
cd network-intrusion-detector

# Set up a virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# (Re)generate the synthetic data
python generate_data.py

# Train the model
python -m scripts.train

# Evaluate – prints the classification report
python -m scripts.eval

# Produce the confusion‑matrix image (shown in this README)
python scripts/plot_confusion.py


## Contributing

Feel free to open issues or submit pull requests. Please keep the `data/raw/` directory out of version control.


