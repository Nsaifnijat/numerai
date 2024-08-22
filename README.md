# numerai
Project Overview

This project is designed to perform financial modeling using the LightGBM algorithm for regression tasks. The project integrates data from Numerai's API to build and evaluate predictive models. The model is built using the LightGBM framework, which is known for its efficiency and accuracy in handling large datasets with high dimensionality.

Features

LightGBM Regressor

LightGBM (LGBMRegressor): This is a highly efficient and scalable gradient boosting framework that uses tree-based learning algorithms. It is optimized for high performance and low memory usage, making it ideal for financial modeling.
Numerai API Integration
NumerAPI (numerapi): Numerai is a data science competition platform focused on financial data. This project uses the NumerAPI to fetch the latest datasets and upload predictions directly to Numerai.
Garbage Collection
gc (gc): The garbage collection module is utilized to manage memory effectively during the training process, ensuring that unnecessary data does not clog memory resources.
