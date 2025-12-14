"""
Development Guide: How to Build AI Agents
"""

import streamlit as st

st.set_page_config(page_title="Development Guide", page_icon="📖", layout="wide")

st.title("📖 Agent Development Guide")
st.markdown("---")

st.header("🏗️ Agent Architecture Overview")

st.markdown("""
Building an AI agent involves several key components working together:

```
┌─────────────┐
│   Input     │  ← User query, API data, files, etc.
└──────┬──────┘
       │
┌──────▼────────────────────────┐
│   Agent Core (LLM)            │
│  - Understands intent         │
│  - Plans actions              │
│  - Makes decisions            │
└──────┬────────────────────────┘
       │
┌──────▼──────────────┐
│   Tools/Tools       │  ← Capabilities (web search, calculator, etc.)
│   - Tool 1          │
│   - Tool 2          │
│   - Tool 3          │
└──────┬──────────────┘
       │
┌──────▼──────┐
│   Actions   │  ← Execute tasks, call APIs, etc.
└──────┬──────┘
       │
┌──────▼──────┐
│   Output    │  → Results, responses, files
└─────────────┘
```

### Key Components Explained

1. **Agent Core**: The LLM that processes information and makes decisions
2. **Tools**: Functions the agent can call (search, calculate, read files, etc.)
3. **Memory**: Context retention across interactions
4. **Orchestrator**: Manages the flow between components
""")

st.markdown("---")

st.header("📝 Step-by-Step Development Process")

st.subheader("Step 1: Define the Agent's Purpose")
st.markdown("""
**What should your agent do?**

Examples:
- Analyze data and generate reports
- Answer questions from documents
- Automate web tasks
- Generate and execute code
- Monitor and respond to events

**Define clear objectives:**
- Input: What information does it need?
- Output: What should it produce?
- Constraints: Any limitations or rules?
- Success criteria: How do you measure success?
""")

st.subheader("Step 2: Choose Your Framework")
st.markdown("""
**LangChain** (Recommended for beginners):
- Large ecosystem
- Great documentation
- Many integrations
- Good for: General-purpose agents

**CrewAI**:
- Multi-agent systems
- Role-based agents
- Good for: Complex workflows with multiple agents

**AutoGen**:
- Conversational agents
- Code generation
- Good for: Research and development tasks

**LlamaIndex**:
- Document processing
- RAG applications
- Good for: Knowledge-based agents
""")

st.subheader("Step 3: Set Up Tools")
st.markdown("""
Tools extend an agent's capabilities. Common tools include:

```python
# Example: Creating tools for an agent
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper

# Web Search Tool
search = GoogleSearchAPIWrapper()
search_tool = Tool(
    name="Web Search",
    func=search.run,
    description="Search the web for current information"
)

# Calculator Tool
def calculate(expression: str) -> str:
    try:
        result = eval(expression)
        return str(result)
    except:
        return "Error calculating"

calc_tool = Tool(
    name="Calculator",
    func=calculate,
    description="Evaluate mathematical expressions"
)

# File Reader Tool
def read_file(file_path: str) -> str:
    with open(file_path, 'r') as f:
        return f.read()

file_tool = Tool(
    name="File Reader",
    func=read_file,
    description="Read contents of a text file"
)
```
""")

st.subheader("Step 4: Initialize the Agent")
st.markdown("""
```python
from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI
from langchain.memory import ConversationBufferMemory

# Initialize LLM
llm = OpenAI(temperature=0)

# Create memory
memory = ConversationBufferMemory(
    memory_key="chat_history",
    return_messages=True
)

# Initialize agent with tools
agent = initialize_agent(
    tools=[search_tool, calc_tool, file_tool],
    llm=llm,
    agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION,
    memory=memory,
    verbose=True  # Shows reasoning process
)

# Use the agent
response = agent.run("What is the weather in San Francisco?")
print(response)
```
""")

st.subheader("Step 5: Add Memory/Context")
st.markdown("""
Agents need memory to maintain context:

**Types of Memory:**
1. **Conversation Buffer**: Stores entire conversation
2. **Conversation Summary**: Summarizes past conversations
3. **Vector Store**: Semantic search over past interactions
4. **Entity Memory**: Tracks specific entities mentioned

```python
from langchain.memory import ConversationSummaryBufferMemory

memory = ConversationSummaryBufferMemory(
    llm=llm,
    max_token_limit=2000,
    return_messages=True
)

# Memory automatically stores and retrieves context
```
""")

st.subheader("Step 6: Implement Error Handling")
st.markdown("""
```python
import logging
import time
from typing import Optional

def safe_agent_run(agent, query: str, max_retries: int = 3) -> Optional[str]:
    # Run agent with error handling and retries
    for attempt in range(max_retries):
        try:
            response = agent.run(query)
            return response
        except Exception as e:
            logging.error(f"Attempt {attempt + 1} failed: {str(e)}")
            if attempt == max_retries - 1:
                return f"Error: Unable to process query after {max_retries} attempts"
            time.sleep(1)  # Wait before retry
    return None

# Usage
result = safe_agent_run(agent, user_query)
```
""")

st.subheader("Step 7: Test and Iterate")
st.markdown("""
**Testing Checklist:**
- [ ] Handles expected inputs correctly
- [ ] Gracefully handles errors
- [ ] Maintains context across interactions
- [ ] Uses appropriate tools
- [ ] Produces accurate outputs
- [ ] Performs within acceptable time limits

**Iteration Tips:**
- Start with simple cases
- Add complexity gradually
- Monitor token usage (costs)
- Collect user feedback
- Optimize tool descriptions for better tool selection
""")

st.markdown("---")

st.header("🎯 Best Practices")

col1, col2 = st.columns(2)

with col1:
    st.subheader("✅ DO")
    st.markdown("""
    - Define clear, specific tool descriptions
    - Use appropriate temperature (0 for deterministic, 0.7+ for creative)
    - Implement proper error handling
    - Log agent actions for debugging
    - Set token limits to control costs
    - Test with edge cases
    - Use streaming for better UX
    - Validate inputs and outputs
    """)

with col2:
    st.subheader("❌ DON'T")
    st.markdown("""
    - Don't expose sensitive APIs without authentication
    - Don't let agents run arbitrary code without sandboxing
    - Don't ignore rate limits
    - Don't hardcode API keys
    - Don't skip error handling
    - Don't use high temperature for critical tasks
    - Don't forget to handle timeouts
    - Don't ignore memory constraints
    """)

st.markdown("---")

st.header("🔍 Debugging Tips")

st.markdown("""
1. **Enable Verbose Mode**: See agent's reasoning process
   ```python
   agent = initialize_agent(..., verbose=True)
   ```

2. **Log Tool Calls**: Track which tools are used
   ```python
   import logging
   logging.basicConfig(level=logging.INFO)
   ```

3. **Test Tools Individually**: Ensure each tool works in isolation

4. **Inspect Prompts**: Check what's sent to the LLM
   ```python
   print(agent.agent.llm_chain.prompt.template)
   ```

5. **Monitor Token Usage**: Track costs and performance
   ```python
   from langchain.callbacks import get_openai_callback
   
   with get_openai_callback() as cb:
       result = agent.run(query)
       print(f"Total Tokens: {cb.total_tokens}")
       print(f"Total Cost: ${cb.total_cost}")
   ```

6. **Use Smaller Models for Testing**: Save costs during development
""")

st.markdown("---")

st.header("📊 Common Patterns")

pattern_examples = {
    "ReAct Pattern": """
Agent uses Reasoning + Acting:
1. Thinks about the problem
2. Decides which tool to use
3. Observes the result
4. Thinks again
5. Repeats until goal is achieved
    """,
    
    "RAG Pattern": """
Retrieval Augmented Generation:
1. User query comes in
2. Search relevant documents (vector search)
3. Retrieve context
4. Pass context + query to LLM
5. Generate response with citations
    """,
    
    "Multi-Agent Pattern": """
Multiple specialized agents:
1. Orchestrator agent receives task
2. Delegates to specialist agents
3. Agents collaborate/communicate
4. Results synthesized
5. Final output returned
    """,
    
    "Planning Pattern": """
Agent creates a plan first:
1. Break goal into sub-tasks
2. Create execution plan
3. Execute plan step by step
4. Adapt if needed
5. Return final result
    """
}

for pattern, description in pattern_examples.items():
    with st.expander(f"📐 {pattern}"):
        st.code(description.strip())

st.markdown("---")

st.info("""
💡 **Next Step**: Check out the **Examples** page to see these concepts in action 
with working code you can run!
""")


