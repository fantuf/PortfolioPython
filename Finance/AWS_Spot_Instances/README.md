# AWS Spot Pricing Analysis and ROI Forecast for ML/AI Workloads

## Objective

This project analyzes historical AWS Spot Instance pricing data to help ML/AI teams **cut cloud infrastructure costs** without sacrificing performance. It compares Spot vs On-Demand pricing for `r3.xlarge` Linux instances in the EU-West-1 (Ireland) region, forecasts future prices using time series models, and quantifies the potential ROI of switching to Spot Instances.

## Business Question

> *"How much can an ML/AI team save by using AWS Spot Instances instead of On-Demand, and how predictable are Spot prices over the next 30 days?"*

## Dataset

| Column | Description |
|---|---|
| `datetime` | Timestamp of the recorded Spot price (UTC) |
| `instance_type` | EC2 instance type — analysis focuses on `r3.xlarge` |
| `os` | Operating system — filtered to `Linux/UNIX` |
| `region` | AWS Availability Zone within `eu-west-1` (Ireland) |
| `price` | Spot price in USD per hour |

Source: AWS Spot pricing feed (`eu-west-1.csv`).

## Project Structure

```
├── AWS_Spot_Instances.ipynb   ← Full analysis notebook (run end-to-end)
├── eu-west-1.csv              ← Raw pricing dataset
└── README.md
```

## Analysis Pipeline

The notebook is organized into four sequential sections:

### 1 · Data Exploration & Preprocessing
- Column naming, type casting, null-value audit.
- Datetime parsing and timezone handling.
- Filtering to `r3.xlarge` + `Linux/UNIX` for a clean ML-relevant subset.

### 2 · Time Series Analysis
- **Hourly resampling** of raw price ticks into a regular time series.
- **Seasonal decomposition** (additive, period = 24 h) to isolate trend, seasonality, and residual components.
- **ACF / PACF** plots (24 lags) to identify autocorrelation structure and guide model selection.
- **ADF stationarity test** to confirm whether differencing is needed.

### 3 · Forecasting Models
| Model | Purpose |
|---|---|
| **ARIMA (6,0,2)** | Classical parametric forecast — captures short-range autocorrelation without differencing (series is stationary). |
| **Prophet** | Bayesian additive model with daily seasonality enabled — produces a 30-day hourly price forecast with uncertainty intervals. |

### 4 · ROI Estimation
Compares forecasted Spot prices against the fixed On-Demand rate to quantify hourly and monthly savings for ML/AI workloads.

## Key Technical Skills Demonstrated

- **Time Series Modeling** — decomposition, stationarity testing, ARIMA, Prophet
- **Exploratory Data Analysis** — resampling, filtering, visualization with Matplotlib
- **Cloud Cost Optimization** — translating statistical output into actionable infrastructure savings
- **Python Data Stack** — Pandas, Statsmodels, Prophet, Matplotlib

## Requirements

```
pandas
matplotlib
statsmodels
prophet
```

Install with:

```bash
pip install pandas matplotlib statsmodels prophet
```

## How to Run

1. Place `eu-west-1.csv` in the same directory as the notebook.
2. Open `AWS_Spot_Instances.ipynb` in Jupyter / VS Code / Colab.
3. Run all cells sequentially — no configuration needed.
