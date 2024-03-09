from kedro.pipeline import Pipeline, node, pipeline

from .nodes import (
    create_dataset,
)


def create_pipeline(**kwargs) -> Pipeline:
    return pipeline(
        [
            node(
                func=create_dataset,
                inputs=[],
                outputs="raw_data@pandas",
                name="create_dataset",
            ),
        ]
    )
