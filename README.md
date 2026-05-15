
# Social Media Profile Exposure Analyzer (SocioTrace)

## Overview

SocioTrace is a cybersecurity-focused tool that analyzes publicly available social media profiles to detect privacy exposure and potential risks. It uses Open Source Intelligence (OSINT) techniques and basic Natural Language Processing (NLP) to evaluate how much personal information is exposed online.

The system helps users understand their digital footprint and provides actionable insights to improve online privacy and security.

---

## Features

* Analyze public profiles from multiple platforms
* Cross-platform profile detection (username matching)
* Detect sensitive information (email, phone, location, etc.)
* Privacy Risk Score generation
* Attacker-perspective risk analysis
* Personalized privacy recommendations

---

## Tech Stack

* Backend: Python
* Framework: Flask
* Database: MongoDB
* NLP: Basic text processing
* OSINT Tools: Sherlock, Instaloader, snscrape
* Visualization: Matplotlib

---

## How It Works

1. User inputs a public social media profile URL
2. System detects the platform (GitHub, Instagram, LinkedIn, etc.)
3. Public data is extracted using OSINT tools
4. NLP and rule-based analysis detect exposed information
5. Exposure is classified into categories
6. A Privacy Risk Score is generated
7. Results, graphs, and recommendations are displayed

---

## How to Run

### 1. Clone the repository

```bash
git clone https://github.com/your-repo/sociotrace.git
cd sociotrace
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Run the application

```bash
python main.py
```

### 4. Use the system

* Enter a public profile URL
* View exposure analysis and risk report

---

## Example Input

```
https://github.com/torvalds
https://www.instagram.com/cristiano/
```

---

## Output Includes

* Extracted public profile data
* Exposure detection (email, phone, etc.)
* Risk score (Low / Medium / High)
* Graphical representation
* Privacy recommendations

---

## Ethical Considerations

* Only publicly available data is used
* No login credentials or private data access
* No long-term storage of sensitive information
* Designed for awareness, not misuse

---

## Future Improvements

* Support more platforms (Facebook, Reddit, YouTube)
* Machine learning-based risk scoring
* Real-time monitoring and alerts
* User dashboard for tracking exposure
* Browser extension integration

