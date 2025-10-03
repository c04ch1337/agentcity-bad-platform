# How to Add the Mercenaries (Easy Mode)

These are pretend (fictional) helper “agents” for safe training. We are only adding files and simple buttons. Nothing dangerous, no hacking.

## Part A — Put the files in the right place

1. Find your project folder called **`ai-battle-legion`**.
2. Open it and **make a new folder** named **`mercenaries`**.
3. Copy everything from this add‑on’s **`mercenaries/`** folder into your project’s **`ai-battle-legion/mercenaries/`** folder.

## Part B — Teach the API (backend) to read them

1. In your project, go to: `ai-battle-legion/backend/app/`
2. Create folders so the path looks like: `backend/app/mercenaries/` and `backend/app/routes/`
3. Copy these files from this add‑on:
   - `backend_patch/app/mercenaries/registry.py`  →  `backend/app/mercenaries/registry.py`
   - `backend_patch/app/routes/mercenaries.py`    →  `backend/app/routes/mercenaries.py`
4. Open `backend/app/main.py` and add these two lines:
   ```python
   from .routes.mercenaries import router as mercs_router
   app.include_router(mercs_router)
   ```
5. Save the file.

## Part C — Add a simple screen to the Streamlit app (frontend)

1. Open: `ai-battle-legion/frontend-agent/app.py`
2. Scroll to the bottom and paste this block:
   ```python
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
   ```
3. Save the file.

## Part D — Turn the containers off and back on

In a terminal, inside your `ai-battle-legion` folder:

```bash
docker compose down
docker compose up --build
```

- Backend docs: http://localhost:8000/docs  
- Agent console: http://localhost:8501

## Part E — Try it!

1. Open the Agent Console (Streamlit) at http://localhost:8501
2. Click **“Load Mercenaries”**. You should see a list.
3. Expand one, then click **Instantiate**. You’ll see a simple “agent config” appear.

That’s it. You added the mercenaries the safe way. If something breaks, read the messages on the screen and check your spelling.
