roads = [
    {"id": "FG",          "distance_km": 0.5, "current_density": 60,  "past_density": 50,  "weightage": 0.5},
    {"id": "GB",          "distance_km": 0.5, "current_density": 80,  "past_density": 70,  "weightage": 0.5},
    {"id": "BD (School)", "distance_km": 0.5, "current_density": 180, "past_density": 150, "weightage": 0.8},
    {"id": "DP",          "distance_km": 0.5, "current_density": 70,  "past_density": 60,  "weightage": 0.5},
    {"id": "FH",          "distance_km": 0.8, "current_density": 60,  "past_density": 50,  "weightage": 0.5},
    {"id": "HM",          "distance_km": 0.8, "current_density": 80,  "past_density": 70,  "weightage": 0.5},
    {"id": "MN",          "distance_km": 0.8, "current_density": 50,  "past_density": 40,  "weightage": 0.5},
    {"id": "NP",          "distance_km": 0.8, "current_density": 70,  "past_density": 60,  "weightage": 0.5},
]

def estimated_density(road):
    w = road["weightage"]
    return w * road["current_density"] + (1 - w) * road["past_density"]

print(f"{'Road ID':<14} {'Distance (km)':<15} {'Current Density':<17} {'Past Density':<14} {'Weightage':<11} {'Estimated Density'}")
print("-" * 80)
for road in roads:
    est = estimated_density(road)
    print(f"{road['id']:<14} {road['distance_km']:<15} {road['current_density']:<17} {road['past_density']:<14} {road['weightage']:<11} {est}")
