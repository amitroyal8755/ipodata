import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import os

def main():
    # Set page title
    st.title("IPO Data Display App")

    # Load data from Excel file
    # Load data from Excel file
    file_path = os.path.join(os.path.dirname(__file__), 'ipo_data.xlsx')
    try:
        df = pd.read_excel(file_path)
    except Exception as e:
        st.error(f"Error: {e}")
        return


    # Display the data
    st.write("### IPO Data")
    give = st.number_input("No. of lines", min_value=1, value=5)
    st.dataframe(df.sample(give))

    # Modify DataFrame
    df['Profit/Loss'] = df['Profit/Loss'] * 100
    df['Listing Day Gain'] = df['Listing Day Gain'] * 100

    # Plotting - Scatter Plot of Listing Day Gain vs Total Subscription
    st.write("### Scatter Plot of Listing Day Gain vs Total Subscription")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Total '], df['Listing Day Gain'])
    ax.set_title('Scatter Plot of Listing Day Gain vs Total Subscription')
    ax.set_xlabel('Total Subscription')
    ax.set_ylabel('Listing Day Gain')
    st.pyplot(fig)

    # Plotting - Scatter Plot of Profit/Loss vs Total Subscription
    st.write("### Scatter Plot of Profit/Loss vs Total Subscription")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Total '], df['Profit/Loss'])
    ax.set_title('Scatter Plot of Profit/Loss vs Total Subscription')
    ax.set_xlabel('Total Subscription')
    ax.set_ylabel('Profit/Loss')
    st.pyplot(fig)

    # Plotting - Scatter Plot of Profit/Loss vs Total Subscription with Listing Day Gain as Marker Size
    st.write("### Scatter Plot of Profit/Loss vs Total Subscription with Listing Day Gain as Marker Size")
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.scatter(df['Total '], df['Profit/Loss'], s=df['Listing Day Gain']*20, alpha=0.5, label='Listing Day Gain')
    ax.set_title('Scatter Plot of Profit/Loss vs Total Subscription')
    ax.set_xlabel('Total Subscription')
    ax.set_ylabel('Profit/Loss')
    ax.legend()
    st.pyplot(fig)

    # Plotting - 3D Scatter Plot of Profit/Loss, Total Subscription, and Listing Day Gain
    st.write("### Profit/Loss, Total Subscription, and Listing Day Gain")
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')
    scatter = ax.scatter(df['Total '], df['Profit/Loss'], df['Listing Day Gain'], c=df['Listing Day Gain'], cmap='viridis', s=100)
    ax.set_xlabel('Total Subscription')
    ax.set_ylabel('Profit/Loss')
    ax.set_zlabel('Listing Day Gain')
    cbar = plt.colorbar(scatter)
    cbar.set_label('Listing Day Gain')
    ax.set_title('3D Scatter Plot of Profit/Loss, Total Subscription, and Listing Day Gain')
    st.pyplot(fig)


    st.write("project made by amit")

if __name__ == "__main__":
    main()
