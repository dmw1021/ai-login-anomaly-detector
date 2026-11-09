
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load the login events analyzed by our AI model
data = pd.read_csv("data/login_events.csv")
flagged = pd.read_csv("reports/flagged_logins.csv")

# Separate normal and anomalous login events
normal = data[~data["event_id"].isin(flagged["event_id"])]

# Create the visualization
plt.figure(figsize=(10, 6))

plt.scatter(
    normal["hour"],
    normal["failed_attempts"],
    color="steelblue",
    alpha=0.5,
    label="Normal Login Activity"
)

plt.scatter(
    flagged["hour"],
    flagged["failed_attempts"],
    color="red",
    alpha=0.8,
    label="AI-Flagged Anomalies"
)

plt.xlabel("Login Hour (24-Hour Clock)")
plt.ylabel("Number of Failed Login Attempts")
plt.title("AI-Powered Login Anomaly Detection")
plt.legend()
plt.grid(alpha=0.3)

# Save the chart for GitHub
Path("reports").mkdir(exist_ok=True)
plt.savefig("reports/anomaly_visualization.png", dpi=300)
plt.show()
