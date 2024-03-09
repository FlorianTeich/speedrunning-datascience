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

```
