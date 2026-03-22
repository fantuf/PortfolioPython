# Wine Quality Analysis

Interactive analysis of wine quality based on chemical and physical properties, with 3D data visualization powered by Plotly and Streamlit.

## Description

This project explores a dataset of 21,000 wine samples, each described by 12 attributes: fixed acidity, volatile acidity, citric acid, residual sugar, chlorides, free and total sulfur dioxide, density, pH, sulphates, alcohol, and a quality score.

The analysis focuses on the relationship between **pH**, **total sulfur dioxide**, and **wine quality**:

- **pH** — Represents the acidity level, a key factor in flavor and preservation. Wines with balanced pH levels tend to have better taste and longevity.
- **Total Sulfur Dioxide** — Measures SO₂ levels, a common preservative in wine. Excessive amounts can negatively affect aroma and taste, while insufficient levels may lead to spoilage.

## Features

- Balanced dataset reduction via stratified sampling across quality classes
- Interactive 3D scatter plot (quality vs pH vs total sulfur dioxide)
- Web interface powered by Streamlit

## Requirements

- Python 3.8+
- Dependencies listed in `requirements.txt`:

```
pandas
numpy
matplotlib
plotly
streamlit
```

## Installation

```bash
git clone https://github.com/<your-username>/wine-quality-analysis.git
cd wine-quality-analysis
pip install -r requirements.txt
```

## Usage

```bash
streamlit run wine_analysis2.py
```

The application will open in your browser displaying an interactive 3D chart. You can rotate, zoom, and explore quality clusters.

## Project Structure

```
.
├── wine_analysis2.py      # Main script with analysis and visualization
├── wine_data.csv           # Dataset (21,000 samples)
├── requirements.txt        # Python dependencies
└── README.md
```

## Dataset

The `wine_data.csv` file contains the following columns:

| Column | Description |
|---|---|
| `fixed_acidity` | Fixed acidity |
| `volatile_acidity` | Volatile acidity |
| `citric_acid` | Citric acid |
| `residual_sugar` | Residual sugar |
| `chlorides` | Chlorides |
| `free_sulfur_dioxide` | Free SO₂ |
| `total_sulfur_dioxide` | Total SO₂ |
| `density` | Density |
| `pH` | pH |
| `sulphates` | Sulphates |
| `alcohol` | Alcohol |
| `quality` | Quality score |

## License

This project is licensed under the MIT License.
