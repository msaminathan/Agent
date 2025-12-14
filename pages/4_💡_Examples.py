"""
Examples Page: Working Agent Implementations
"""

import streamlit as st
import os
from typing import Optional

st.set_page_config(page_title="Agent Examples", page_icon="💡", layout="wide")

st.title("💡 Agent Examples")
st.markdown("---")

st.markdown("""
This page contains **real, working examples** of AI agents you can run.
Each example includes code explanations and can be executed directly.
""")

st.markdown("---")

# Example 1: Simple Calculator Agent
with st.expander("🔢 Example 1: Calculator Agent (Simple)", expanded=True):
    st.subheader("Description")
    st.markdown("""
    A basic agent that performs mathematical calculations. This demonstrates:
    - Simple tool creation
    - Agent initialization
    - Basic interaction
    """)
    
    st.subheader("Code")
    code1 = """from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI
from langchain.tools import Tool
import os

# Simple calculator function
def calculate(expression: str) -> str:
    '''Evaluate a mathematical expression safely'''
    try:
        # Simple safety check
        allowed_chars = set('0123456789+-*/(). ')
        if not all(c in allowed_chars for c in expression):
            return "Error: Invalid characters"
        result = eval(expression)
        return str(result)
    except Exception as e:
        return f"Error: {str(e)}"

# Create calculator tool
calc_tool = Tool(
    name="Calculator",
    func=calculate,
    description="Evaluates mathematical expressions. Input should be a valid expression like '2 + 2' or '10 * 5'"
)

# Initialize agent (requires OPENAI_API_KEY)
llm = OpenAI(temperature=0)
agent = initialize_agent(
    tools=[calc_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Run agent
response = agent.run("What is 123 * 456?")
print(response)
"""
    st.code(code1, language="python")
    
    st.subheader("Try it!")
    if st.button("Run Calculator Agent Example", key="calc_example"):
        st.info("💡 To run this example, set your OPENAI_API_KEY and execute the code above.")

# Example 2: Web Research Agent
with st.expander("🌐 Example 2: Web Research Agent"):
    st.subheader("Description")
    st.markdown("""
    An agent that searches the web for information and provides answers.
    Demonstrates:
    - Web search tool integration
    - Information synthesis
    - Tool chaining
    """)
    
    st.subheader("Code")
    code2 = """from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI
from langchain.tools import Tool
from langchain.utilities import GoogleSearchAPIWrapper
import os

# Web search tool (requires GOOGLE_API_KEY and GOOGLE_CSE_ID)
search = GoogleSearchAPIWrapper()
search_tool = Tool(
    name="Google Search",
    func=search.run,
    description="Search Google for current information. Useful for finding recent data, news, or facts."
)

# Initialize agent
llm = OpenAI(temperature=0)
agent = initialize_agent(
    tools=[search_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Research a topic
response = agent.run("What are the latest developments in AI agents in 2024?")
print(response)
"""
    st.code(code2, language="python")
    
    st.info("""
    **Setup Required:**
    1. Get Google API key and Custom Search Engine ID
    2. Set environment variables:
       - `GOOGLE_API_KEY`
       - `GOOGLE_CSE_ID`
    """)

# Example 3: Document Q&A Agent
with st.expander("📄 Example 3: Document Question-Answering Agent"):
    st.subheader("Description")
    st.markdown("""
    An agent that answers questions based on document content.
    Uses RAG (Retrieval Augmented Generation) pattern.
    """)
    
    st.subheader("Code")
    code3 = """from langchain.document_loaders import TextLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os

# Load and process document
loader = TextLoader("document.txt")
documents = loader.load()

# Split into chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
texts = text_splitter.split_documents(documents)

# Create embeddings and vector store
embeddings = OpenAIEmbeddings()
vectorstore = Chroma.from_documents(texts, embeddings)

# Create QA chain
llm = OpenAI(temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vectorstore.as_retriever()
)

# Ask questions
query = "What is the main topic of this document?"
answer = qa_chain.run(query)
print(answer)
"""
    st.code(code3, language="python")

# Example 4: Data Analysis Agent
with st.expander("📊 Example 4: Data Analysis Agent"):
    st.subheader("Description")
    st.markdown("""
    An agent that analyzes CSV data and answers questions about it.
    Uses pandas for data manipulation.
    """)
    
    st.subheader("Code")
    code4 = """from langchain.agents import create_pandas_dataframe_agent
from langchain.llms import OpenAI
import pandas as pd
import os

# Load data
df = pd.read_csv("data.csv")

# Create agent with pandas tools
llm = OpenAI(temperature=0)
agent = create_pandas_dataframe_agent(
    llm=llm,
    df=df,
    verbose=True
)

# Ask questions about the data
questions = [
    "What are the column names?",
    "What is the average value in column X?",
    "Show me the top 5 rows",
    "Create a summary of the data"
]

for question in questions:
    response = agent.run(question)
    print(f"Q: {question}")
    print(f"A: {response}\\n")
"""
    st.code(code4, language="python")

# Example 5: Code Generation Agent
with st.expander("💻 Example 5: Code Generation Agent"):
    st.subheader("Description")
    st.markdown("""
    An agent that generates and can execute Python code.
    Uses Python REPL tool.
    """)
    
    st.subheader("Code")
    code5 = """from langchain.agents import initialize_agent, AgentType
from langchain.llms import OpenAI
from langchain.tools import PythonREPLTool
import os

# Python REPL tool (use with caution - can execute arbitrary code)
python_tool = PythonREPLTool()

# Initialize agent
llm = OpenAI(temperature=0)
agent = initialize_agent(
    tools=[python_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

# Generate and execute code
response = agent.run(
    "Write Python code to calculate the factorial of 10 and print the result"
)
print(response)
"""
    st.code(code5, language="python")
    
    st.warning("⚠️ **Security Note**: Code execution agents can run arbitrary code. Use with caution and consider sandboxing.")

# Example 6: Multi-Agent System (CrewAI)
with st.expander("👥 Example 6: Multi-Agent System (CrewAI)"):
    st.subheader("Description")
    st.markdown("""
    A system with multiple specialized agents working together.
    Uses CrewAI framework.
    """)
    
    st.subheader("Code")
    code6 = """from crewai import Agent, Task, Crew
from langchain.llms import OpenAI
import os

# Define agents with specific roles
researcher = Agent(
    role='Research Analyst',
    goal='Research and gather information on given topics',
    backstory='You are an expert researcher who finds accurate information',
    verbose=True
)

writer = Agent(
    role='Content Writer',
    goal='Write engaging content based on research',
    backstory='You are a skilled writer who creates compelling narratives',
    verbose=True
)

# Define tasks
research_task = Task(
    description='Research the history of AI agents',
    agent=researcher
)

write_task = Task(
    description='Write a 500-word article based on the research',
    agent=writer
)

# Create crew and execute
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    verbose=True
)

result = crew.kickoff()
print(result)
"""
    st.code(code6, language="python")
    
    st.info("💡 Install CrewAI: `pip install crewai crewai-tools`")

st.markdown("---")

st.header("🚀 Running Examples")

st.markdown("""
### Prerequisites:
1. Set up your environment (see Prerequisites page)
2. Install required packages:
   ```bash
   pip install langchain openai langchain-community
   pip install chromadb  # For vector stores
   pip install pandas    # For data analysis
   ```
3. Set API keys in `.env` file or environment:
   ```bash
   export OPENAI_API_KEY="your-key-here"
   ```

### Create Example Files:
""")

example_scripts = {
    "example_calculator.py": code1.split("print(response)")[0] + "\n# Example usage\nresponse = agent.run('What is 25 * 37?')\nprint(response)",
    "example_research.py": code2.split("print(response)")[0] + "\n# Example usage\nresponse = agent.run('What is machine learning?')\nprint(response)",
    "example_qa.py": code3,
    "example_data_analysis.py": code4,
    "example_codegen.py": code5.split("print(response)")[0] + "\n# Example usage\nresponse = agent.run('Create a list of first 10 Fibonacci numbers')\nprint(response)",
}

if st.button("💾 Generate Example Scripts"):
    os.makedirs("examples", exist_ok=True)
    for filename, content in example_scripts.items():
        with open(f"examples/{filename}", "w") as f:
            f.write(content)
    st.success("✅ Example scripts created in `examples/` directory!")

st.markdown("---")

st.header("📚 Additional Resources")

st.markdown("""
- **LangChain Documentation**: https://python.langchain.com/
- **CrewAI Documentation**: https://docs.crewai.com/
- **AutoGen Documentation**: https://microsoft.github.io/autogen/
- **LlamaIndex Documentation**: https://docs.llamaindex.ai/

**Practice Ideas:**
- Create a personal assistant agent
- Build a customer service bot
- Develop an automation agent for repetitive tasks
- Create a code review agent
- Build a content moderation agent
""")


