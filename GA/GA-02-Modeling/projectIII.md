# Project III: Modeling I

The goal of this project is to implement the modeling process we have worked towards in class.  You have options for what datasets you want to use,
however the primary goal is to frame, evaluate, and discuss a classification problem using at least Logistic Regression.

### Minimal Requirements

For this assignment, you are to prepare a Jupyter notebook that contains an analysis of a classification problem using Logistic Regression.
The `admissions` dataset provides a baseline example for this.  You are free to find alternative examples.  Regardless of your dataset, your notebook
should do the following:

- Describe the dataset including either an explicit data dictionary (in the case of a smaller dataset) or a link to an original data dictionary
(in the case of a large dataset)
- Explicitly frame your classification problem; what are you measuring and how are you going to understand the quality of your model?
- Describe any data cleaning and feature manipulation prior to model implementation
- Describe any parameter tuning or normalization that took place
- Be sure to use cross-validation in training
- Discuss results on test set
- Describe Accuracy, Precision, Recall, and F1 score of your model
- Plot and interpret the following:
   - Precision and Recall curves together (thresholds vs. probability)
   - Precision vs. Recall
   - ROC curve


### Extra

- Frame and implement a Regression problem in the same dataset
- Use Gradient Descent to compare with closed form solutions
- Use KNearestNeighbors to frame and solve a classification problem in your data; discuss evaluation
