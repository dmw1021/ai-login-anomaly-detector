import numpy as np
import pandas as pd
from pathlib import Path

rng = np.random.default_rng(42)
rows = []
for i in range(500):
    unusual = i >= 475
    hour = int(rng.choice([0, 1, 2, 3, 23])) if unusual else int(rng.integers(8, 19))
    failures = int(rng.integers(8, 21)) if unusual else int(rng.choice([0, 0, 0, 1, 2]))
    rows.append({"event_id": i + 1, "username": f"employee_{int(rng.integers(1, 31)):02d}", "hour": hour, "failed_attempts": failures, "new_ip": int(rng.random() < (0.85 if unusual else 0.08)), "country_mismatch": int(rng.random() < (0.7 if unusual else 0.02))})
Path('data').mkdir(exist_ok=True)
pd.DataFrame(rows).to_csv('data/login_events.csv', index=False)
print('Created data/login_events.csv with 500 synthetic events')
