"""
Main Streamlit Application for AI Agents Tutorial
A comprehensive guide to understanding and building AI agents
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="AI Agents Tutorial",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Main title
st.title("🤖 AI Agents: Complete Guide & Tutorial")
st.markdown("---")

st.markdown("""
### Welcome to the AI Agents Learning Platform!

This multipage application will guide you through:
- 📚 Understanding what AI agents are
- 🛠️ Setting up your development environment
- 💡 Learning agent architecture and concepts
- 🔨 Building practical agent examples
- 🚀 Deploying agents in production

**Navigate using the sidebar** to explore different sections.

---

### What You'll Learn

1. **Agent Fundamentals**: Core concepts, architecture, and types of agents
2. **Development Environment**: All software and libraries needed on Ubuntu
3. **Practical Examples**: Real-world agents you can build and run
4. **Step-by-Step Guides**: Detailed tutorials for creating your own agents
5. **Deployment**: How to deploy agents to production

### Quick Start

If you're new to AI agents, start with **"1️⃣ Introduction"** from the sidebar.
If you're ready to code, jump to **"4️⃣ Examples"** to see working agents.
""")

st.markdown("---")
st.info("💡 **Tip**: Each page contains interactive examples and code snippets you can run directly!")


