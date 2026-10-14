# scripts/train.py
import os
import sys

# Add the project root (one level up from the script) to the import path
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.append(PROJECT_ROOT)

from src.classifier import TrafficClassifier

if __name__ == "__main__":
    classifier = TrafficClassifier()
    classifier.train('data/processed/features.csv')
