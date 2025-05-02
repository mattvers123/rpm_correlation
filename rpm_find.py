import numpy as np
import pandas as pd

def find_start_time(t, rpm, start_rpm, frame_duration=1.0, step=0.01):
    """
    Finds the earliest time where the average RPM over a specified frame duration
    meets or exceeds the start_rpm threshold.

    Parameters:
    - t: numpy array of time values.
    - rpm: numpy array of RPM values corresponding to time t.
    - start_rpm: The desired starting RPM threshold.
    - frame_duration: Duration of the time window in seconds (default is 1.0 second).
    - step: Time increment to slide the window (default is 0.01 second).

    Returns:
    - start_time: The time at which the average RPM over the frame_duration meets or exceeds start_rpm.
    - average_rpm: The average RPM within that time window.
    """
    max_time = t[-1]
    current_time = t[0]

    while current_time + frame_duration <= max_time:
        start_idx = np.searchsorted(t, current_time)
        end_idx = np.searchsorted(t, current_time + frame_duration)
        if end_idx > len(rpm):
            break
        avg_rpm = np.mean(rpm[start_idx:end_idx])
        if avg_rpm >= start_rpm:
            return current_time, avg_rpm
        current_time += step

    raise ValueError("No suitable start time found where average RPM meets or exceeds the threshold.")


data = pd.read_csv("/content/ornek_data_04.csv", on_bad_lines='skip')
