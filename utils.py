 # import pandas as pd
 
 # def load_data(path):
 #     """Load CSV and ensure 'quality' column exists."""
 #     df = pd.read_csv(path)
 #     if 'quality' not in df.columns:
 #         raise ValueError("CSV must contain a 'quality' column.")
 #     return df
 
 # def features_and_target(df):
 #     """Return X (features) and y (target)."""
 #     X = df.drop(columns=['quality'])
 #     y = df['quality']
 #     return X, y


```python
import pandas as pd


def load_data(path):
    """Load CSV and ensure 'quality_score' column exists."""
    df = pd.read_csv(path)

    if "quality_score" not in df.columns:
        raise ValueError(
            "CSV must contain a 'quality_score' column."
        )

    return df


def features_and_target(df):
    """Return X (features) and y (target)."""

    feature_columns = [
        "fixed_acidity_scaled",
        "volatile_acidity_scaled",
        "citric_acid_scaled",
        "residual_sugar_grams",
        "free_sulfur_dioxide",
        "total_sulfur_dioxide",
        "alcohol_pct_scaled",
    ]

    missing_features = [
        feature
        for feature in feature_columns
        if feature not in df.columns
    ]

    if missing_features:
        raise ValueError(
            f"Missing feature columns: {missing_features}"
        )

    X = df[feature_columns]
    y = df["quality_score"]

    return X, y
```
