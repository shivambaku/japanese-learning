import random
from datetime import datetime

import streamlit as st
from utils.data import build_grammar_data, build_review, build_study_data

grammar_data = build_grammar_data()
study_data = build_study_data()


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

review = build_review(first_not_completed)
st.markdown("#### Reviews")
for example in review:
    st.markdown(f"- {example}")

if st.button("Mark as completed"):
    first_not_completed["completed"] = True
    grammar_data[first_not_completed["grammar_1_index"]][
        "completed_at"
    ] = datetime.now()
    grammar_data[first_not_completed["grammar_2_index"]][
        "completed_at"
    ] = datetime.now()
    grammar_data[first_not_completed["grammar_3_index"]][
        "completed_at"
    ] = datetime.now()
    st.rerun()
