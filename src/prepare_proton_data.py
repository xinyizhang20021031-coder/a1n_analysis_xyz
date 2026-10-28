# prepare_proton_data.py


import pandas as pd
import numpy as np

# 1. Load the original data
df = pd.read_csv(
    "data/webdata_2026_g1F1p/webdata_2026_proton/1_smc_HEPData-ins471981-v1-Table_1.csv",
    comment="#"
)
# df = pd.read_csv("data/webdata_2026_g1F1p/webdata_2026_proton/1_smc_HEPData-ins471981-v1-Table_1.csv")
# print(df.columns.tolist())

# 2. Create a proton-specific/neutron-specific dataframe
proton = pd.DataFrame()
# neutron = pd.DataFrame()

proton["X"] = df["X"]
proton["X.low"] = df["X LOW"]
proton["X.high"] = df["X HIGH"]
proton["Q2"] = df["MEAN(NAME=Q**2) [GEV**2]"]
proton["G1F1"] = df["ASYM(NAME=A1)"]

proton["G1F1.stat"] = df["stat +"]
proton["G1F1.sys"] = df["sys +"]

# neutron["X"] = df["X"]
# neutron["Q2"] = df["Q**2[GeV**2.]"]
# neutron["G1F1"] = df["g1n/F1n"]

# neutron["G1F1.stat"] = df["stat.1"]
# neutron["G1F1.sys"] = df["sys.1"]

# 3. Total error
proton["G1F1.err"] = np.sqrt(
    proton["G1F1.stat"]**2
    + proton["G1F1.sys"]**2
)

# neutron["G1F1.err"] = np.sqrt(
#     neutron["G1F1.stat"]**2
#     + neutron["G1F1.sys"]**2
# )

# 4. Save new dataframe to CSV
proton.to_csv(
    "data/webdata_2026_g1F1p/1_smc_HEPData-ins471981-v1-Table_1_proton.csv",
    index=False
)

# neutron.to_csv(
#     "../data/5_e155_PLB493_2000_19_neutron.csv",
#     index=False
# )

print(proton.head())
print("Saved to data/webdata_2026_g1F1p/1_smc_HEPData-ins471981-v1-Table_1_proton.csv")

# print(neutron.head())
# print("Saved to data/5_e155_PLB493_2000_19_neutron.csv")
