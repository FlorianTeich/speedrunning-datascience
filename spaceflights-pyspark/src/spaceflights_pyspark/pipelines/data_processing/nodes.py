import pandas as pd
from pyspark.sql import Column
from pyspark.sql import DataFrame as SparkDataFrame
from pyspark.sql.functions import regexp_replace
from pyspark.sql.types import DoubleType


def create_dataset() -> pd.DataFrame:
    # Create a classification dataset via scikit learn and save it as a parquet file
    from sklearn.datasets import make_classification

    X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)
    df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(20)])
    df['target'] = y

    return df
