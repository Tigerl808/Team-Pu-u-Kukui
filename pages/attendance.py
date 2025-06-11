import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from streamlit_extras.add_vertical_space import add_vertical_space

from style_helper import apply_custom_style

@st.cache_data
def load_and_clean_data():
  df = pd.read_csv("data/Tbl_RegAttend.csv")

  # Remove completely empty columns (extra commas at the end of CSV)
  df = df.dropna(axis=1, how='all')

  # Filter to rows where Island == "Total"
  df = df[df["Island"] == "Total"].copy()

  # Clean column names
  df.columns = df.columns.str.strip().str.replace(' ', '_').str.replace('/', '_')
  
  # Convert all columns that can be numeric
  for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors='ignore')  # keep strings like 'Island', 'textDate'
  return df

def main():
  apply_custom_style()
  
  st.header("Attendance Analysis")
  df_total = load_and_clean_data()

  # Select numeric columns only for x and y axis
  numeric_cols = df_total.select_dtypes(include=['number']).columns.tolist()

  # Default to specific columns if available
  default_x = numeric_cols.index("Marketing_and_Outreach") if "Marketing_and_Outreach" in numeric_cols else 0
  default_y = numeric_cols.index("Attend_Rate") if "Attend_Rate" in numeric_cols else 1
  
  x_axis = st.selectbox("X-axis", numeric_cols, index=default_x)
  y_axis = st.selectbox("Y-axis", numeric_cols, index=default_y)

  fig, ax = plt.subplots()
  sns.regplot(x=df_total[x_axis], y=df_total[y_axis], ax=ax, scatter_kws={"s": 40})
  ax.set_title(f"{y_axis.replace('_', ' ')} vs {x_axis.replace('_', ' ')}")
  ax.set_xlabel(x_axis.replace('_', ' '))
  ax.set_ylabel(y_axis.replace('_', ' '))
  st.pyplot(fig)

if __name__ == "__main__":
  main()
