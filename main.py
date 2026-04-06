import schedule
import time
from scraper import fetch_jobs
from notifier import send_discord_webhook

def job():
    """Main job that scrapes and notifies."""
    print("Fetching software engineer intern jobs for US/Canada...")
    try:
        jobs_df = fetch_jobs()
        print(f"Scrape completed. Found {len(jobs_df)} total jobs.")
        send_discord_webhook(jobs_df)
    except Exception as e:
        print(f"An error occurred: {e}")

# Run immediately on start
job()

# Schedule for every hour
schedule.every(1).hours.do(job)

print("Job scheduler started. Running every hour...")

while True:
    schedule.run_pending()
    time.sleep(1)
