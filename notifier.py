import os
import discord
import pandas as pd
from discord import SyncWebhook, Embed
from dotenv import load_dotenv

load_dotenv()

def send_discord_webhook(jobs_df: pd.DataFrame):
    """Formats and sends job data to Discord via webhook."""
    webhook_url = os.getenv("DISCORD_WEBHOOK_URL")
    if not webhook_url:
        print("Error: DISCORD_WEBHOOK_URL environment variable not set.")
        return

    webhook = SyncWebhook.from_url(webhook_url)

    if jobs_df.empty:
        # Silent or simple message for no results
        # webhook.send("No new software engineer internships found this hour.")
        print("No jobs found this hour.")
        return

    # Discord has a limit of 10 embeds per message and 6000 character total.
    # We will send embeds in batches of 10.
    
    embeds = []
    for _, job in jobs_df.iterrows():
        # Clean data for potential empty fields
        title = job.get('title', 'N/A')
        company = job.get('company', 'N/A')
        location = job.get('location', 'N/A')
        job_url = job.get('job_url', '#')
        site = job.get('site', 'Unknown Site')
        
        embed = Embed(
            title=f"{title} @ {company}",
            description=f"📍 {location}\nSource: {site.title()}",
            url=job_url,
            color=discord.Color.blue()
        )
        embeds.append(embed)
        
        # Batch send every 10 embeds
        if len(embeds) == 10:
            webhook.send(embeds=embeds)
            embeds = []
            
    # Final batch
    if embeds:
        webhook.send(embeds=embeds)

    print(f"Sent {len(jobs_df)} jobs to Discord.")
