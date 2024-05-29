import streamlit as st
import pandas as pd
import seaborn as sns

st.write("""
# My first app
Hello *world!*
""")

st.date_input('What is the most amazing date? ')

df = sns.load_dataset('dowjones')
df = df.set_index('Date')
print(df)
st.line_chart(df)
