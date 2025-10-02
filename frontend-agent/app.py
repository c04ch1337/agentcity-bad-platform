import os, requests, streamlit as st

BACKEND = os.getenv("BACKEND_URL", "http://localhost:8000")

st.set_page_config(page_title="AgentCity BAD — Agent Console", layout="wide")
st.title("🪖 AgentCity BAD — Agent Console")

col1, col2 = st.columns(2)
with col1:
    if st.button("Health Check"):
        r = requests.get(f"{BACKEND}/health", timeout=10)
        st.json(r.json())

with col2:
    if st.button("List Agents"):
        r = requests.get(f"{BACKEND}/agents", timeout=10)
        st.json(r.json())

goal = st.text_input("Mission Goal", value="Optimize inventory")
if st.button("Deploy GENERAL"):
    payload = {"mission_type": "plan_and_delegate", "goal": goal}
    r = requests.post(f"{BACKEND}/deploy/AI-GENERAL-STRATEGIC-COMMAND", json=payload, timeout=20)
    st.json(r.json())
