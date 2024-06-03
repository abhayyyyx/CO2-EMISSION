# CO2-EMISSION

Hello everyone,
This is co2 emission project, I've used random forest algo to predict the CO2. Hope this helps you to build your knowledge in data science.

Problem statement :

The fundamental goal here is to model the CO2 emissions as a function of several car engine features.

Data Set Details: The file contains the data for this example. Here the number of variables (columns) is 12, and the number of instances (rows) is 7385. In that way, this problem has the 12 following variables:

make, car brand under study.
model, the specific model of the car.
vehicle_class, car body type of the car.
engine_size, size of the car engine, in Liters.
cylinders, number of cylinders.
transmission, "A" for`Automatic', "AM" for ``Automated manual', "AS" for 'Automatic with select shift', "AV" for 'Continuously variable', "M" for 'Manual'.
fuel_type, "X" for 'Regular gasoline', "Z" for 'Premium gasoline', "D" for 'Diesel', "E" for 'Ethanol (E85)', "N" for 'Natural gas'.
fuel_consumption_city, City fuel consumption ratings, in liters per 100 kilometers.
fuel_consumption_hwy, Highway fuel consumption ratings, in liters per 100 kilometers.
fuel_consumption_comb(l/100km), the combined fuel consumption rating (55% city, 45% highway), in L/100 km.
fuel_consumption_comb(mpg), the combined fuel consumption rating (55% city, 45% highway), in miles per gallon (mpg).
co2_emissions, the tailpipe emissions of carbon dioxide for combined city and highway driving, in grams per kilometer.


## Business Objective : 

The primary objective of the project is to develop a model that can accurately predict CO2 emissions based on different engine features of cars.
The goal is to estimate the amount of CO2 a car will emit using the provided data.

## Tools and Technologies:

The project was developed using various tools and technologies, including:
Python programming language
Libraries such as NumPy, Matplotlib, SciPy, scikit-learn, and Streamlit
Linear Regression, Random Forest, K-Nearest Neighbors (KNN), and Support Vector Regression (SVR) models for prediction
Deployment on the cloud using Streamlit
