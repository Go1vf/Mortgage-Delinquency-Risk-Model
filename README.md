# Mortgage Delinquency Prediction Model

## Overview
This project develops predictive models to estimate the probability of mortgage delinquency exceeding 90 days within two years. Utilizing the Fannie Mae Single-Family Mortgage dataset, the model aims to provide accurate predictions to aid in risk assessment and management in the financial sector.

## Dataset
The analysis uses the Fannie Mae Single-Family Mortgage dataset covering the periods:
- **Training Period**: 2015 Q1 to 2019 Q4
- **Testing Period**: 2022 Q1 to 2023 Q4

The dataset includes 110 features with over 100 million payment records, focusing on a critical subset of data where default rates are approximately 1%.

## Features
After extensive Exploratory Data Analysis (EDA) involving correlation matrices and data distribution examination, the feature set was refined to 15 critical predictors by eliminating variables that were either missing significant data or were highly correlated.

## Models and Performance
- **XGBoost**: Initially implemented to handle the imbalanced dataset, enhancing the recall rate from 64% to 80% compared to traditional logistic regression approaches.
- **LSTM**: A Long Short-Term Memory model was employed for its proficiency in time-series analysis, which after hyperparameter tuning via grid search, outperformed the XGBoost model by achieving an 87% recall rate.

## Requirements
To run the code, you will need Python 3.8 or later, with the following packages:
- numpy
- pandas
- scikit-learn
- xgboost
- keras
- tensorflow

## Installation
Clone this repository and install the required Python packages using:
```bash
git clone https://your-repository-link.git
cd Mortgage-Delinquency-Prediction
conda env create -f environment.yml
conda activate mortgage-delinquency-prediction
