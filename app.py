import streamlit as st
import pandas as pd
import numpy as np

# Creating a DataFrame
df = pd.DataFrame({
    "Column A": [1, 2, 3, 4],
    "Column B": [10, 20, 30, 40]
})

# Display text and DataFrame
st.write("Hello, Streamlit!")
st.write(df)

# Create a DataFrame for chart
chart = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

# Display a line chart
st.line_chart(chart)
