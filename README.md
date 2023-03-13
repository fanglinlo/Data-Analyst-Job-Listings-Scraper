# Data Analyst Job Listings Scraper

This script scrapes job listings from the 104 job search website for the keyword "Data analyst" in Taiwan. The script retrieves the date, company name, job title, and job link for each job listing and saves the data to both a CSV file and a MySQL database.

## Libraries Used

- pandas
- sqlalchemy
- requests
- BeautifulSoup
- re
- datetime

## How to Use

1. Clone the repository to your local machine.
2. Install the required libraries using pip or conda.
3. Modify the script as needed, such as changing the search keyword, location, and database connection information.
4. Run the script in your terminal or IDE.
5. Check the CSV file and MySQL database for the scraped data.

## Notes

- The script currently only scrapes the first 10 pages of job listings. Modify the `range` function in the for loop to scrape more pages.
- The MySQL connection information needs to be modified to match your own database connection information.
