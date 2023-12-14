
import numpy as np
import pandas as pd
import streamlit as st

def eq(x, E, Es, a):
  top = np.pi * pow(a,2) + 6 * np.pi * x * a + 8 * pow(x, 2)
  bottom = pow(np.pi, 2) * pow(a, 2) * E + 2 * np.pi * a * (2 * x * Es + x * E) + 8 * pow(x, 2) * Es
  frac = top / bottom
  return E * Es * frac

E = st.slider("E", value=100, min_value=0, max_value=500)
Es = 130
a = 100

df = pd.DataFrame(np.linspace(0,1000, 100), columns=['x'])
df['y'] = df['x'].apply(lambda x: eq(x, E, Es, a))
df.head()

st.line_chart(df, x='x', y='y')