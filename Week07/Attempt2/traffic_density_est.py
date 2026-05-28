import os
import random
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

ROUTE1 = [
    {"id": "FG",          "distance_km": 0.5, "is_school": False},
    {"id": "GB",          "distance_km": 0.5, "is_school": False},
    {"id": "BD (School)", "distance_km": 0.5, "is_school": True},
    {"id": "DP",          "distance_km": 0.5, "is_school": False},
]

ROUTE2 = [
    {"id": "FH", "distance_km": 0.8, "is_school": False},
    {"id": "HM", "distance_km": 0.8, "is_school": False},
    {"id": "MN", "distance_km": 0.8, "is_school": False},
    {"id": "NP", "distance_km": 0.8, "is_school": False},
]


SCHOOL_RUSH_HOURS = {7, 8, 9, 15, 16, 17, 18}


def get_weightage(is_school, hour):
    if is_school:
        if hour in SCHOOL_RUSH_HOURS:
            return round(random.uniform(0.75, 0.95), 2)   # rush: high congestion weighting
        return round(random.uniform(0.5, 0.75), 2)        # off-peak school zone
    return round(random.uniform(0.4, 0.5), 2)


def get_density(is_school, hour):
    if is_school:
        if hour in SCHOOL_RUSH_HOURS:
            v = random.randint(150, 250)                   # rush: heavy school traffic
        else:
            v = random.randint(90, 150)                    # off-peak school zone
        return v, random.randint(90, 150)                  # past always off-peak baseline
    return random.randint(35, 95), random.randint(35, 95)


def estimated_density(current, past, weightage):
    return round(weightage * current + (1 - weightage) * past, 2)


def generate_route_set(roads, hour):
    result = []
    for road in roads:
        current, past = get_density(road["is_school"], hour)
        w = get_weightage(road["is_school"], hour)
        est = estimated_density(current, past, w)
        result.append({**road, "current_density": current, "past_density": past,
                        "weightage": w, "estimated_density": est})
    return result


# --- Generate 24 hourly sets ---
hours = list(range(24))
route1_totals = []
route2_totals = []
choices = []
all_sets = []

for h in hours:
    r1 = generate_route_set(ROUTE1, h)
    r2 = generate_route_set(ROUTE2, h)
    t1 = round(sum(seg["estimated_density"] for seg in r1), 2)
    t2 = round(sum(seg["estimated_density"] for seg in r2), 2)
    chosen = 1 if t1 <= t2 else 2
    route1_totals.append(t1)
    route2_totals.append(t2)
    choices.append(chosen)
    all_sets.append({"hour": h, "route1": r1, "route2": r2,
                     "total1": t1, "total2": t2, "choice": chosen})

# --- Display one sample set (first rush hour: 07:00) ---
sample = all_sets[7]
print(f"\n{'='*80}")
print(f"  SAMPLE DATA  —  Hour {sample['hour']:02d}:00")
print(f"{'='*80}")
header = f"{'Road ID':<14} {'Dist (km)':<11} {'Current':<10} {'Past':<10} {'Weightage':<11} {'Est. Density'}"
print(f"\n  ROUTE 1")
print(f"  {header}")
print(f"  {'-'*70}")
for seg in sample["route1"]:
    print(f"  {seg['id']:<14} {seg['distance_km']:<11} {seg['current_density']:<10} "
          f"{seg['past_density']:<10} {seg['weightage']:<11} {seg['estimated_density']}")
print(f"  {'':>57} Total: {sample['total1']:.2f}")

print(f"\n  ROUTE 2")
print(f"  {header}")
print(f"  {'-'*70}")
for seg in sample["route2"]:
    print(f"  {seg['id']:<14} {seg['distance_km']:<11} {seg['current_density']:<10} "
          f"{seg['past_density']:<10} {seg['weightage']:<11} {seg['estimated_density']}")
print(f"  {'':>57} Total: {sample['total2']:.2f}")

print(f"\n  >>> Route {sample['choice']} is chosen (lower estimated density) <<<")
print(f"{'='*80}\n")

# --- y = mx + b  Breakdown ---
print(f"{'='*80}")
print(f"  FORMULA BREAKDOWN  —  y = mx + b  —  Hour {sample['hour']:02d}:00")
print(f"  where  x = Current Density,  m = Weightage (coefficient),")
print(f"         b = (1 - m) x Past Density (intercept),  y = Estimated Density")
print(f"{'='*80}")
col = f"  {'Road ID':<14} {'m (Coeff.)':<13} {'b (Intercept)':<16} {'Equation':<34} {'y (Est.)'}"
sep = f"  {'-'*78}"
for label, segs in [("ROUTE 1", sample["route1"]), ("ROUTE 2", sample["route2"])]:
    print(f"\n  {label}")
    print(col)
    print(sep)
    for seg in segs:
        m = seg["weightage"]
        b = round((1 - m) * seg["past_density"], 2)
        x = seg["current_density"]
        y = seg["estimated_density"]
        eq = f"Est = {m} x {x} + {b}"
        print(f"  {seg['id']:<14} {m:<13} {b:<16} {eq:<34} {y}")
print(f"\n{'='*80}")
print(f"  Coefficient (m) = Weightage     — how much trust is given to the live reading")
print(f"  Intercept   (b) = (1-m) x Past  — the baseline carried forward from history")
print(f"{'='*80}\n")

# --- Two-line graph ---
fig, ax = plt.subplots(figsize=(14, 6))

ax.plot(hours, route1_totals, marker='o', linewidth=2,
        color='steelblue', label='Route 1  (FG → GB → BD → DP)')
ax.plot(hours, route2_totals, marker='s', linewidth=2,
        color='tomato', label='Route 2  (FH → HM → MN → NP)')

# Shade rush-hour bands (behind everything else)
for h in SCHOOL_RUSH_HOURS:
    ax.axvspan(h - 0.5, h + 0.5, alpha=0.12, color='orange', zorder=0)

# Shade background to show which route is chosen each hour
for h in hours:
    color = 'steelblue' if choices[h] == 1 else 'tomato'
    ax.axvspan(h - 0.5, h + 0.5, alpha=0.08, color=color)

# Mark the chosen point at each hour
for h in hours:
    y = route1_totals[h] if choices[h] == 1 else route2_totals[h]
    ax.plot(h, y, marker='*', markersize=12,
            color='gold', zorder=5, markeredgecolor='black', markeredgewidth=0.5)

r1_patch   = mpatches.Patch(color='steelblue', label='Route 1  (FG → GB → BD → DP)')
r2_patch   = mpatches.Patch(color='tomato',    label='Route 2  (FH → HM → MN → NP)')
star       = plt.Line2D([0], [0], marker='*', color='w', markerfacecolor='gold',
                        markeredgecolor='black', markersize=12, label='Chosen route')
rush_patch = mpatches.Patch(color='orange', alpha=0.4, label='School rush hours (7–9, 15–18)')

ax.set_xlabel('Hour of Day', fontsize=12)
ax.set_ylabel('Total Estimated Density', fontsize=12)
ax.set_title('Route 1 vs Route 2 — Estimated Traffic Density over 24 Hours', fontsize=14)
ax.set_xticks(hours)
ax.set_xticklabels([f"{h:02d}:00" for h in hours], rotation=45, ha='right', fontsize=8)
ax.legend(handles=[r1_patch, r2_patch, star, rush_patch], loc='upper right')
ax.grid(True, alpha=0.3)

save_path = os.path.join(os.path.dirname(__file__), "images", "route_comparison.png")

plt.tight_layout()
plt.savefig(save_path, dpi=150)
print(f"Graph saved as {save_path}")
plt.show()
