import streamlit as st
from pawpal_system import Owner, Pet, Task, Scheduler

st.set_page_config(page_title="PawPal+", page_icon="🐾", layout="centered")

# ---------------------------------------------------------
# Initialize session state
# ---------------------------------------------------------
if "owner" not in st.session_state:
    st.session_state.owner = Owner("Jordan")  # default owner


# ---------------------------------------------------------
# Header + Intro
# ---------------------------------------------------------
st.title("🐾 PawPal+")

st.markdown(
    """
Welcome to PawPal+, your pet care planning assistant.

This app connects directly to your backend logic layer (`pawpal_system.py`)
so you can interactively test your scheduling system.
"""
)

st.divider()


# ---------------------------------------------------------
# Owner Name
# ---------------------------------------------------------
st.subheader("Owner Information")

owner_name = st.text_input("Owner name", value=st.session_state.owner.name)
st.session_state.owner.name = owner_name


# ---------------------------------------------------------
# Add Pets
# ---------------------------------------------------------
st.subheader("Add a Pet")

new_pet_name = st.text_input("Pet name")
new_pet_species = st.selectbox("Species", ["dog", "cat", "other"])

if st.button("Add Pet"):
    if new_pet_name.strip():
        pet = Pet(new_pet_name, new_pet_species)
        st.session_state.owner.add_pet(pet)
        st.success(f"Added pet: {new_pet_name}")
    else:
        st.error("Pet name cannot be empty.")

# Show current pets
if st.session_state.owner.pets:
    st.write("### Current Pets:")
    for pet in st.session_state.owner.pets:
        st.write(f"- **{pet.name}** ({pet.species})")
else:
    st.info("No pets yet. Add one above.")

st.divider()


# ---------------------------------------------------------
# Add Tasks
# ---------------------------------------------------------
st.subheader("Add a Task")

if st.session_state.owner.pets:
    pet_names = [pet.name for pet in st.session_state.owner.pets]
    selected_pet = st.selectbox("Assign to Pet", pet_names)

    task_desc = st.text_input("Task description", value="Morning walk")
    task_time = st.text_input("Task time (HH:MM)", value="08:00")
    task_freq = st.selectbox("Frequency", ["once", "daily", "weekly"])

    if st.button("Add Task"):
        pet = st.session_state.owner.get_pet(selected_pet)
        pet.add_task(Task(task_desc, task_time, task_freq))
        st.success(f"Added task to {selected_pet}")
else:
    st.info("Add a pet first to assign tasks.")

st.divider()


# ---------------------------------------------------------
# Build Schedule
# ---------------------------------------------------------
st.subheader("Build Schedule")

if st.button("Generate schedule"):
    scheduler = Scheduler()

    # Handle recurrence for each pet
    for pet in st.session_state.owner.pets:
        scheduler.handle_recurrence(pet)

    schedule, conflicts = scheduler.build_daily_schedule(st.session_state.owner)

    st.success("Schedule generated!")

    # Display schedule
    st.markdown("### Today's Schedule")
    for item in schedule:
        st.markdown(
            f"""
            **{item['time']} — {item['description']}**  
            🐾 Pet: **{item['pet']}**  
            🔁 Frequency: {item['frequency']}  
            ✔️ Completed: {item['completed']}
            """
        )
        st.divider()

    # Display conflicts
    if conflicts:
        st.warning("⚠️ Conflicts detected!")
        for time, tasks in conflicts.items():
            st.write(f"**{time}** has {len(tasks)} tasks:")
            for t in tasks:
                st.write(f"- {t.description}")
else:
    st.caption("Click the button above to generate your schedule.")
