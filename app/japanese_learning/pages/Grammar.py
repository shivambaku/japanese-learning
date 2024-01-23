from datetime import date

import pandas as pd
import streamlit as st
from utils.data import build_grammar_data

st.markdown("# Grammar")

grammar_data = build_grammar_data()

df = pd.DataFrame(grammar_data)
df = df.drop("examples", axis=1)

st.data_editor(
    df,
    column_config={
        "title": st.column_config.TextColumn("Title"),
        "completed_at": st.column_config.DateColumn(
            "Completed At",
            format="DD.MM.YYYY",
            step=1,
        ),
    },
    # hide_index=True,
    use_container_width=True,
)
