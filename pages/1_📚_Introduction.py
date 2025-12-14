"""
Introduction Page: What is an AI Agent?
"""

import streamlit as st

st.set_page_config(page_title="Introduction - AI Agents", page_icon="📚", layout="wide")

st.title("📚 Introduction: What is an AI Agent?")
st.markdown("---")

col1, col2 = st.columns([2, 1])

with col1:
    st.header("🤖 Understanding AI Agents")
    
    st.markdown("""
    ### Definition
    
    An **AI Agent** is an autonomous software program that:
    - Perceives its environment through inputs (data, APIs, user queries)
    - Makes decisions based on predefined goals or objectives
    - Takes actions to achieve those goals
    - Learns and adapts from feedback (in some cases)
    
    ### Key Characteristics
    
    1. **Autonomy**: Operates independently without constant human intervention
    2. **Reactivity**: Responds to changes in the environment
    3. **Pro-activeness**: Takes initiative to achieve goals
    4. **Social Ability**: Can interact with other agents, systems, or humans
    """)
    
    st.header("🧩 Agent Components")
    
    st.markdown("""
    A typical AI agent consists of:
    
    1. **Sensors (Input)**: How the agent perceives the world
       - Text input, APIs, databases, files, web scraping
       
    2. **Processor (Brain)**: The decision-making engine
       - LLM (Large Language Model) like GPT-4, Claude, Llama
       - Rules, logic, or trained models
       
    3. **Actuators (Output)**: How the agent acts on the world
       - API calls, file operations, database writes, tool execution
       
    4. **Memory**: Context retention
       - Short-term (current conversation)
       - Long-term (vector databases, databases)
       
    5. **Tools**: Capabilities the agent can use
       - Web search, calculators, code execution, API calls
    """)

with col2:
    st.markdown("""
    ### 🎯 Agent vs Traditional Programs
    
    **Traditional Program:**
    ```
    Input → Fixed Logic → Output
    ```
    
    **AI Agent:**
    ```
    Input → Reasoning/Planning → 
    Tool Selection → Action → 
    Observation → Adaptation → Goal
    ```
    """)
    
    st.info("""
    **Key Difference**: Agents use reasoning
    and can adapt their approach based on
    the situation, while traditional programs
    follow fixed logic.
    """)

st.markdown("---")

st.header("🏗️ Types of AI Agents")

col1, col2, col3 = st.columns(3)

with col1:
    st.subheader("1. Simple Reflex Agents")
    st.markdown("""
    - React to current state only
    - No memory
    - Example: Thermostat
    """)

with col2:
    st.subheader("2. Model-Based Agents")
    st.markdown("""
    - Maintain internal model of world
    - Handle partial observability
    - Example: Game-playing agent
    """)

with col3:
    st.subheader("3. Goal-Based Agents")
    st.markdown("""
    - Work towards specific goals
    - Can plan actions
    - Example: Task completion agent
    """)

col1, col2 = st.columns(2)

with col1:
    st.subheader("4. Utility-Based Agents")
    st.markdown("""
    - Maximize utility/performance
    - Optimal decision making
    - Example: Trading bot
    """)

with col2:
    st.subheader("5. Learning Agents")
    st.markdown("""
    - Improve from experience
    - Adapt behavior over time
    - Example: Recommendation system
    """)

st.markdown("---")

st.header("🎯 Real-World Applications")

examples = [
    ("🌐 Web Browsing Agent", "Automates web searches, form filling, data extraction"),
    ("📊 Data Analysis Agent", "Analyzes datasets, generates reports, finds insights"),
    ("📧 Email Assistant", "Sorts emails, drafts responses, schedules meetings"),
    ("💬 Customer Support Bot", "Answers queries, escalates issues, provides solutions"),
    ("🔍 Research Agent", "Gathers information from multiple sources, synthesizes findings"),
    ("📝 Content Creation Agent", "Writes articles, creates summaries, generates code"),
    ("🤖 Automation Agent", "Performs repetitive tasks, orchestrates workflows"),
    ("🧪 Testing Agent", "Generates test cases, validates functionality")
]

for title, desc in examples:
    st.markdown(f"**{title}**: {desc}")

st.markdown("---")

st.header("💡 Why Use AI Agents?")

st.markdown("""
1. **Automation**: Handle complex, multi-step tasks automatically
2. **Intelligence**: Make decisions based on context and goals
3. **Scalability**: Process multiple tasks concurrently
4. **Efficiency**: Reduce manual work and human errors
5. **Adaptability**: Adjust to new scenarios without code changes
6. **Integration**: Connect different systems and tools seamlessly

---

### 🎓 Next Steps

Ready to start building? Navigate to:
- **2️⃣ Prerequisites**: Set up your development environment
- **3️⃣ Development Guide**: Learn how to build agents
- **4️⃣ Examples**: See working agent implementations
""")


