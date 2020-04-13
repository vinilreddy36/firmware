#!/usr/bin/python
import matplotlib.pyplot as plt

class one_dimensional_kalman_filter:
    def __init__(self, measured_value, error_in_measured_value, initial_estimate, initial_error_in_estimate):
        self.measured_value = measured_value
        self.error_in_measured_value = error_in_measured_value
        self.previous_estimate = initial_estimate
        self.error_in_estimate = initial_error_in_estimate
        self.kalman_gain = 0
        self.current_estimate = 0
        self.predicted_values = []

    def kalman_filter(self):
        count = 0
        while True:
            self.kalman_gain = self.error_in_estimate / (self.error_in_estimate + self.error_in_measured_value)
            self.current_estimate = self.previous_estimate + self.kalman_gain*(self.measured_value[count] - self.previous_estimate)
            self.error_in_estimate = (1 - self.kalman_gain) * self.error_in_estimate
            self.previous_estimate = self.current_estimate
            self.predicted_values.append(self.current_estimate)
            count = count + 1
            if len(self.measured_value) == count:
                break
        return self.predicted_values


data = [75, 71, 70, 74, 73, 71, 72, 76, 75, 74, 73, 71, 70, 70, 73, 73]

test = one_dimensional_kalman_filter(data, 4, 50, 2.0)
predicted_data = test.kalman_filter()
print(predicted_data)

plt.plot(data, 'b', predicted_data, 'g')
plt.ylim([20, 80])
plt.show()
