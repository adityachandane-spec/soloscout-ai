import streamlit as st
from eligibility import check_eligibility

st.set_page_config(page_title="SoloScout AI", page_icon="🎯", layout="wide")

st.title("🎯 SoloScout AI")
st.subheader("Find opportunities you can actually apply for.")
st.caption("Prototype v0.1 · Eligibility rules demo · Sample records are illustrative, not live events.")

with st.sidebar:
    st.header("Your student profile")
    age = st.number_input("Your age", min_value=13, max_value=100, value=17)
    student_type = st.selectbox("Education level", ["school", "undergraduate", "graduate", "other"])
    solo = st.checkbox("I want to participate individually", value=True)
    budget = st.number_input("Maximum registration fee (₹)", min_value=0, max_value=100000, value=0, step=100)
    st.divider()
    st.caption("Your profile is only used locally in this prototype. Do not enter sensitive personal information.")

profile = {"age": int(age), "student_type": student_type, "solo": solo, "budget_inr": int(budget)}

# Clearly labelled fixtures let us test the rules before connecting live search.
opportunities = [
    {
        "name": "Demo: School Innovators Challenge",
        "description": "Illustrative event record for testing age, education, solo and fee checks.",
        "min_age": 14, "max_age": 19,
        "accepted_student_types": ["school"],
        "solo_allowed": True, "fee_inr": 0,
        "source_url": "https://example.com/",
        "source_note": "DEMO DATA — not a real event. Replace with an official event source before relying on it.",
    },
    {
        "name": "Demo: University Team Hackathon",
        "description": "Illustrative event record that requires a university team.",
        "min_age": 18, "max_age": None,
        "accepted_student_types": ["undergraduate", "graduate"],
        "solo_allowed": False, "fee_inr": 0,
        "source_url": "https://example.com/",
        "source_note": "DEMO DATA — not a real event. Replace with an official event source before relying on it.",
    },
    {
        "name": "Demo: Open Youth Coding Sprint",
        "description": "Illustrative record with missing age and team rules to demonstrate uncertainty.",
        "min_age": None, "max_age": None,
        "accepted_student_types": ["school", "undergraduate"],
        "solo_allowed": None, "fee_inr": 0,
        "source_url": "https://example.com/",
        "source_note": "DEMO DATA — missing rules intentionally produce a verification warning.",
    },
]

st.markdown("### Eligibility check")
st.info("This first version tests eligibility logic using clearly labelled sample records. Live web discovery and AI agent tools are the next development milestone.")

for opportunity in opportunities:
    result = check_eligibility(profile, opportunity)
    with st.container(border=True):
        left, right = st.columns([3, 1])
        with left:
            st.markdown(f"#### {opportunity['name']}")
            st.write(opportunity["description"])
            st.caption(opportunity["source_note"])
            st.link_button("Example source (not an event listing)", opportunity["source_url"], disabled=True)
        with right:
            st.metric("Assessment", result["status"])
            st.caption(f"{result['passed']} pass · {result['failed']} fail · {result['unknown']} unknown")
        with st.expander("See why SoloScout made this assessment"):
            for check in result["checks"]:
                icon = {"pass": "✅", "fail": "❌", "unknown": "⚠️"}[check["status"]]
                st.write(f"{icon} **{check['requirement']}:** {check['explanation']}")

st.divider()
st.markdown("### What is coming next")
st.write("1. Live opportunity search · 2. Official-page extraction · 3. Evidence-backed eligibility checks · 4. AI agent planning and ranking.")
st.caption("SoloScout never treats missing information as proof of eligibility. Always confirm details on the organiser's official page.")
