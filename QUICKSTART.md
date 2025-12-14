# 🚀 Quick Start Guide

Get up and running with the AI Agents tutorial in 5 minutes!

## Step 1: Clone/Navigate to Project

```bash
cd Agents
```

## Step 2: Run Setup Script (Optional but Recommended)

```bash
chmod +x setup.sh
./setup.sh
```

This will:
- Check Python installation
- Create virtual environment
- Install dependencies
- Create .env file template

## Step 3: Manual Setup (If not using script)

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

## Step 4: Configure API Keys (Optional)

For running examples that use LLMs, you'll need API keys:

1. Get an API key from one of these providers:
   - OpenAI: https://platform.openai.com/api-keys
   - Anthropic: https://console.anthropic.com/
   - Google: https://makersuite.google.com/app/apikey

2. Create `.env` file:
   ```bash
   cp .env.example .env
   # Edit .env and add your keys
   ```

   Or manually:
   ```bash
   echo "OPENAI_API_KEY=your_key_here" > .env
   ```

**Note**: The app itself works without API keys! You just can't run the interactive examples.

## Step 5: Run the Application

```bash
streamlit run app.py
```

The app will open automatically in your browser at `http://localhost:8501`

## Step 6: Explore!

1. Start with **"1️⃣ Introduction"** to learn what agents are
2. Check **"2️⃣ Prerequisites"** for complete setup instructions
3. Read **"3️⃣ Development Guide"** to learn how to build agents
4. Try **"4️⃣ Examples"** to see working code
5. Review **"5️⃣ Deployment"** when ready to deploy

## Troubleshooting

### Import Errors
```bash
# Make sure virtual environment is activated
source venv/bin/activate

# Reinstall dependencies
pip install -r requirements.txt
```

### Port Already in Use
```bash
streamlit run app.py --server.port 8502
```

### API Key Issues
- Make sure .env file is in the project root
- Check that python-dotenv is installed: `pip install python-dotenv`
- Verify key is correct (no extra spaces)

### Module Not Found
```bash
# Make sure you're in the virtual environment
which python  # Should show .../venv/bin/python

# Reinstall all packages
pip install --upgrade -r requirements.txt
```

## Next Steps

- ✅ Run through all the tutorial pages
- ✅ Try modifying the example code
- ✅ Build your own simple agent
- ✅ Deploy your agent using the deployment guide

## Getting Help

- Check the main README.md
- Review each page in the app for detailed information
- Consult framework documentation:
  - [LangChain Docs](https://python.langchain.com/)
  - [Streamlit Docs](https://docs.streamlit.io/)

Happy learning! 🤖


