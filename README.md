# speedrunning-datascience

Abstract: Lets try to fuse concepts of speedrunning and data science!
The goal of this repo is to create a documentation of goals, best practices and methods to very quickly write production-ready code related to data science or machine learning.

## First goals:

* The task is to use some training data to train a classier and evaluate its performance on a given test split of the data
* The code needs to be executable
* The experiment of training a classifier and preprocessing the data needs to be reproducable
* The code needs to be deployable in a short amount of time and with only minor changes to the code base if any (this is super ambiguous formulation, lets revisit it later on in order to specifiy it better)

## Steps taken:

```bash
poetry init
poetry add kedro
poetry shell
kedro new --starter=spaceflights-pyspark
cd spaceflight-pyspark
pip install -f requirements.txt
```

* remove documentation at the beginning of conf/base/catalog.yaml
* remove conf/base/parameters_data_science.yaml
* remove scr/spaceflights_pyspark/pipelines/data_science
* switch to scr/spaceflights_pyspark/pipelines/data_pipelines/nodes.py and remove all functions
    * declare first function "create_dataset()"
* modify the scr/spaceflights_pyspark/pipelines/data_pipelines/pipeline.py:
    * removed a lot of nodes except for one
    * edited the sindle node in order to reference our create_dataset function as well as a "raw"-parquet catalog entry
    * rename the pipeline.py to "create_dataset.py"
    * editing the __init__.py file in order to reference the renamed create_dataset.py
* removing csv files from /data/01_raw
* run ```kedro run``` to test our pipeline
* edit .gitignore in order to ignore parquet, json and csv files
