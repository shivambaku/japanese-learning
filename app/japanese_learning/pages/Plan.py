from datetime import date

import pandas as pd
import streamlit as st
from utils.data import build_grammar_data, build_study_data, load_grammar_data

st.cache_data.clear()

st.markdown("# Study Plan")

grammar_data = load_grammar_data()
study_data = build_study_data(grammar_data)

df = pd.DataFrame(study_data)

df.drop(
    columns=[
        "grammar_1_index",
        "grammar_2_index",
        "grammar_3_index",
        "grammar_1_examples",
        "grammar_2_examples",
        "grammar_3_examples",
    ],
    inplace=True,
)

st.dataframe(
    df,
    hide_index=True,
    use_container_width=True,
)
