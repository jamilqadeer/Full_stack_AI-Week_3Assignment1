# real_estate_numpy.py
import pandas as pd
import numpy as np

#  local file
CSV = "RealEstate-USA.csv"

#  or paste raw GitHub URL here
CSV = "https://raw.githubusercontent.com/ShahzadSarwar10/Fullstack-WITH-AI-B-3-SAT-SUN-6Months-Explorer/refs/heads/main/DataSetForPractice/RealEstate-USA.csv"

df = pd.read_csv(CSV)
print("Columns available:", list(df.columns))

# expected columns:
wanted = ["brokered_by","price","acre_lot","city","house_size"]
# check names (if CSV header is different, see output and adjust)
for w in wanted:
    if w not in df.columns:
        print("Warning: column not found ->", w)

# convert numeric columns safely
df["price"] = pd.to_numeric(df.get("price"), errors="coerce")
df["house_size"] = pd.to_numeric(df.get("house_size"), errors="coerce")
df["acre_lot"] = pd.to_numeric(df.get("acre_lot"), errors="coerce")

# numpy arrays
brokered_by = df["brokered_by"].to_numpy()
price = df["price"].to_numpy()
acre_lot = df["acre_lot"].to_numpy()
city = df["city"].to_numpy()
house_size = df["house_size"].to_numpy()

print("\nSample (first 8 rows):")
print("brokered_by:", brokered_by[:8])
print("price:", price[:8])
print("acre_lot:", acre_lot[:8])
print("city:", city[:8])
print("house_size:", house_size[:8])
