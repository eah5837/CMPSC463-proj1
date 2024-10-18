import random
import matplotlib.pyplot as plt

# Define the merge sort algorithm for time-series sorting
class DataSorter:
    def merge_sort(self, data):
        if len(data) > 1:
            mid = len(data) // 2
            left_half = data[:mid]
            right_half = data[mid:]

            self.merge_sort(left_half)
            self.merge_sort(right_half)

            i = j = k = 0
            while i < len(left_half) and j < len(right_half):
                if left_half[i][0] < right_half[j][0]:
                    data[k] = left_half[i]
                    i += 1
                else:
                    data[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                data[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                data[k] = right_half[j]
                j += 1
                k += 1

        return data

# Kadane's Algorithm for Maximum Subarray
class MaxSubarray:
    def find_max_gain(self, data):
        max_ending_here = max_so_far = data[0][1]
        start = end = s = 0

        for i in range(1, len(data)):
            if data[i][1] > max_ending_here + data[i][1]:
                max_ending_here = data[i][1]
                s = i
            else:
                max_ending_here += data[i][1]

            if max_ending_here > max_so_far:
                max_so_far = max_ending_here
                start = s
                end = i

        return max_so_far, data[start][0], data[end][0]

# Closest Pair of Points for Anomaly Detection
class AnomalyDetector:
    def closest_pair(self, data):
        data = sorted(data, key=lambda x: x[1])
        min_distance = float("inf")
        pair = None

        for i in range(len(data) - 1):
            diff = abs(data[i][1] - data[i + 1][1])
            if diff < min_distance:
                min_distance = diff
                pair = (data[i], data[i + 1])

        return pair, min_distance

# Visualization function for trends and anomalies
def visualize_trends_and_anomalies(data, max_gain_info, anomaly_pair):
    timestamps, prices = zip(*data)

    plt.figure(figsize=(10, 5))
    plt.plot(timestamps, prices, label='Stock Prices', color='blue')

    # Highlight the maximum gain period
    plt.axvspan(max_gain_info[1], max_gain_info[2], color='green', alpha=0.3, label='Max Gain Period')

    # Highlight the anomaly
    anomaly_timestamps = [anomaly_pair[0][0], anomaly_pair[1][0]]
    anomaly_prices = [anomaly_pair[0][1], anomaly_pair[1][1]]
    plt.scatter(anomaly_timestamps, anomaly_prices, color='red', label='Anomaly Detected')

    plt.xlabel('Time')
    plt.ylabel('Price')
    plt.title('Stock Price Trend with Anomalies')
    plt.legend()
    plt.show()

# Running the system with sample data
def generate_sample_data(size=50):
    data = []
    for i in range(size):
        timestamp = i + 1
        price = random.randint(100, 500)
        data.append((timestamp, price))
    return data

data = generate_sample_data(50)

# Sort the data using merge sort
sorter = DataSorter()
sorted_data = sorter.merge_sort(data)

# Find the period of maximum gain
max_gain_finder = MaxSubarray()
max_gain_info = max_gain_finder.find_max_gain(sorted_data)

# Detect anomalies
anomaly_detector = AnomalyDetector()
anomaly_pair, min_dist = anomaly_detector.closest_pair(sorted_data)

# Visualize trends and anomalies
visualize_trends_and_anomalies(sorted_data, max_gain_info, anomaly_pair)