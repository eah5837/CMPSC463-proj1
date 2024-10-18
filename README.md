Large-Scale Financial Data Analysis & Trend Detection

Project Overview

This project develops a system to analyze large financial datasets such as stock prices or cryptocurrency data to detect patterns, trends, and anomalies. It uses divide-and-conquer algorithms to efficiently process time-series financial data, enabling users to make data-driven decisions.

Key functionalities include:

	•	Sorting financial data using merge sort.
	•	Detecting the period of maximum gain or loss using Kadane’s algorithm (maximum subarray problem).
	•	Identifying anomalies (e.g., irregular price spikes) using the closest pair of points algorithm.

Features

	•	Merge Sort: Efficient sorting of financial data (e.g., by timestamps).
	•	Kadane’s Algorithm: Identify periods of maximum gain/loss in stock or cryptocurrency prices.
	•	Anomaly Detection: Detect anomalies in financial transactions or price data.
	•	Visualization: Generate graphs showing stock price trends, maximum gain periods, and detected anomalies.

File Structure

├── DataSorter.py          # Class for sorting the financial data
├── MaxSubarray.py         # Class for detecting maximum gain/loss period
├── AnomalyDetector.py     # Class for detecting anomalies using closest pair of points
├── main.py                # Main script to run the system and visualize results
├── README.md              # Project documentation
├── requirements.txt       # Dependencies for the project (e.g., matplotlib)
└── /data                  # Sample datasets (toy example data)


How to Run the Project

Prerequisites

	•	Python 3.x
	•	Install required packages by running:

pip install -r requirements.txt

Running the Code

	1.	Load the dataset: Add your financial data (stock prices, transaction logs, etc.) to the /data folder. Ensure the data is in the format of a list of tuples, where each tuple contains a timestamp and a price/transaction volume.
	2.	Run the system: Execute the following command to run the main script:

python main.py
	3.	Visualize Results: The system will generate visualizations that show:
	•	The stock price trend over time.
	•	The period of maximum gain or loss.
	•	Detected anomalies (e.g., unusual price spikes).

System Components

1. DataSorter:

	•	This class implements the merge sort algorithm to sort financial data based on timestamps, ensuring efficient data analysis.

2. MaxSubarray:

	•	This class implements Kadane’s algorithm to find the period of maximum gain or loss within the dataset.

3. AnomalyDetector:

	•	This class uses the closest pair of points algorithm to detect anomalies in financial data, such as irregular price fluctuations or suspicious trades.

Verification

The system has been tested with a synthetic dataset of stock prices. The following features were verified:

	•	Correct sorting of financial data by timestamp.
	•	Accurate identification of the period of maximum gain/loss.
	•	Detection of anomalies (price spikes or dips) in the dataset.

Sample Output

	•	Stock Price Trend with Maximum Gain and Anomalies:

Discussion

	•	Findings: The system successfully detected periods of maximum growth or loss in stock prices, as well as anomalies like sharp price changes. This can help identify investment opportunities or fraudulent activities.
	•	Challenges: Handling larger datasets efficiently, though the divide-and-conquer approach offers scalability.
	•	Future Improvements: Extend the anomaly detection algorithm to work with multi-dimensional datasets for deeper analysis.

License

This project is licensed under the MIT License.

This README gives an overview of the project, explains how to run it, and summarizes key components. You can customize it further with more details on the dataset you’re using and include a sample graph screenshot under Sample Output.

