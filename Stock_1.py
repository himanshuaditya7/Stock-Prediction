import csv
import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt

dates = []
prices = []
def get_data(filename):
    with open(filename, 'r') as csvfile:
        csvFileReader = csv.reader(csvfile)
        next(csvFileReader)  # skipping column names
        for row in csvFileReader:
            dates.append(int(row[0].split('-')[0]))
            prices.append(float(row[1]))
    return


def show_plot(dates, prices):
    linear_mod = linear_model.LinearRegression()
    dates = np.reshape(dates, (len(dates), 1))  # converting to matrix of n X 1
    prices = np.reshape(prices, (len(prices), 1))
    linear_mod.fit(dates, prices)  # fitting the data points in the model
    plt.scatter(dates, prices, color='yellow')  # plotting the initial datapoints
    plt.plot(dates, linear_mod.predict(dates), color='blue', linewidth=3)  # plotting the line made by linear regression
    plt.show()
    return


def predict_price(dates, prices, x):
    linear_mod = linear_model.LinearRegression()  # defining the linear regression model
    dates = np.reshape(dates, (len(dates), 1))  # converting to matrix of n X 1
    prices = np.reshape(prices, (len(prices), 1))
    linear_mod.fit(dates, prices)  # fitting the data points in the model
    predicted_price = linear_mod.predict(x)
    return predicted_price[0][0], linear_mod.coef_[0][0], linear_mod.intercept_[0]


get_data('GOOGL.csv')  # calling get_data method by passing the csv file to it
print(dates)
print(prices)
print("\n")


show_plot(dates, prices)
