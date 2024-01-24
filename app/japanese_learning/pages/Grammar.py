from datetime import date

import pandas as pd
import streamlit as st
from utils.data import load_grammar_data

st.cache_data.clear()

st.markdown("# Grammar")
df = load_grammar_data()
st.dataframe(df, hide_index=True)
