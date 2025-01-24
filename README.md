# Cloud-Project--Time-series-Forecasting
No-Code Stock Price Prediction with Amazon SageMaker Canvas
Objective:
Build a time-series model to predict stock prices for Tesla and NVIDIA using Yahoo Finance data, and visualize predictions with Amazon QuickSight.

Tools Used:

Amazon SageMaker Canvas
Amazon QuickSight
Amazon S3
Steps:

Prepare Dataset:

Set up SageMaker domain and IAM roles.
Download and clean historical stock data (e.g., for AAPL) from Nasdaq.
Upload the data to S3.
Build the Model in SageMaker Canvas:

Launch Canvas, import the data, and configure the model to predict MarketClose using Date and Ticker.
Train the model using a quick or standard build.
Generate Predictions:

Evaluate the model's accuracy and generate 30-day probabilistic forecasts (P10, P50, P90).
Visualize with QuickSight:

Create a dataset in QuickSight with the forecast results.
Build a line chart to display the predictions, excluding non-working days and zero values.
Conclusion:
This project shows how no-code tools like SageMaker Canvas and QuickSight can be used to easily build and visualize stock price predictions.
