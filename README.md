# 🛡️ Community Moderation Bot

A Python-based moderation bot for VK, a large social networking platform.

The bot automates community moderation by monitoring messages and detecting restricted content before it can cause moderation issues.

## 🛠 Tech Stack

- Python
- VK API
- Docker
- Docker Compose

## 🚀 Key Features

- Automated message moderation
- Restricted-word detection
- Community protection against problematic content
- Automatic processing of incoming messages
- Designed for continuous deployment

## 📦 Local Setup

### Clone the Repository

```bash
git clone https://github.com/miaaa1337/vk_bot.git
cd vk_bot
```

###Install Dependencies
```bash
pip install -r requirements.txt
```

###Configure Environment Variables
Create the required environment variables for your VK API credentials.
###Run
```bash
python main.py
```

###🐳 Docker
The project includes Docker configuration for reproducible deployment.
```bash
docker-compose up --build -d
```

###📌 About VK

VK is a large social networking platform with community and messaging features.
This project uses its API to automate moderation workflows for online communities.









