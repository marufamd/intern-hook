import os
import discord
import pandas as pd
from discord import SyncWebhook, Embed
from dotenv import load_dotenv

load_dotenv()

def send_discord_webhook(jobs_df: pd.DataFrame):
    """Formats and sends job data to Discord via webhook as plain text."""
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print("Error: DISCORD_WEBHOOK_URL environment variable not set.")
        return

    webhook = SyncWebhook.from_url(webhook_url)

    if jobs_df.empty:
        print("No jobs found this hour.")
        return

    # Discord message limit is 2000 characters.
    MAX_CHARS = 2000
    
    job_entries = []
    for _, job in jobs_df.iterrows():
        title = job.get('title', 'N/A')
        company = job.get('company', 'N/A')
        location = job.get('location', 'N/A')
        job_url = job.get('job_url', '#')
        site = job.get('site', 'Unknown Site').title()
        
        entry = f"[{title} @ {company}](<{job_url}>) - 📍 {location} - {site}"
        job_entries.append(entry)

    # Chunk the entries to fit Discord's 2000 character limit
    current_message = []
    current_length = 0
    
    for entry in job_entries:
        # Check if adding this entry + newline exceeds the limit
        # entry length + 1 (for the newline)
        if current_length + len(entry) + 1 > MAX_CHARS:
            # Send the current batch
            if current_message:
                webhook.send("\n".join(current_message))
            current_message = [entry]
            current_length = len(entry)
        else:
            current_message.append(entry)
            current_length += len(entry) + 1 # +1 for newline

    # Send any remaining entries
    if current_message:
        webhook.send("\n".join(current_message))

    print(f"Sent {len(jobs_df)} jobs to Discord.")
