
import requests, pandas as pd, time
from tqdm.auto import tqdm

url = "https://min-api.cryptocompare.com/data/v2/histohour"
params = {"fsym":"BTC","tsym":"USD","limit":2000}  # 2000h per page (~83 days)
headers = {"authorization": f"Apikey {API_KEY}"}

all_rows = []
toTs = int(pd.Timestamp.now(tz="UTC").timestamp())

with tqdm(desc="Scarico BTC/USD 1h (CryptoCompare)") as bar:
    while True:
        r = requests.get(url, params={**params, "toTs": toTs}, headers=headers, timeout=30)
        r.raise_for_status()
        data = r.json()["Data"]["Data"]
        if not data: break
        all_rows.extend(data)
        bar.update(len(data))
        toTs = data[0]["time"] - 1
        if toTs < int(pd.Timestamp("2015-01-01", tz="UTC").timestamp()):
            break
        time.sleep(0.2)

df = pd.DataFrame(all_rows)
df["timestamp"] = pd.to_datetime(df["time"], unit="s", utc=True)
df = df.rename(columns={"volumefrom":"volume"})
df = df[["timestamp","open","high","low","close","volume"]].astype({
    "open":float,"high":float,"low":float,"close":float,"volume":float
}).drop_duplicates("timestamp").sort_values("timestamp").reset_index(drop=True)

df.to_csv("btc_1h.csv", index=False)
print(f"✅ Save {len(df):,} rows in btc_1h.csv")
