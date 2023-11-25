Amazon Price Tracker with Python


This Python application automates price tracking for a specific Amazon product and sends email alerts when the price drops below a predefined threshold. Leveraging BeautifulSoup for web scraping, it extracts the product price from the Amazon webpage.

Features:
Web Scraping: Utilizes BeautifulSoup along with the requests library to fetch and parse the Amazon product page.
Price Comparison: Retrieves the current price of the specified product and compares it against a set threshold (e.g., ₹25,000).
Email Notifications: Sends an email alert via Gmail's SMTP server if the current price falls below the predefined threshold.
How to Use:
Setup: Install the necessary Python libraries (bs4, requests, smtplib).
Configuration: Update web_url with the URL of the Amazon product to track.
Credentials: Input your Gmail credentials (my_email and password) for sending emails.
Threshold: Adjust the price variable to set your desired price threshold.
Scheduling: Use platforms like PythonAnywhere to schedule the script to run daily at 9 am.
Usage Example:
python
Copy code
python amazon_price_tracker.py
Important Notes:
Compliance: Ensure adherence to website terms of service and considerate use of web scraping methods.
Security: Safeguard your email credentials and consider using environment variables for sensitive data.
This script provides a simple yet effective means to monitor Amazon product prices. Users can modify thresholds and scheduling settings to suit their preferences. However, it's essential to use this tool responsibly and ethically in accordance with Amazon's policies and best practices for web scraping.

For any issues or contributions, feel free to fork this repository and make improvements. Suggestions and enhancements are always welcome.
