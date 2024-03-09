from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    train_classifier,
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=train_classifier,
                inputs=["preprocessed_train@spark",
                         "preprocessed_val@spark",
                         "preprocessed_test@spark"],
                outputs="model",
                name="train_classifier",
            ),
        ]
    )
