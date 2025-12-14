# 🤖 AI Agents: Complete Guide & Tutorial

A comprehensive Streamlit multipage application for learning and building AI agents. This app covers everything from understanding what AI agents are to deploying them in production.

## 📚 What's Included

This application provides:

1. **Introduction**: Understanding AI agents, their types, and real-world applications
2. **Prerequisites**: Complete setup guide for Ubuntu, including all required software and libraries
3. **Development Guide**: Step-by-step process for building agents with best practices
4. **Examples**: Working code examples for various types of agents
5. **Deployment**: Multiple deployment options with detailed instructions

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Ubuntu 20.04+ (or any Linux distribution)

### Installation

1. **Clone or navigate to this repository**
   ```bash
   cd Agents
   ```

2. **Create a virtual environment** (recommended)
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables** (optional, for running examples)
   ```bash
   # Create .env file
   touch .env
   
   # Add your API keys (optional)
   echo "OPENAI_API_KEY=your_key_here" >> .env
   echo "ANTHROPIC_API_KEY=your_key_here" >> .env
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

6. **Access the app**
   - Open your browser to `http://localhost:8501`
   - Navigate through pages using the sidebar

## 📖 Application Structure

```
Agents/
├── app.py                      # Main Streamlit application
├── pages/                      # Multipage structure
│   ├── 1_📚_Introduction.py   # What are AI agents?
│   ├── 2_🛠️_Prerequisites.py  # Setup guide
│   ├── 3_📖_Development_Guide.py  # How to build agents
│   ├── 4_💡_Examples.py       # Working examples
│   └── 5_🚀_Deployment.py     # Deployment guide
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

## 🔑 Key Features

### Educational Content
- Comprehensive explanation of AI agents
- Different types of agents and their use cases
- Agent architecture and components

### Practical Examples
- Calculator agent
- Web research agent
- Document Q&A agent
- Data analysis agent
- Code generation agent
- Multi-agent systems

### Development Guidance
- Step-by-step development process
- Best practices and patterns
- Debugging tips
- Common pitfalls to avoid

### Deployment Options
- Streamlit Cloud (easiest)
- Docker containers
- Ubuntu server deployment
- Security best practices

## 🛠️ Technologies Used

- **Streamlit**: Web application framework
- **LangChain**: Agent framework
- **CrewAI**: Multi-agent framework
- **OpenAI/Anthropic**: LLM providers
- **ChromaDB**: Vector database
- **Pandas**: Data processing

## 📝 Notes

- **API Keys**: Some examples require API keys (OpenAI, Anthropic, Google). You can still use the app to learn without keys, but examples won't run.
- **Costs**: Running agents with LLM APIs incurs costs. Monitor your usage.
- **Local Alternatives**: Consider using Ollama for local LLM models (free, runs on your machine).

## 🔒 Security

- Never commit API keys to version control
- Use environment variables for sensitive information
- Follow security best practices outlined in the Deployment page

## 📚 Additional Resources

- [LangChain Documentation](https://python.langchain.com/)
- [CrewAI Documentation](https://docs.crewai.com/)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [OpenAI API Documentation](https://platform.openai.com/docs)

## 🤝 Contributing

Feel free to extend this application with:
- More agent examples
- Additional frameworks
- UI improvements
- Better documentation

## 📄 License

This project is open source and available for educational purposes.

## 💡 Tips for Learning

1. **Start with Introduction**: Understand the concepts first
2. **Follow Prerequisites**: Set up your environment properly
3. **Study Examples**: See how agents are built in practice
4. **Experiment**: Modify examples and see what happens
5. **Build Your Own**: Start with simple agents and gradually increase complexity

## 🆘 Troubleshooting

### Common Issues

**Import Errors**: Make sure all dependencies are installed
```bash
pip install -r requirements.txt
```

**API Key Errors**: Check your .env file or environment variables
```bash
export OPENAI_API_KEY=your_key_here
```

**Port Already in Use**: Streamlit runs on port 8501 by default
```bash
streamlit run app.py --server.port 8502
```

## 🎯 Next Steps

1. Explore all pages of the application
2. Run the example code
3. Modify examples to suit your needs
4. Build your own agent
5. Deploy your agent

---

**Happy Learning! 🤖**

For questions or issues, please refer to the documentation in each page or check the framework-specific documentation.


