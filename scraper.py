import pandas as pd
from jobspy import scrape_jobs

def fetch_jobs():
    """Fetches software engineer internships from USA and Canada posted within the last hour."""
    search_params = {
        "search_term": "software engineer intern",
        "job_type": "internship",
        "hours_old": 1,
        "results_wanted": 25,
        "site_name": ["indeed", "linkedin", "zip_recruiter", "google"],
    }

    # Fetching for USA
    jobs_usa = scrape_jobs(
        **search_params,
        location="United States",
        country_indeed='USA'
    )

    # Fetching for Canada
    jobs_canada = scrape_jobs(
        **search_params,
        location="Canada",
        country_indeed='Canada'
    )

    # Combine results
    if not isinstance(jobs_usa, pd.DataFrame):
        jobs_usa = pd.DataFrame()
    if not isinstance(jobs_canada, pd.DataFrame):
        jobs_canada = pd.DataFrame()

    all_jobs = pd.concat([jobs_usa, jobs_canada], ignore_index=True)
    
    # Remove duplicates based on job_url if any
    if not all_jobs.empty:
        all_jobs = all_jobs.drop_duplicates(subset=['job_url'])
        
    return all_jobs
