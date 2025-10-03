# Add this block to frontend-agent/app.py

import os, requests, streamlit as st

BACKEND = os.getenv("BACKEND_URL", "http://localhost:8000")

st.header("🧪 Mercenaries (Fictional, Defensive)")
if st.button("Load Mercenaries"):
    r = requests.get(f"{BACKEND}/mercenaries", timeout=10)
    data = r.json()
    st.write(f"Available: {data.get('count',0)}")
    items = data.get("items", [])
    for item in items:
        with st.expander(f"{item['name']} — {item['role']}"):
            st.json(item)
            if st.button(f"Instantiate: {item['id']}", key=item['id']):
                resp = requests.post(f"{BACKEND}/mercenaries/instantiate/{item['id']}", json={}, timeout=20)
                st.json(resp.json())
