# Import necessary libraries and modules
from pre_training import preprocess_data
from autogluon.tabular import TabularPredictor
import os
from autogluon.common import space
import autogluon.common as ag

# Preprocess the data
train_processed, test_processed, submission_processed = preprocess_data()

# Define hyperparameters for different model types
hyperparameters = {  
                   'XGB': [{'objective': 'reg:squarederror',  # 'reg:linear' is deprecated
                            'eval_metric': 'rmse', 
                            'max_depth': ag.space.Int(lower=5, upper=9, default=7), 
                            'n_estimators': ag.space.Int(lower=100, upper=500, default=100), 
                            'eta': 0.3, 
                            'subsample': 1,
                            'colsample_bytree': 1}],
                   'GBM': [{'extra_trees': True, 
                            'num_boost_round': ag.space.Int(lower=100, upper=800, default=100),
                            'num_leaves': ag.space.Int(lower=26, upper=66, default=36),  # number of leaves in trees (integer hyperparameter)
                            'ag_args': {'name_suffix': 'XT'}}, {}, 'GBMLarge']
                  }

# Define hyperparameter tuning arguments
hyperparameter_tune_kwargs = { 
                            'num_trials': 15,
                            'scheduler' : 'local',
                            'searcher': 'auto',
                        }

# Fit the TabularPredictor
predictor = TabularPredictor(label='count', eval_metric='root_mean_squared_error').fit(train_data=train_processed,
                                                                                          time_limit=600,
                                                                                          hyperparameters=hyperparameters, 
                                                                                          hyperparameter_tune_kwargs=hyperparameter_tune_kwargs)

# Print fit summary
print(predictor.fit_summary())

# Plot the leaderboard
leaderboard_plot = predictor.leaderboard(silent=True).plot(kind="bar", x="model", y="score_val")

# Save the plot to the "img" directory
img_path = os.path.join("img", "leaderboard_plot.png")
leaderboard_plot.figure.savefig(img_path)

# Make predictions
predictions = predictor.predict(test_processed)

# Print predictions summary
print(f"predictions summary:\n{predictions.describe()}")

# Count the number of negative values in the predictions
num_negative_values = (predictions < 0).sum()

# Print the count of negative values
print("Number of negative values:", num_negative_values)

# Set negative predictions to zero
predictions[predictions < 0] = 0

# Update the "count" column in the submission data frame with the predictions
submission_processed["count"] = predictions

# Save the submission data frame to a CSV file
submission_processed.to_csv("submission.csv", index=False)
