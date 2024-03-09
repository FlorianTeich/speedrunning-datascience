import pandas as pd
from pyspark.sql import Column
from pyspark.sql import DataFrame as SparkDataFrame
from pyspark.sql.functions import regexp_replace
from pyspark.sql.types import DoubleType
from sklearn.ensemble import RandomForestClassifier


def create_dataset() -> pd.DataFrame:
    # Create a classification dataset via scikit learn and save it as a parquet file
    from sklearn.datasets import make_classification

    X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)
    df = pd.DataFrame(X, columns=[f'feature_{i}' for i in range(20)])
    df['target'] = y

    return df


def preprocess_data(data: SparkDataFrame) -> SparkDataFrame:
    return data


def assign_split(data: SparkDataFrame, seed: int = 42,
                 train_ratio:float = 0.7,
                 val_ratio:float = 0.15,
                 test_ratio:float = 0.15) -> SparkDataFrame:
    assert train_ratio + val_ratio + test_ratio == 1.0, "Ratios should sum to 1"

    from pyspark.sql.functions import rand, when, col

    data = data.withColumn("rand", rand(seed))
    data = data.withColumn("split", 
                           when(data["rand"] <= train_ratio, "train")
                           .otherwise(
                               when(data["rand"] <= train_ratio + val_ratio, "val")
                               .otherwise("test")
                           ))
    data = data.drop("rand")
    
    return data.where(col("split") == "train").drop("split"), \
        data.where(col("split") == "val").drop("split"), \
        data.where(col("split") == "test").drop("split")

def train_classifier(train_data: SparkDataFrame,
                     val_data: SparkDataFrame,
                     test_data: SparkDataFrame) -> RandomForestClassifier:
    # Train a classifier using train_data and validate it using val_data
    # Then test it using test_data
    from sklearn.metrics import accuracy_score

    X_train = train_data.toPandas().drop("target", axis=1)
    y_train = train_data.toPandas()["target"]

    #X_val = val_data.toPandas().drop("target", axis=1)
    #y_val = val_data.toPandas()["target"]

    #X_test = test_data.toPandas().drop("target", axis=1)
    #y_test = test_data.toPandas()["target"]

    clf = RandomForestClassifier(random_state=42)
    clf.fit(X_train, y_train)

    #y_pred = clf.predict(X_val)
    #val_accuracy = accuracy_score(y_val, y_pred)

    return clf
