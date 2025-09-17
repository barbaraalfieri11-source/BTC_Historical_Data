
# BTC_Historical_Data

This repository contains historical **Bitcoin (BTC/USD) hourly candles** from 2015 to 2025,
downloaded using the **Kraken exchange API** via the `ccxt` Python library.

## Dataset
- **File**: `btc_1h.csv`
- **Frequency**: 1 hour (OHLCV: open, high, low, close, volume)
- **Period**: January 2015 – September 2025
- **Rows**: ~93,900
- **Source**: [Kraken](https://www.kraken.com/) (via API)

## Usage
Load the dataset in Python with Pandas:

```python
import pandas as pd

df = pd.read_csv("btc_1h.csv", parse_dates=["timestamp"])
print(df.head())

