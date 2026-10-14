# src/classifier.py
"""Traffic classification model for network intrusion detection.

This module offers a thin wrapper around scikit‑learn’s
RandomForestClassifier. It expects a CSV file containing feature columns
and a binary ``label`` column (0 = benign, 1 = malicious).  The model can
be trained, saved to disk, and later loaded for evaluation or inference.
"""

import os
import joblib
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix


class TrafficClassifier:
    """Encapsulates training, persistence, and evaluation of a traffic‑classification model.

    Attributes
    ----------
    model : RandomForestClassifier
        The underlying scikit‑learn model.
    """

    def __init__(self) -> None:
        """Create a new (un‑trained) classifier."""
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)

    # --------------------------------------------------------------
    # TRAINING
    # --------------------------------------------------------------
    def train(self,
              csv_path: str,
              model_path: str = "data/processed/model.joblib") -> None:
        """Fit the RandomForest on the data in ``csv_path`` and persist it.

        Parameters
        ----------
        csv_path : str
            Path to a CSV file that contains feature columns and a ``label`` column.
        model_path : str, optional
            Where to store the pickled model (default: ``data/processed/model.joblib``).

        Raises
        ------
        FileNotFoundError
            If ``csv_path`` does not exist.
        """
        # Load the CSV
        data = pd.read_csv(csv_path)
        X = data.drop(columns=["label"])
        y = data["label"]

        # Fit the model
        self.model.fit(X, y)
        print(f"Model trained on {len(data)} samples.")

        # Persist the trained model
        os.makedirs(os.path.dirname(model_path), exist_ok=True)
        joblib.dump(self.model, model_path)
        print(f"Model saved to {model_path}")

    # --------------------------------------------------------------
    # EVALUATION
    # --------------------------------------------------------------
    def evaluate(self,
                 csv_path: str = None,
                 model_path: str = "data/processed/model.joblib") -> None:
        """Evaluate the classifier on a CSV dataset.

        If the instance has not been trained yet, this method will try to load a
        previously saved model from ``model_path``.  If the file does not exist,
        a ``RuntimeError`` is raised.

        Parameters
        ----------
        csv_path : str, optional
            Path to a CSV file with the same format used for training.
            Must be provided; otherwise a ``ValueError`` is raised.
        model_path : str, optional
            Location of the saved model (default matches ``train``).

        Raises
        ------
        RuntimeError
            If no trained model is available and ``model_path`` does not exist.
        ValueError
            If ``csv_path`` is not provided.
        """
        # Ensure we have a fitted model – load from disk if necessary
        if not hasattr(self.model, "estimators_"):
            if os.path.exists(model_path):
                self.model = joblib.load(model_path)
                print(f"Loaded saved model from {model_path}")
            else:
                raise RuntimeError("No trained model available. Call train() first.")

        if not csv_path:
            raise ValueError("Evaluation dataset path must be provided.")

        # Load evaluation data
        data = pd.read_csv(csv_path)
        X = data.drop(columns=["label"])
        y = data["label"]

        # Predict and show metrics
        preds = self.model.predict(X)
        print("Classification Report:\n", classification_report(y, preds))
        print("Confusion Matrix:\n", confusion_matrix(y, preds))
