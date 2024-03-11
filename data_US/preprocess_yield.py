import os
import pandas as pd

data_path = os.path.join("data_US", "county_data")
yield_csv = os.path.join(data_path, "YIELD_COUNTY_US.csv")

yield_df = pd.read_csv(yield_csv, header=0)
# convert yield from bushels/acre to t/ha
# See https://www.ndwheat.com/buyers/chartsandstats/
yield_df["yield"] = 0.06725 * yield_df["yield"]
yield_df["yield"] = yield_df["yield"].round(3)
print(yield_df.head(5).to_string())

yield_df.to_csv(yield_csv, index=False)

yield_df = pd.read_csv(yield_csv, header=0)
print(yield_df.head(5).to_string())
