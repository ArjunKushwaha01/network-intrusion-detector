import matplotlib
matplotlib.use('Agg')          # ← non‑interactive backend, works in headless env

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# ---- Build the matrix (use the same numbers you saw in the evaluation) ----
cm = np.array([[200, 0],
               [0, 200]])

# ---- Plot --------------------------------------------------------------
sns.heatmap(cm,
            annot=True,
            fmt='d',
            cmap='Blues',
            xticklabels=['Pred 0', 'Pred 1'],
            yticklabels=['True 0', 'True 1'])

plt.title('Confusion Matrix')
plt.ylabel('True label')
plt.xlabel('Predicted label')

# ---- Save to file -------------------------------------------------------
output_path = 'data/processed/confusion_matrix.png'
plt.savefig(output_path, dpi=150, bbox_inches='tight')
print(f'Confusion‑matrix image written to {output_path}')
