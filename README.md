# wine-quality-prediction
Model trained on a linear regression with combined L1 and L2 priors as regularizer to predict wine quality on specific features.

## Workflows
1. Update config.yaml
2. Update schema.yaml [Optional]
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py

# How to run?
 
### Steps:

Clone the repository

```bash
git clone https://github.com/aliakseibrown/wine-quality-prediction.git
```

### STEP 1 - Create a conda environment after opening the repository

```bash
conda create -n wine python=3.8 -y
```

```bash
conda activate wine
```

### STEP 2 - Install the requirements
```bash
pip install -r requirements.txt
```


##### cmd
- mlflow ui

### dagshub
[dagshub](https://dagshub.com/) 

MLFLOW_TRACKING_URI=https://dagshub.com/aliakseibrown/wine-quality-prediction.mlflow \
MLFLOW_TRACKING_USERNAME=aliakseibrown \
MLFLOW_TRACKING_PASSWORD=435491a5b08f4198a561a9bd44fbe9d89f59fa04 \
python script.py

Run this to export as env variables:

```bash
export MLFLOW_TRACKING_URI=https://dagshub.com/aliakseibrown/wine-quality-prediction.mlflow

export MLFLOW_TRACKING_USERNAME=aliakseibrown

export MLFLOW_TRACKING_PASSWORD=435491a5b08f4198a561a9bd44fbe9d89f59fa04

```