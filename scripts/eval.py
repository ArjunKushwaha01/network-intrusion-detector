from src.classifier import TrafficClassifier
if __name__ == "__main__":
    clf = TrafficClassifier()
    clf.evaluate('data/processed/features.csv')
