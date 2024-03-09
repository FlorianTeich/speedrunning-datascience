from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    archive
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=archive,
                inputs="params:mlflow_uri",
                outputs="log",
                name="archive",
            ),
        ]
    )
