from datetime import datetime

import streamlit as st
from utils.data import (
    build_review,
    build_study_data,
    load_grammar_data,
    update_grammar_data,
)

st.cache_data.clear()

MAX_GRAMMAR_PER_DAY = 3

grammar_data = load_grammar_data()
study_data = build_study_data(grammar_data)

first_not_completed = [study for study in study_data if not study["completed"]][0]

st.markdown("# Japanese Learning")

st.markdown(
    f"#### Grammar {first_not_completed['grammar_1_index']}: {first_not_completed['grammar_1']}"
)
for example in first_not_completed["grammar_1_examples"]:
    st.markdown(f"- {example}")

st.markdown(
    f"#### Grammar {first_not_completed['grammar_2_index']}: {first_not_completed['grammar_2']}"
)
for example in first_not_completed["grammar_2_examples"]:
    st.markdown(f"- {example}")

st.markdown(
    f"#### Grammar {first_not_completed['grammar_3_index']}: {first_not_completed['grammar_3']}"
)
for example in first_not_completed["grammar_3_examples"]:
    st.markdown(f"- {example}")

review = build_review(grammar_data, study_data)
st.markdown("#### Reviews")
for example in review:
    st.markdown(f"- {example}")

if st.button("Mark as completed"):
    for i in range(MAX_GRAMMAR_PER_DAY):
        grammar_index = first_not_completed[f"grammar_{i+1}_index"]
        grammar_data.loc[grammar_index, "completed_at"] = datetime.now()

    update_grammar_data(grammar_data)

    st.rerun()
