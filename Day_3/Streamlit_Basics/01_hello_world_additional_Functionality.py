"""
Example 1: Hello World - Understanding Script Execution

Key Teaching Points:
- Streamlit runs your script from top to bottom on every interaction
- Each widget interaction triggers a complete rerun
- This is fundamentally different from traditional web frameworks
"""

import streamlit as st
import time
import pandas as pd
from datetime import datetime

# ============ PAGE CONFIGURATION ============
st.set_page_config(
    page_title="Streamlit Demo - Script Execution",
    page_icon="🌍",
    layout="wide"
)

# ============ SIDEBAR WITH ADDITIONAL INFO ============
with st.sidebar:
    st.header("📊 App Statistics")
    
    # Track total interactions
    if "total_interactions" not in st.session_state:
        st.session_state.total_interactions = 0
    
    # Track last run time
    if "last_run" not in st.session_state:
        st.session_state.last_run = datetime.now()
    
    current_time = datetime.now()
    st.metric("Total Interactions", st.session_state.total_interactions)
    st.metric("Time since last run", f"{(current_time - st.session_state.last_run).seconds}s")
    
    st.divider()
    st.header("🛠️ Debug Info")
    show_debug = st.checkbox("Show Debug Information", value=False)
    
    st.divider()
    st.header("🎮 App Controls")
    reset_btn = st.button("Reset All Counters", use_container_width=True)

# ============ MAIN CONTENT ============

# This runs every time the app loads or user interacts
st.title("🌍 Hello Streamlit World!")

# Create tabs for better organization
tab1, tab2, tab3, tab4 = st.tabs(["📝 Basic Demo", "🔄 Rerun Visualization", "📊 Performance", "🎯 Interactive Learning"])

with tab1:
    st.write("This text appears every time the script runs.")
    
    # Add a button to demonstrate reruns
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🎉 Click Me!", use_container_width=True):
            st.write("🎉 Button was clicked! The entire script just ran again.")
            st.balloons()
            st.session_state.total_interactions += 1
    
    with col2:
        if st.button("🎈 Surprise Me!", use_container_width=True):
            st.write("🎈 Surprise! Another rerun just happened.")
            st.snow()
            st.session_state.total_interactions += 1
    
    # Add a text input to show interactive reruns
    name = st.text_input("What's your name?", placeholder="Type your name here...")
    if name:
        st.write(f"Hello, {name}! Notice how this updates as you type.")
        st.session_state.total_interactions += 1

with tab2:
    st.subheader("🔄 Visualizing Script Reruns")
    
    # Counter to visualize reruns
    if "counter" not in st.session_state:
        st.session_state.counter = 0
    
    st.session_state.counter += 1
    st.session_state.last_run = datetime.now()
    
    # Progress bar visualization
    st.write("**Script Execution Counter:**")
    progress_value = min(st.session_state.counter / 20, 1.0)
    st.progress(progress_value)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total Script Runs", st.session_state.counter)
    with col2:
        remaining = max(0, 20 - st.session_state.counter)
        st.metric("Runs until 20", remaining)
    
    # Live timestamp
    st.write(f"**Last execution:** {st.session_state.last_run.strftime('%H:%M:%S.%f')[:-3]}")
    
    # Add a slider to show reruns on value change
    st.write("---")
    st.write("**Watch reruns happen as you move this slider:**")
    slider_value = st.slider("Move me to trigger reruns", 0, 100, 50)
    st.write(f"Slider value: {slider_value}")
    
    if slider_value != 50:
        st.info(f"🔄 Slider changed to {slider_value} - this triggered a rerun!")

with tab3:
    st.subheader("📊 Performance Monitoring")
    
    # Measure execution time
    start_time = time.time()
    
    # Simulate some processing (to show execution time)
    if "processing_time" not in st.session_state:
        st.session_state.processing_time = []
    
    # Different operations to show execution cost
    with st.expander("🔍 See what runs every time"):
        st.write("These operations run on every interaction:")
        st.code("""
        - Reading from session_state
        - Creating visualizations
        - Running calculations
        - Formatting dates
        - Checking conditions
        """)
    
    # Create a simple dataframe that gets regenerated on each run
    df = pd.DataFrame({
        'Run Number': list(range(1, st.session_state.counter + 1)),
        'Timestamp': [datetime.now().strftime('%H:%M:%S')] * st.session_state.counter,
        'Random Value': [st.session_state.counter * 2] * st.session_state.counter
    })
    
    st.write("**Dataframe regenerated on every run:**")
    st.dataframe(df.tail(5), use_container_width=True)
    
    # Track execution time
    execution_time = time.time() - start_time
    st.session_state.processing_time.append(execution_time)
    
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Last Execution Time", f"{execution_time:.4f} seconds")
    with col2:
        if len(st.session_state.processing_time) > 1:
            avg_time = sum(st.session_state.processing_time[-10:]) / min(10, len(st.session_state.processing_time))
            st.metric("Avg Last 10 Runs", f"{avg_time:.4f} seconds")

with tab4:
    st.subheader("🎯 Interactive Learning")
    
    # Teaching note box
    with st.expander("🎓 Teaching Notes", expanded=True):
        st.write("""
        **Key Concepts Demonstrated:**
        - ✅ Script reruns on every interaction
        - ✅ Widgets trigger reruns when their values change
        - ✅ Session state preserves data across reruns
        - ✅ Without session_state, variables would reset every time
        """)
    
    # Quiz section
    st.write("### 📝 Test Your Understanding")
    
    quiz_question = st.radio(
        "What happens when you click a button in Streamlit?",
        options=[
            "Only the button's callback function runs",
            "The entire script runs from top to bottom",
            "Only the UI updates without running any code",
            "Nothing happens until you refresh the page"
        ],
        index=None
    )
    
    if quiz_question:
        if quiz_question == "The entire script runs from top to bottom":
            st.success("✅ Correct! Every interaction causes a complete script rerun.")
        else:
            st.error("❌ Not quite. Try again! Remember what we learned about script execution.")
    
    # Challenge section
    st.write("### 🏆 Mini Challenge")
    challenge = st.checkbox("Try to guess what will happen when you check this box")
    if challenge:
        st.info("💡 Did you notice that checking this box triggered another script rerun?")
        st.code("""
        # Every widget interaction, including checkboxes, 
        # triggers a complete script rerun!
        """)

# ============ DEBUG INFORMATION ============
if show_debug:
    st.divider()
    with st.expander("🐛 Debug Information", expanded=True):
        col1, col2, col3 = st.columns(3)
        with col1:
            st.write("**Session State Keys:**")
            st.write(list(st.session_state.keys()))
        with col2:
            st.write("**Widget Values:**")
            st.write({
                "name": name if 'name' in locals() else "Not set",
                "slider": slider_value if 'slider_value' in locals() else "Not set"
            })
        with col3:
            st.write("**App Info:**")
            st.write(f"Total Runs: {st.session_state.counter}")
            st.write(f"Interactions: {st.session_state.total_interactions}")

# ============ RESET FUNCTIONALITY ============
if reset_btn:
    for key in list(st.session_state.keys()):
        if key not in ["total_interactions"]:  # Keep some stats
            del st.session_state[key]
    st.session_state.counter = 0
    st.session_state.processing_time = []
    st.rerun()

# ============ FOOTER ============
st.divider()
session_id = str(hash(st.session_state.get('_script_run_id', 'N/A')))
st.caption(f"🏃‍♂️ Script executed at {datetime.now().strftime('%H:%M:%S.%f')[:-3]} | "
           f"Total runs: {st.session_state.counter} | "
           f"Session ID: {session_id[:8]}")

# Optional: Add a warning about infinite loops
if st.session_state.counter > 50:
    st.warning("⚠️ You've triggered many reruns! In a real app, be careful about operations that could cause infinite loops.")