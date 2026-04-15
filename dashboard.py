import streamlit as st
import requests
import pandas as pd
import matplotlib.pyplot as plt

# API Configuration
API_URL = "http://127.0.0.1:5000/api/tasks"

st.set_page_config(page_title="Task Manager Pro", layout="wide")

# Custom CSS for the Stone & Amber aesthetic
st.markdown("""
    <style>
    .stApp { background-color: #0c0a09; color: #fafaf9; }
    
    /* Target based on the help/label text inside the button */
    /* AMBER for Submit */
    div[data-testid="stSidebar"] button {
        background-color: #f59e0b !important;
        color: #0c0a09 !important;
        font-weight: bold !important;
    }

    /* BLUE for Update - Using the 'secondary' type as a selector */
    div[data-testid="stColumn"]:nth-of-type(3) button {
        background-color: #3b82f6 !important;
        color: white !important;
        border: none !important;
    }

    /* RED for Delete - Using the 'secondary' type as a selector */
    div[data-testid="stColumn"]:nth-of-type(4) button {
        background-color: #ef4444 !important;
        color: white !important;
        border: none !important;
    }

    /* Hover States */
    button:hover {
        opacity: 0.8 !important;
        border: 1px solid white !important;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("✅ Task Manager Enterprise")

# --- REFINED HELPER FUNCTIONS ---
def get_all_tasks():
    try:
        response = requests.get(API_URL, timeout=5)
        return response.json().get("tasks", []) if response.status_code == 200 else []
    except: return []

def api_request(method, url, payload=None, action_name="Processing"):
    with st.spinner(f"{action_name}..."):
        try:
            if method == "POST": res = requests.post(url, json=payload)
            elif method == "PUT": res = requests.put(url, json=payload)
            elif method == "DELETE": res = requests.delete(url)
            
            if res.status_code in [200, 201, 204]:
                st.toast(f"{action_name} successful!", icon="🚀")
                return True
        except Exception as e:
            st.error(f"Error: {e}")
    return False

# --- LAYOUT ---
main_col, side_col = st.columns([0.7, 0.3])

with side_col:
    st.header("Control Panel")
    with st.expander("➕ Add New Task", expanded=True):
        new_task_title = st.text_input("Task Description")
        if st.button("Submit Task", key="btn_submit", use_container_width=True):
            if new_task_title and api_request("POST", API_URL, {"title": new_task_title}, "Creating task"):
                st.rerun()

    # Re-fetch tasks to ensure analytics are fresh
    tasks = get_all_tasks()
    if tasks:
        df = pd.DataFrame(tasks)
        st.subheader("Analytics")
        total = len(df)
        completed = len(df[df['done'] == True])
        
        st.metric("Total Tasks", total)
        st.metric("Completion", f"{(completed/total)*100:.1f}%" if total > 0 else "0%")
        
        fig, ax = plt.subplots(figsize=(4, 4))
        fig.patch.set_facecolor('#0c0a09')
        # Handle cases where all tasks are pending or all are done
        counts = df['done'].value_counts()
        labels = ['Done' if x else 'Pending' for x in counts.index]
        ax.pie(counts, labels=labels, colors=['#f59e0b', '#44403c'], textprops={'color':"w"})
        st.pyplot(fig)

with main_col:
    st.header("Task Registry")
    if not tasks:
        st.info("No tasks in the database.")
    else:
        for task in tasks:
            with st.container():
                c1, c2, c3, c4 = st.columns([0.1, 0.5, 0.2, 0.2])
                with c1: st.write(f"#{task['id']}")
                
                with c2:
                    # IMPROVEMENT: Adding on_change would be ideal, 
                    # but since we need both title and checkbox, we detect changes here:
                    is_done = st.checkbox("Done", value=task['done'], key=f"done_{task['id']}")
                    current_title = st.text_input("Title", value=task['title'], key=f"txt_{task['id']}", label_visibility="collapsed")
                    
                    # AUTO-SAVE IF CHECKBOX TOGGLED
                    if is_done != task['done']:
                        api_request("PUT", f"{API_URL}/{task['id']}", {"title": current_title, "done": is_done}, "Updating Status")
                        st.rerun()

                with c3:
                    if st.button("Update", key=f"upd_{task['id']}", use_container_width=True):
                        api_request("PUT", f"{API_URL}/{task['id']}", {"title": current_title, "done": is_done}, "Updating")
                        st.rerun()
                with c4:
                    if st.button("Delete", key=f"del_{task['id']}", use_container_width=True):
                        api_request("DELETE", f"{API_URL}/{task['id']}", action_name="Deleting")
                        st.rerun()
            st.divider()

if tasks:
    progress = completed / total
    st.progress(progress, text=f"Overall Progress: {int(progress*100)}%")