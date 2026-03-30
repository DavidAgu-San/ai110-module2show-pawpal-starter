import streamlit as st
#classes and scheduler

class Task:
    PRIORITY_MAP = {"high": 3, "medium": 2, "low": 1}

    def __init__(self, title, duration_minutes, priority):
        self.title = title
        self.duration = duration_minutes
        self.priority = priority
        self.priority_score = Task.PRIORITY_MAP[priority]

    def __repr__(self):
        return f"{self.title} ({self.priority}, {self.duration} min)"


class Pet:
    def __init__(self, name, species):
        self.name = name
        self.species = species


class Owner:
    def __init__(self, name):
        self.name = name


class Scheduler:
    """
    Simple rule-based scheduler:
    - Sort tasks by priority (high → low)
    - Break ties using shortest duration first
    - Assign start times sequentially beginning at 8:00 AM
    """

    def build_schedule(self, tasks):
        task_objs = [
            Task(t["title"], t["duration_minutes"], t["priority"])
            for t in tasks
        ]

        # Sort by priority desc, duration asc
        task_objs.sort(key=lambda t: (-t.priority_score, t.duration))

        schedule = []
        current_time = 8 * 60  # Start at 8:00 AM

        for t in task_objs:
            start_hour = current_time // 60
            start_min = current_time % 60
            start_str = f"{start_hour:02d}:{start_min:02d}"

            explanation = (
                f"Chosen because it is **{t.priority} priority** "
                f"and takes **{t.duration} minutes**."
            )

            schedule.append({
                "task": t.title,
                "start": start_str,
                "duration": t.duration,
                "priority": t.priority,
                "why": explanation
            })

            current_time += t.duration

        return schedule

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to the PawPal+ starter app.

This file is intentionally thin. It gives you a working Streamlit app so you can start quickly,
but **it does not implement the project logic**. Your job is to design the system and build it.

Use this app as your interactive demo once your backend classes/functions exist.
"""
)

with st.expander("Scenario", expanded=True):
    st.markdown(
        """
**PawPal+** is a pet care planning assistant. It helps a pet owner plan care tasks
for their pet(s) based on constraints like time, priority, and preferences.

You will design and implement the scheduling logic and connect it to this Streamlit UI.
"""
    )

with st.expander("What you need to build", expanded=True):
    st.markdown(
        """
At minimum, your system should:
- Represent pet care tasks (what needs to happen, how long it takes, priority)
- Represent the pet and the owner (basic info and preferences)
- Build a plan/schedule for a day that chooses and orders tasks based on constraints
- Explain the plan (why each task was chosen and when it happens)
"""
    )

st.divider()

st.subheader("Quick Demo Inputs (UI only)")
owner_name = st.text_input("Owner name", value="Jordan")
pet_name = st.text_input("Pet name", value="Mochi")
species = st.selectbox("Species", ["dog", "cat", "other"])

st.markdown("### Tasks")
st.caption("Add a few tasks. In your final version, these should feed into your scheduler.")

if "tasks" not in st.session_state:
    st.session_state.tasks = []

col1, col2, col3 = st.columns(3)
with col1:
    task_title = st.text_input("Task title", value="Morning walk")
with col2:
    duration = st.number_input("Duration (minutes)", min_value=1, max_value=240, value=20)
with col3:
    priority = st.selectbox("Priority", ["low", "medium", "high"], index=2)

if st.button("Add task"):
    st.session_state.tasks.append(
        {"title": task_title, "duration_minutes": int(duration), "priority": priority}
    )

if st.session_state.tasks:
    st.write("Current tasks:")
    st.table(st.session_state.tasks)
else:
    st.info("No tasks yet. Add one above.")

st.divider()

st.subheader("Build Schedule")
st.caption("This button should call your scheduling logic once you implement it.")

if st.button("Generate schedule"):
    st.warning(
        "Not implemented yet. Next step: create your scheduling logic (classes/functions) and call it here."
    )
    st.markdown(
        """
Suggested approach:
1. Design your UML (draft).
2. Create class stubs (no logic).
3. Implement scheduling behavior.
4. Connect your scheduler here and display results.
"""
    )
