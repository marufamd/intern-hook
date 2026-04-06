# Software Engineer Intern Job Webhook

An automated hourly Discord notification system that scrapes the latest software engineering internships in the United States and Canada using the [JobSpy](https://github.com/cullenwatson/JobSpy) library.

## Features
- **Hourly Updates**: Scrapes and sends new internships posted within the last hour.
- **US & Canada Coverage**: Aggregates results from both countries.
- **Multi-Source Scraping**: Pulls from LinkedIn, Indeed, Glassdoor, Google Jobs, and ZipRecruiter.
- **Discord Integration**: Sends nicely formatted Discord embeds using `discord.py`.
- **Dockerized**: Easy to deploy and run in the background.

## Prerequisites
- Docker and Docker Compose (Recommended)
- OR Python 3.10+ and a Discord Webhook URL

## Getting Started

### 1. Set Up Your Webhook
1. Go to your Discord server's settings.
2. Select **Integrations** > **Webhooks** > **New Webhook**.
3. Copy the **Webhook URL**.

### 2. Configuration
Create a `.env` file in the project root:
```bash
cp .env.template .env
```
Open `.env` and replace `your_discord_webhook_url_here` with your actual Discord Webhook URL.

### 3. Run with Docker (Recommended)
This is the easiest way to keep the bot running 24/7.
```bash
docker-compose up -d --build
```
This will build the image and start the container in detached mode.

### 4. Run Locally (Alternative)
If you prefer to run it without Docker:
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Start the script:
   ```bash
   python main.py
   ```

## Project Structure
- `scraper.py`: Handles job fetching logic using JobSpy.
- `notifier.py`: Formats and sends job notifications to Discord.
- `main.py`: Schedules the hourly scraping job.
- `Dockerfile` & `docker-compose.yml`: Containerization configuration.

## Customizing the Search
To change the search terms or locations, modify the `search_params` in `scraper.py`.

## License
MIT
