"""
Deployment Guide: How to Deploy AI Agents
"""

import streamlit as st

st.set_page_config(page_title="Deployment Guide", page_icon="🚀", layout="wide")

st.title("🚀 Deployment Guide")
st.markdown("---")

st.header("📋 Deployment Options")

deployment_options = {
    "Streamlit Cloud": {
        "difficulty": "Easy",
        "cost": "Free tier available",
        "best_for": "Demos, prototypes, simple apps",
        "setup": "Connect GitHub repo, auto-deploys"
    },
    "Docker + Cloud": {
        "difficulty": "Medium",
        "cost": "Varies (AWS, GCP, Azure)",
        "best_for": "Production apps, scaling",
        "setup": "Containerize app, deploy to cloud"
    },
    "Local Server": {
        "difficulty": "Easy",
        "cost": "Free (your hardware)",
        "best_for": "Internal tools, testing",
        "setup": "Run Streamlit locally with systemd"
    },
    "FastAPI + Uvicorn": {
        "difficulty": "Medium",
        "cost": "Varies",
        "best_for": "API endpoints, microservices",
        "setup": "Convert to FastAPI, deploy with Uvicorn"
    }
}

for option, details in deployment_options.items():
    with st.expander(f"🌐 {option}"):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown(f"**Difficulty**: {details['difficulty']}")
            st.markdown(f"**Cost**: {details['cost']}")
        with col2:
            st.markdown(f"**Best For**: {details['best_for']}")
            st.markdown(f"**Setup**: {details['setup']}")

st.markdown("---")

st.header("📦 Option 1: Deploy to Streamlit Cloud (Easiest)")

st.subheader("Step 1: Prepare Your Repository")
st.code("""
# Ensure your repo structure:
Agents/
├── app.py                 # Main Streamlit app
├── pages/                 # Streamlit pages
│   ├── 1_📚_Introduction.py
│   └── ...
├── requirements.txt       # Python dependencies
├── .streamlit/
│   └── config.toml       # Optional: Streamlit config
└── README.md
""", language="bash")

st.subheader("Step 2: Create requirements.txt")
st.markdown("See the requirements.txt section below for a complete list.")

st.subheader("Step 3: Push to GitHub")
st.code("""
# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/yourusername/yourrepo.git
git push -u origin main
""", language="bash")

st.subheader("Step 4: Deploy on Streamlit Cloud")
st.markdown("""
1. Go to https://share.streamlit.io/
2. Sign in with GitHub
3. Click "New app"
4. Select your repository and branch
5. Set main file path (usually `app.py`)
6. Click "Deploy"
7. Add secrets for API keys in app settings
""")

st.markdown("---")

st.header("🐳 Option 2: Docker Deployment")

st.subheader("Create Dockerfile")
dockerfile_content = """# Use Python 3.10 slim image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \\
    gcc \\
    && rm -rf /var/lib/apt/lists/*

# Copy requirements first (for better caching)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Expose Streamlit port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

# Run Streamlit
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]
"""
st.code(dockerfile_content, language="dockerfile")

st.subheader("Create .dockerignore")
dockerignore_content = """venv/
__pycache__/
*.pyc
.env
.git/
.gitignore
*.md
.DS_Store
"""
st.code(dockerignore_content, language="text")

st.subheader("Build and Run Docker Container")
st.code("""
# Build the image
docker build -t ai-agents-app .

# Run the container
docker run -p 8501:8501 \\
    -e OPENAI_API_KEY=your_key_here \\
    ai-agents-app

# Or use docker-compose (create docker-compose.yml)
""", language="bash")

st.subheader("Docker Compose Example")
docker_compose_content = """version: '3.8'

services:
  streamlit:
    build: .
    ports:
      - "8501:8501"
    environment:
      - OPENAI_API_KEY=${OPENAI_API_KEY}
      - ANTHROPIC_API_KEY=${ANTHROPIC_API_KEY}
    env_file:
      - .env
    volumes:
      - ./data:/app/data
    restart: unless-stopped
"""
st.code(docker_compose_content, language="yaml")

st.markdown("---")

st.header("🖥️ Option 3: Deploy on Ubuntu Server (Local/VPS)")

st.subheader("Step 1: System Setup")
st.code("""
# Update system
sudo apt update && sudo apt upgrade -y

# Install Python and pip
sudo apt install python3 python3-pip python3-venv -y

# Install nginx (for reverse proxy, optional)
sudo apt install nginx -y
""", language="bash")

st.subheader("Step 2: Clone and Setup Application")
st.code("""
# Clone repository
cd /opt
sudo git clone https://github.com/yourusername/yourrepo.git
sudo chown -R $USER:$USER yourrepo
cd yourrepo

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
""", language="bash")

st.subheader("Step 3: Create Systemd Service")
service_content = """[Unit]
Description=Streamlit AI Agents App
After=network.target

[Service]
Type=simple
User=your_username
WorkingDirectory=/opt/yourrepo
Environment="PATH=/opt/yourrepo/venv/bin"
EnvironmentFile=/opt/yourrepo/.env
ExecStart=/opt/yourrepo/venv/bin/streamlit run app.py --server.port=8501
Restart=always

[Install]
WantedBy=multi-user.target
"""
st.code(service_content, language="ini")

st.code("""
# Save as /etc/systemd/system/streamlit-app.service
sudo nano /etc/systemd/system/streamlit-app.service

# Enable and start service
sudo systemctl daemon-reload
sudo systemctl enable streamlit-app
sudo systemctl start streamlit-app

# Check status
sudo systemctl status streamlit-app
""", language="bash")

st.subheader("Step 4: Setup Nginx Reverse Proxy (Optional)")
nginx_config = """server {
    listen 80;
    server_name your-domain.com;

    location / {
        proxy_pass http://localhost:8501;
        proxy_http_version 1.1;
        proxy_set_header Upgrade $http_upgrade;
        proxy_set_header Connection "upgrade";
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        proxy_cache_bypass $http_upgrade;
    }
}
"""
st.code(nginx_config, language="nginx")

st.code("""
# Save to /etc/nginx/sites-available/streamlit-app
sudo nano /etc/nginx/sites-available/streamlit-app

# Create symlink
sudo ln -s /etc/nginx/sites-available/streamlit-app /etc/nginx/sites-enabled/

# Test and reload nginx
sudo nginx -t
sudo systemctl reload nginx
""", language="bash")

st.subheader("Step 5: Setup SSL with Let's Encrypt (Optional)")
st.code("""
# Install certbot
sudo apt install certbot python3-certbot-nginx -y

# Get SSL certificate
sudo certbot --nginx -d your-domain.com

# Auto-renewal is set up automatically
""", language="bash")

st.markdown("---")

st.header("🔐 Security Best Practices")

security_tips = [
    "**Environment Variables**: Never hardcode API keys. Use .env files or secret management.",
    "**API Key Restrictions**: Set up API key restrictions on provider side (IP whitelisting, rate limits).",
    "**Authentication**: Add authentication for production deployments (Streamlit-Authenticator).",
    "**HTTPS**: Always use HTTPS in production (use Let's Encrypt).",
    "**Firewall**: Configure firewall (ufw) to only allow necessary ports.",
    "**Updates**: Keep dependencies updated for security patches.",
    "**Logging**: Monitor logs for suspicious activity.",
    "**Rate Limiting**: Implement rate limiting to prevent abuse.",
    "**Sandboxing**: If agents execute code, use proper sandboxing.",
    "**Input Validation**: Validate all user inputs before processing."
]

for tip in security_tips:
    st.markdown(f"- {tip}")

st.markdown("---")

st.header("📊 Monitoring & Maintenance")

monitoring_section = """
### Logging
```python
import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('app.log'),
        logging.StreamHandler()
    ]
)
```

### Health Checks
```python
# Add to your Streamlit app
import streamlit as st

def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now().isoformat()
    }
```

### Monitoring Tools
- **Uptime Monitoring**: UptimeRobot, Pingdom
- **Application Monitoring**: Sentry, LogRocket
- **Server Monitoring**: Prometheus, Grafana
- **Cost Tracking**: Monitor API usage and costs
"""
st.markdown(monitoring_section)

st.markdown("---")

st.header("💰 Cost Optimization")

cost_tips = [
    "**Use Appropriate Models**: Use smaller/cheaper models when possible (GPT-3.5 vs GPT-4).",
    "**Caching**: Cache responses for repeated queries.",
    "**Token Limits**: Set maximum token limits per request.",
    "**Rate Limiting**: Implement user-side rate limiting.",
    "**Model Selection**: Choose models based on task complexity.",
    "**Batch Processing**: Process multiple requests together when possible.",
    "**Local Models**: Consider running local models (Ollama) for development.",
    "**Monitoring**: Track token usage and costs regularly."
]

for tip in cost_tips:
    st.markdown(f"- {tip}")

st.markdown("---")

st.header("✅ Deployment Checklist")

checklist_items = [
    "All dependencies listed in requirements.txt",
    "Environment variables documented",
    ".env file added to .gitignore",
    "API keys configured via secrets/environment",
    "Error handling implemented",
    "Logging configured",
    "Health checks added",
    "Security measures in place",
    "HTTPS enabled (production)",
    "Monitoring set up",
    "Backup strategy defined",
    "Documentation updated"
]

for item in checklist_items:
    st.checkbox(item, key=f"deploy_check_{item}")

st.success("""
✅ Once all items are checked, your agent is ready for deployment!

**Quick Test Command**: 
```bash
streamlit run app.py
```

If it runs locally, it should work in deployment too!
""")


