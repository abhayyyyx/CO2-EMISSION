import streamlit as st
import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestRegressor

# Creating Sidebar
with st.sidebar:
    st.markdown("# CO2 Emissions by Vehicle")
    user_input = st.selectbox('Please select', ('Visualization', 'Model'))

# Load the vehicle dataset
df = pd.read_csv(r"C:\Users\SUMAN\Desktop\AA-2024\project - co2\co2_emissions (1).csv")

# Drop rows with natural gas as fuel type
fuel_type_mapping = {"Z": "Premium Gasoline", "X": "Regular Gasoline", "D": "Diesel", "E": "Ethanol(E85)", "N": "Natural Gas"}
df["fuel_type"] = df["fuel_type"].map(fuel_type_mapping)
df_natural = df[~df["fuel_type"].str.contains("Natural Gas")].reset_index(drop=True)

# Remove outliers from the data
df_new = df_natural[['engine_size', 'cylinders','fuel_type', 'fuel_consumption_comb(l/100km)', 'co2_emissions']]
df_new['fuel_type'] = df_new['fuel_type'].astype('category').cat.codes
df_new_model = df_new[(np.abs(stats.zscore(df_new)) < 1.9).all(axis=1)]

if user_input == 'Visualization':
    # Visualization code goes here...
    # Remove unwanted warnings---------------------------------------------------------------------------------
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # Showing Dataset------------------------------------------------------------------------------------------
    st.title('CO2 Emissions by Vehicle')
    st.header("Data We collected from the source")
    st.write(df)

    # Brands of Cars-------------------------------------------------------------------------------------------
    st.subheader('Brands of Cars')
    df_brand = df['make'].value_counts().reset_index().rename(columns={'count': 'Count'})
    plt.figure(figsize=(15, 6))
    fig1 = sns.barplot(data=df_brand, x="make", y="Count")
    plt.xticks(rotation=75)
    plt.title("All Car Companies and their Cars")
    plt.xlabel("Companies")
    plt.ylabel("Cars")
    plt.bar_label(fig1.containers[0], fontsize=7)
    st.pyplot()
    st.write(df_brand)

    # Top 25 Models of Cars------------------------------------------------------------------------------------
    st.subheader('Top 25 Models of Cars')
    df_model = df['model'].value_counts().reset_index().rename(columns={'count':'Count'})
    plt.figure(figsize=(20, 6))
    fig2 = sns.barplot(data=df_model[:25], x="model", y="Count")
    plt.xticks(rotation=75)
    plt.title("Top 25 Car Models")
    plt.xlabel("Models")
    plt.ylabel("Cars")
    plt.bar_label(fig2.containers[0])
    st.pyplot()
    st.write(df_model)

    # Vehicle Class--------------------------------------------------------------------------------------------
    st.subheader('Vehicle Class')
    df_vehicle_class = df['vehicle_class'].value_counts().reset_index().rename(columns={'count':'Count'})
    plt.figure(figsize=(20, 5))
    fig3 = sns.barplot(data=df_vehicle_class, x="vehicle_class", y="Count")
    plt.xticks(rotation=75)
    plt.title("All Vehicle Class")
    plt.xlabel("Vehicle Class")
    plt.ylabel("Cars")
    plt.bar_label(fig3.containers[0])
    st.pyplot()
    st.write(df_vehicle_class)

    # Engine Sizes of Cars-------------------------------------------------------------------------------------
    st.subheader('Engine Sizes of Cars')
    df_engine_size = df['engine_size'].value_counts().reset_index().rename(columns={'count':'Count'})
    plt.figure(figsize=(20, 6))
    fig4 = sns.barplot(data=df_engine_size, x="engine_size", y="Count")
    plt.xticks(rotation=90)
    plt.title("All Engine Sizes")
    plt.xlabel("Engine Size(L)")
    plt.ylabel("Cars")
    plt.bar_label(fig4.containers[0])
    st.pyplot()
    st.write(df_engine_size)

    # Cylinders-----------------------------------------------------------------------------------------------
    st.subheader('cylinders')
    df_cylinders = df['cylinders'].value_counts().reset_index().rename(columns={'count':'Count'})
    plt.figure(figsize=(20, 6))
    fig5 = sns.barplot(data=df_cylinders, x="cylinders", y="Count")
    plt.xticks(rotation=90)
    plt.title("All Cylinders")
    plt.xlabel("Cylinders")
    plt.ylabel("Cars")
    plt.bar_label(fig5.containers[0])
    st.pyplot()
    st.write(df_cylinders)

    # Transmission of Cars------------------------------------------------------------------------------------
    transmission_mapping = {'AS':'Automatic select shift', 'M' : 'Manual', 'AV' :'Continously variable', 'AM' : 'Automated manual', 'A' : 'Automatic'}
    df["transmission"] = df["transmission"].map(transmission_mapping)
    st.subheader('Transmission')
    df_transmission = df['transmission'].value_counts().reset_index().rename(columns={'count': 'Count'})
    fig6 = plt.figure(figsize=(20, 5))
    sns.barplot(data=df_transmission, x="transmission", y="Count")
    plt.title("All Transmissions")
    plt.xlabel("Transmissions")
    plt.ylabel("Cars")
    plt.bar_label(plt.gca().containers[0])
    st.pyplot(fig6)
    st.write(df_transmission)

    # Fuel Type of Cars--------------------------------------------------------------------------------------
    st.subheader('Fuel Type')
    df_fuel_type = df['fuel_type'].value_counts().reset_index().rename(columns={'count': 'Count'})
    fig7 = plt.figure(figsize=(20, 5))
    sns.barplot(data=df_fuel_type, x="fuel_type", y="Count")
    plt.title("All Fuel Types")
    plt.xlabel("Fuel Types")
    plt.ylabel("Cars")
    plt.bar_label(plt.gca().containers[0])
    st.pyplot(fig7)
    st.text("We have only one data on natural gas. So we cannot predict anything using only one data. That's why we have to drop this row.")
    st.write(df_fuel_type)

    # Removing Natural Gas-----------------------------------------------------------------------------------
    st.subheader('After removing Natural Gas data')
    df_ftype = df_natural['fuel_type'].value_counts().reset_index().rename(columns={'count': 'Count'})
    fig8 = plt.figure(figsize=(20, 5))
    sns.barplot(data=df_ftype, x="fuel_type", y="Count")
    plt.title("All Fuel Types")
    plt.xlabel("Fuel Types")
    plt.ylabel("Cars")
    plt.bar_label(plt.gca().containers[0])
    st.pyplot(fig8)
    st.write(df_ftype)

    # CO2 Emission variation with Brand----------------------------------------------------------------------
    st.header('Variation in CO2 emissions with different features')
    st.subheader('CO2 Emission with Brand ')
    df_co2_make = df.groupby(['make'])['co2_emissions'].mean().sort_values().reset_index()
    fig8 = plt.figure(figsize=(20, 5))
    sns.barplot(data=df_co2_make, x="make", y="co2_emissions")
    plt.xticks(rotation=90)
    plt.title("CO2 Emissions variation with Brand")
    plt.xlabel("Brands")
    plt.ylabel("CO2 Emissions(g/km)")
    plt.bar_label(plt.gca().containers[0], fontsize=8, fmt='%.1f')
    st.pyplot(fig8)

    def plot_bar(data, x_label, y_label, title):
        plt.figure(figsize=(23, 5))
        sns.barplot(data=data, x=x_label, y=y_label)
        plt.xticks(rotation=90)
        plt.title(title)
        plt.xlabel(x_label)
        plt.ylabel(y_label)
        plt.bar_label(plt.gca().containers[0], fontsize=9)

    # CO2 Emissions variation with Vehicle Class-------------------------------------------------------------
    st.subheader('CO2 Emissions variation with Vehicle Class')
    df_co2_vehicle_class = df.groupby(['vehicle_class'])['co2_emissions'].mean().sort_values().reset_index()
    plot_bar(df_co2_vehicle_class, "vehicle_class", "co2_emissions", "CO2 Emissions variation with Vehicle Class")
    st.pyplot()

    # CO2 Emission variation with Transmission---------------------------------------------------------------
    st.subheader('CO2 Emission variation with Transmission')
    df_co2_transmission = df.groupby(['transmission'])['co2_emissions'].mean().sort_values().reset_index()
    plot_bar(df_co2_transmission, "transmission", "co2_emissions", "CO2 Emission variation with Transmission")
    st.pyplot()

    # CO2 Emissions variation with Fuel Type--------------------------------------------------------------
    st.subheader('CO2 Emissions variation with Fuel Type')
    df_co2_fuel_type = df.groupby(['fuel_type'])['co2_emissions'].mean().sort_values().reset_index()
    plot_bar(df_co2_fuel_type, "fuel_type", "co2_emissions", "CO2 Emissions variation with Fuel Type")
    st.pyplot()

    # Box Plots-------------------------------------------------------------------------------------------
    st.header("Box Plots")
    plt.figure(figsize=(20, 10))
    features = ['engine_size', 'cylinders', 'fuel_consumption_comb(l/100km)','fuel_type', 'co2_emissions']
    for i, feature in enumerate(features, start=1):
        plt.subplot(2, 2, i)
        plt.boxplot(df_new[feature])
        plt.title(feature)
    st.pyplot()

    # Outliers-------------------------------------------------------------------------------------------
    st.text("As we can see there are some outliers present in our Dataset")
    st.subheader("After removing outliers")
    st.write("Before removing outliers we have", len(df), "data")
    st.write("After removing outliers we have", len(df_new_model), "data")

    # Boxplot after removing outliers-------------------------------------------------------------------
    st.subheader("Boxplot after removing outliers")
    plt.figure(figsize=(20, 10))
    for i, feature in enumerate(features, start=1):
        plt.subplot(2, 2, i)
        plt.boxplot(df_new_model[feature])
        plt.title(feature)
    st.pyplot()
else:
    # Prepare the data for modeling
    X = df_new_model[['engine_size', 'cylinders', 'fuel_consumption_comb(l/100km)', 'fuel_type']]
    y = df_new_model['co2_emissions']

    # Train the random forest regression model
    model = RandomForestRegressor().fit(X, y)

    # Create the Streamlit web app
    st.title('CO2 Emission Prediction')
    st.write('Enter the vehicle specifications to predict CO2 emissions.')

    # Input fields for user
    engine_size = st.number_input('engine_size', step=0.1, format="%.1f")
    cylinders = st.number_input('cylinders', min_value=2, max_value=16, step=1)
    fuel_type = st.selectbox('fuel_type', options=df['fuel_type'].unique())
    fuel_consumption = st.number_input('fuel_consumption_comb(l/100km)', step=0.1, format="%.1f")

    # Encode the fuel_type as done in the training data
    fuel_type_encoded = pd.Series([fuel_type]).astype('category').cat.codes[0]

    # Predict CO2 emissions
    input_data = np.array([[engine_size, cylinders, fuel_consumption, fuel_type_encoded]])
    if st.button('Predict'):
        predicted_co2 = model.predict(input_data)

        # Display the prediction
        st.write(f'Predicted CO2 Emissions: {predicted_co2[0]:.2f} g/km')
