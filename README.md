# FundedNext Dashboard Automation

This project automates testing for the FundedNext dashboard using Selenium.

## Setup

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Create a `.env` file in the root directory with the following variables:
   ```env
   TESTUSERNAME=your_username
   PASSWORD=your_password
   URL=https://uat-dashboard.fundednext.com/login
   DASHBOARD=https://uat-dashboard.fundednext.com/dashboard
   ```

## Usage

Run all tests:
```bash
python main.py
```

Run a specific test (e.g., `login`):
```bash
python main.py --test login
```

## Features
- Uses environment variables for credentials and URLs
- Explicit waits for elements
- Error handling and logging
- Screenshot capture on errors
- Modular test structure

## Notes
- Chrome browser and ChromeDriver must be installed and available in your PATH.
- Screenshots are saved in the current directory when errors occur. 