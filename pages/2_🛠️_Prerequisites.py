"""
Prerequisites Page: Software Setup for Ubuntu
"""

import streamlit as st

st.set_page_config(page_title="Prerequisites - Setup", page_icon="🛠️", layout="wide")

st.title("🛠️ Prerequisites & Software Setup")
st.markdown("---")

st.header("📋 Ubuntu System Requirements")

col1, col2 = st.columns(2)

with col1:
    st.subheader("✅ Minimum Requirements")
    st.markdown("""
    - **OS**: Ubuntu 20.04 LTS or later
    - **RAM**: 4GB minimum (8GB recommended)
    - **Storage**: 20GB free space
    - **Python**: 3.8 or higher
    """)

with col2:
    st.subheader("⚡ Recommended")
    st.markdown("""
    - **OS**: Ubuntu 22.04 LTS
    - **RAM**: 16GB or more
    - **Storage**: 50GB+ (for models)
    - **GPU**: NVIDIA GPU with CUDA (optional, for local models)
    """)

st.markdown("---")

st.header("🐍 Python & Package Manager Setup")

st.subheader("1. Install Python 3.10+")
st.code("""
# Check current Python version
python3 --version

# If needed, install Python 3.10+
sudo apt update
sudo apt install python3.10 python3.10-venv python3-pip

# Install python3-venv if not present
sudo apt install python3-venv
""", language="bash")

st.subheader("2. Create Virtual Environment (Best Practice)")
st.code("""
# Create project directory
mkdir ~/ai_agents_project
cd ~/ai_agents_project

# Create virtual environment
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Your prompt should now show (venv)
""", language="bash")

st.info("💡 **Tip**: Always activate your virtual environment before installing packages or running code!")

st.markdown("---")

st.header("📦 Essential Python Libraries")

st.subheader("Core Agent Frameworks")

frameworks = {
    "LangChain": {
        "description": "Most popular framework for building LLM applications",
        "install": "pip install langchain langchain-openai langchain-community",
        "use_case": "General-purpose agents, chains, tools"
    },
    "CrewAI": {
        "description": "Framework for creating collaborative AI agents",
        "install": "pip install crewai crewai-tools",
        "use_case": "Multi-agent systems, role-based agents"
    },
    "AutoGen": {
        "description": "Microsoft's framework for multi-agent conversations",
        "install": "pip install pyautogen",
        "use_case": "Conversational agents, code generation"
    },
    "LlamaIndex": {
        "description": "Data framework for LLM applications",
        "install": "pip install llama-index",
        "use_case": "RAG (Retrieval Augmented Generation), document agents"
    },
    "Haystack": {
        "description": "End-to-end NLP framework",
        "install": "pip install haystack-ai",
        "use_case": "Question answering, document search"
    }
}

for framework, info in frameworks.items():
    with st.expander(f"📚 {framework}"):
        st.markdown(f"**Description**: {info['description']}")
        st.markdown(f"**Install**: `{info['install']}`")
        st.markdown(f"**Use Case**: {info['use_case']}")

st.subheader("LLM Providers & APIs")

llm_providers = {
    "OpenAI": {
        "install": "pip install openai",
        "models": "GPT-4, GPT-3.5-turbo",
        "cost": "Pay per token"
    },
    "Anthropic (Claude)": {
        "install": "pip install anthropic",
        "models": "Claude 3 Opus, Sonnet, Haiku",
        "cost": "Pay per token"
    },
    "Google (Gemini)": {
        "install": "pip install google-generativeai",
        "models": "Gemini Pro, Gemini Ultra",
        "cost": "Free tier available"
    },
    "Ollama (Local)": {
        "install": "curl -fsSL https://ollama.ai/install.sh | sh",
        "models": "Llama 2, Mistral, CodeLlama (runs locally)",
        "cost": "Free, runs on your machine"
    },
    "Hugging Face": {
        "install": "pip install transformers huggingface-hub",
        "models": "Thousands of open-source models",
        "cost": "Free for most models"
    }
}

for provider, info in llm_providers.items():
    with st.expander(f"🤖 {provider}"):
        st.markdown(f"**Install**: `{info['install']}`")
        st.markdown(f"**Models**: {info['models']}")
        st.markdown(f"**Cost**: {info['cost']}")

st.markdown("---")

st.header("🔧 Supporting Libraries")

st.subheader("Data & Processing")
st.code("""
pip install pandas numpy requests beautifulsoup4
pip install pypdf python-docx openpyxl  # Document processing
""", language="bash")

st.subheader("Vector Databases (for RAG)")
st.code("""
# ChromaDB (easy to use, in-memory)
pip install chromadb

# Pinecone (cloud-based, scalable)
pip install pinecone-client

# FAISS (Facebook AI Similarity Search)
pip install faiss-cpu  # or faiss-gpu for GPU support

# Weaviate
pip install weaviate-client
""", language="bash")

st.subheader("Web Scraping & Tools")
st.code("""
pip install selenium playwright  # Browser automation
pip install playwright  # Modern web automation
playwright install  # Install browser binaries
""", language="bash")

st.subheader("API & HTTP Clients")
st.code("""
pip install httpx aiohttp  # Async HTTP clients
pip install fastapi uvicorn  # For building agent APIs
""", language="bash")

st.markdown("---")

st.header("🌐 Additional Software")

st.subheader("Git (Version Control)")
st.code("""
sudo apt install git
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
""", language="bash")

st.subheader("Docker (Optional, for containerization)")
st.code("""
# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add user to docker group (optional)
sudo usermod -aG docker $USER

# Install Docker Compose
sudo apt install docker-compose
""", language="bash")

st.subheader("Node.js (For some tools)")
st.code("""
# Install Node.js via nvm (recommended)
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.0/install.sh | bash
source ~/.bashrc
nvm install --lts
""", language="bash")

st.markdown("---")

st.header("🔐 Environment Variables & API Keys")

st.markdown("""
Many agent frameworks require API keys. Store them securely:

### Create .env file
```bash
# In your project directory
touch .env
```

### Add your keys
```env
OPENAI_API_KEY=your_key_here
ANTHROPIC_API_KEY=your_key_here
GOOGLE_API_KEY=your_key_here
PINECONE_API_KEY=your_key_here
```

### Install python-dotenv
```bash
pip install python-dotenv
```

### Load in Python
```python
from dotenv import load_dotenv
load_dotenv()
import os
api_key = os.getenv("OPENAI_API_KEY")
```
""")

st.warning("⚠️ **Security**: Never commit .env files to Git! Add `.env` to `.gitignore`")

st.markdown("---")

st.header("✅ Quick Setup Checklist")

checklist = st.container()

with checklist:
    st.markdown("""
    - [ ] Python 3.8+ installed
    - [ ] Virtual environment created and activated
    - [ ] Core framework installed (LangChain, CrewAI, etc.)
    - [ ] LLM provider API key obtained
    - [ ] python-dotenv installed for environment variables
    - [ ] .env file created with API keys
    - [ ] Git installed and configured
    - [ ] (Optional) Docker installed
    - [ ] (Optional) Vector database installed
    """)

st.markdown("---")

st.header("🧪 Verify Installation")

st.code("""
# Test Python
python3 --version

# Test pip
pip --version

# Test virtual environment
which python  # Should point to venv/bin/python when activated

# Test LangChain (if installed)
python3 -c "import langchain; print('LangChain version:', langchain.__version__)"

# Test OpenAI (if installed and configured)
python3 -c "from openai import OpenAI; print('OpenAI SDK loaded')"
""", language="bash")

st.success("✅ Once all checks pass, you're ready to start building agents!")


