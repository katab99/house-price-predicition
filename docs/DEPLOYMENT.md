# Deployment Questions

## What approach would you use to version and track different models in production?

I would use a model registry system to track the versions of models for training and testing with metadata such as training data, and parameters, performance metrics, or deployment information.
To track the performance in production, I would using techniques like shadow deployment, canary deployment or A/B testing.

## What key metrics would you monitor for this API service and the prediction model?

For the API service, I would monitor such as request frequency or response status code if any error accours, or model prediction time.
For the prediction model, I would monitor the model input - output for later data analysis, or any outlier on the output.

## How would you roll back to a previous version if needed?

In the model registry system, older versions of models can be archived, so any time a roll back is needed, previous versions are still available.
