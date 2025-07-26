#  Automated LinkedIn Job Application Bot (Python + Selenium)

This project automates the process of applying to **"Easy Apply"** jobs on LinkedIn. It starts from the LinkedIn homepage, logs in, searches for *Python Intern* roles, filters using Easy Apply, and applies where possible.

>  **Note**: The script currently applies to only the first 7 visible jobs. This is likely due to LinkedIn's lazy loading of job cards. Scrolling logic will be added in future improvements.

---

##  Features

-  Logs in securely using `.env` credentials
-  Searches for “Python Intern” roles from the homepage
-  Filters jobs with **Easy Apply**
-  Auto-fills phone number if missing
- ️ Skips complex multi-step applications
-  Applies to simple job listings automatically

---

##  Tech Stack

- **Python 3.10+**
- **Selenium 4+**
- **Chrome WebDriver**
- **dotenv** for secure credential handling

---

