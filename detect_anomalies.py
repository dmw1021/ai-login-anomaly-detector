from pathlib import Path
import pandas as pd
from sklearn.ensemble import IsolationForest

INPUT = Path('data/login_events.csv')
OUTPUT = Path('reports/flagged_logins.csv')
features = ['hour', 'failed_attempts', 'new_ip', 'country_mismatch']

df = pd.read_csv(INPUT)
missing = set(features + ['event_id', 'username']) - set(df.columns)
if missing:
    raise ValueError(f'Missing required columns: {sorted(missing)}')
if df[features].isna().any().any():
    raise ValueError('Input contains missing feature values')

model = IsolationForest(n_estimators=100, contamination=0.05, random_state=42)
df['prediction'] = model.fit_predict(df[features])
df['anomaly_score'] = model.decision_function(df[features])
flagged = df[df['prediction'] == -1].sort_values('anomaly_score')
OUTPUT.parent.mkdir(exist_ok=True)
flagged.to_csv(OUTPUT, index=False)
print(f'Analyzed {len(df)} events; flagged {len(flagged)} for review.')
print(f'Report saved to {OUTPUT}')
print(flagged.head(10).to_string(index=False))
