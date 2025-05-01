# Visa Fee Tracker
A simple yet powerful tool that monitors German Embassy visa fees and notifies you when changes occur. Never be caught off guard by unexpected fee changes again!
## Why This Project Exists
Visa fee changes can happen without warning, causing issues for applicants who have already prepared demand drafts or budgeted for their applications. This tool:
- Automatically checks the German Embassy website for fee updates
- Compares current fees with previously recorded values- Sends email notifications when changes are detected
- Provides detailed information about what changed
## Installation
1. Clone the repository:   
```
   git clone https://github.com/yourusername/visa-fee-tracker.git   
   cd visa-fee-tracker
```
2. Install dependencies:   
```
   pip install -r requirements.txt   
```
3. Set up environment variables:
   Create a `.env` file in the project root with:   
```
   EMAIL_ID=your-email@gmail.com   
   EMAIL_PASS=your-app-password
```   
Note: For Gmail, you'll need to use an App Password if you have 2FA enabled.
## Usage
Run the tracker manually:
```
python main.py
```
For automated checking, set up a cron job or scheduled task to run the script at your preferred interval.
Example cron job (daily at 9 AM):
```
0 9 * * * cd /path/to/visa-fee-tracker && python main.py
```

## How It Works
1. The script fetches the current visa fee information from the German Embassy website
2. It compares this data with previously saved information
3. If changes are detected, it generates a detailed email notification
4. The notification is sent to configured email addresses
5. The new data is saved for future comparisons
## Future Development Roadmap
- [ ] **Subscription System**
  - Allow users to subscribe/unsubscribe for notifications  - Web interface for managing email preferences
  - Confirmation emails for subscription changes
- [ ] **Mailgun Integration**  - Move from SMTP to Mailgun for more reliable delivery
  - Better email analytics and tracking  - Improved email templating
- [ ] **Twitter Bot**
  - Automatic tweets when fees change  - Periodic fee information tweets
  - Direct message notifications
- [ ] **Telegram Bot**  - Instant notifications via Telegram
  - Command-based fee inquiries  - Subscription management through chat
  
## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.
## License

This project is licensed under the MIT License - see the LICENSE file for details.











































