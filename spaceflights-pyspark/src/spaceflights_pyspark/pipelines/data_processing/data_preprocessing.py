from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    preprocess_data,
    assign_split
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=preprocess_data,
                inputs="raw_data@spark",
                outputs="preprocessed@spark",
                name="preprocess_data",
            ),
            node(
                func=assign_split,
                inputs=["preprocessed@spark",
                        "params:seed",
                        "params:train_ratio",
                        "params:val_ratio",
                        "params:test_ratio"],
                outputs=["preprocessed_train@spark",
                         "preprocessed_val@spark",
                         "preprocessed_test@spark"],
                name="assign_split",
            ),
        ]
    )
