# generate_data.py
"""Create synthetic network traffic features for demo purposes.
Columns: duration, src_bytes, dst_bytes, packet_count, label (0 benign, 1 malicious)
"""
import pandas as pd
import numpy as np

np.random.seed(42)
N = 200
# benign traffic
benign = pd.DataFrame({
    "duration": np.random.exponential(scale=2.0, size=N),
    "src_bytes": np.random.normal(loc=300, scale=50, size=N).astype(int),
    "dst_bytes": np.random.normal(loc=300, scale=50, size=N).astype(int),
    "packet_count": np.random.poisson(lam=20, size=N),
    "label": 0,
})
# malicious traffic (port scans etc.)
malicious = pd.DataFrame({
    "duration": np.random.exponential(scale=0.5, size=N),
    "src_bytes": np.random.normal(loc=1000, scale=200, size=N).astype(int),
    "dst_bytes": np.random.normal(loc=100, scale=30, size=N).astype(int),
    "packet_count": np.random.poisson(lam=50, size=N),
    "label": 1,
})

data = pd.concat([benign, malicious], ignore_index=True)
# ensure non‑negative bytes
for col in ["src_bytes", "dst_bytes"]:
    data[col] = data[col].clip(lower=0)

output_path = "data/processed/features.csv"
data.to_csv(output_path, index=False)
print(f"Synthetic data written to {output_path}, shape={data.shape}")
