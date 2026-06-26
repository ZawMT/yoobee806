# Clustering Activities

## Activity 1: The Sensor Spoof Attack (Cybersecurity Integrity)

- **Goal:** Detect malicious data injections or sensor tampering in a cooperative transport framework.
- **Setup:** A hacker has breached the C-ITS system and spoofed the data for Road BD (School), causing its traffic density parameters to change from 0.5 to 0.2 for activity parameters. At the same time, its raw Current Rho (w1) spikes massively to 500.
- **Task:** Run all three algorithms on this modified dataset across Excel and Power BI:

| Road ID | Distance (km) (Activity Parameter) | Current Rho (w1) | Past Rho (w2) |
|---|---|---|---|
| FG | 0.5 | 60 | 50 |
| GB | 0.5 | 60 | 70 |
| BD (School) | 0.2 *(Changed from 0.5)* | 500 *(Changed from 180)* | 150 |
| DP | 0.5 | 70 | 60 |
| FH | 0.8 | 60 | 50 |
| HM | 0.8 | 60 | 70 |
| MN | 0.8 | 50 | 40 |
| NP | 0.8 | 70 | 60 |

- **K-Means:** Watch how the single hacked road violently pulls Centroid 2 out of position, distorting the whole network profile.
- **FCM:** Show how the fuzzy membership percentages smoothly drop to zero for normal zones.
- **DBSCAN:** Watch DBSCAN cleanly isolate this spoofed coordinate as an independent red Noise Point, leaving the normal traffic clusters perfectly intact.
- **Lesson:** DBSCAN is the superior tool for network anomaly/intrusion detection because it isolates noise rather than letting outliers corrupt the baseline model.

## Activity 2: The Core Decision-Matrix Challenge

- **Goal:** Evaluate and defend algorithm selection based on operational needs.
- **Team:** Team K-Means, Team Fuzzy, and Team DBSCAN.
- **Task:** An analytical comparison matrix using their real dashboard outputs:

| Performance Metric | K-Means | Fuzzy C-Means | DBSCAN |
|---|---|---|---|
| How it treats Road BD (School) | Forces it into a hard cluster. | Assigns it a 100% heavy membership. | Identifies it cleanly as Noise. |
| How it handles Road GB (Transition) | Forces it into a continuous low-traffic group. | Shows a 9.9% congestion slip. | Groups it in the normal cluster. |
| Best Traffic Use Case | Clear-cut zoning boundaries. | Predicting traffic breakdown onset. | Incident & Accident routing alerts. |

## Activity 3: The Algorithmic Tug-of-War (Boundary Roads)

- **Goal:** Observe how different clustering mathematical definitions handle "edge-case" roads.
- **Setup:** Focus entirely on Road GB and Road DP, which sit right on the border between free-flowing and congested zones.
- **Task:** How these intermediate roads shift definitions across the three visuals:
  - In **K-Means**, it's a hard "Low Traffic" classification (binary).
  - In **FCM**, it reveals a fluid transition (90.1% vs 9.9% shared profile weight).
  - In **DBSCAN**, it is labelled a "Border Point" — part of the cluster, but on the absolute edge of density.
- **Lesson:** Transport engineers use FCM when they need an early warning system for traffic buildup, while they use K-Means for simple data organization.

## Activity 4: Hyperparameter Sensitivity

- **Goal:** Understand how changing mathematical assumptions completely alters transport insights.
- **Task:** Manually alter a single model variable in their Power BI environments and write down the result:
  - **K-Means Challenge:** Change k from 2 to 4. Watch how it fragments the normal traffic group into unnecessary mini-groups.
  - **DBSCAN Challenge:** Change the density radius rule (Epsilon). Watch how setting the radius too large accidentally swallows the school zone anomaly into the normal cluster, blindfolding the system to congestion.

## Activity 5: The Smart City Traffic Control Simulation

- **Goal:** Act as a C-ITS Routing Optimization Engine.
- **Setup:** The class acts as the automated traffic management center for the highway network.
- **Task:** Create a 3-step automated routing playbook using the strengths of all three models combined:
  1. Use **DBSCAN** to constantly filter the incoming raw data stream for immediate emergency sensor alerts (Noise/Accidents).
  2. Use **FCM** to identify roads where the congestion membership is climbing from 5% to 25%, triggering early ramp-metering signals.
  3. Use **K-Means** at the end of the day to generate simple, clean city zoning maps for urban planners.
