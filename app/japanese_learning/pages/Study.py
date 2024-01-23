from datetime import date

import pandas as pd
import streamlit as st
from utils.data import build_grammar_data, build_study_data

st.markdown("# Study Plan")

study_data = build_study_data()

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

st.data_editor(
    df,
    column_config={
        "grammar_1": st.column_config.TextColumn("Grammar 1"),
        "grammar_2": st.column_config.TextColumn("Grammar 2"),
        "grammar_3": st.column_config.TextColumn("Grammar 3"),
    },
    hide_index=True,
    use_container_width=True,
)
