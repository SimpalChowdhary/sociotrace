# SocioTrace – Social Media Profile Exposure Analyzer

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Flask](https://img.shields.io/badge/Flask-Backend-black)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-green)
![OSINT](https://img.shields.io/badge/OSINT-Enabled-orange)
![Status](https://img.shields.io/badge/Project-Active-success)

A non-invasive, OSINT-based application that analyzes publicly available social media data to detect privacy exposure and assess cybersecurity risks using rule-based analysis and lightweight NLP techniques.

---

## Overview

This system is designed to help users understand their digital footprint by analyzing publicly accessible social media profiles. It uses Open Source Intelligence (OSINT) techniques to collect data from platforms like GitHub, Instagram, LinkedIn, and Twitter/X.

The application processes this data using rule-based logic and Natural Language Processing (NLP) to detect sensitive information such as personal details, location, and behavioral patterns. It then generates a Privacy Risk Score and provides attacker-perspective insights along with actionable recommendations.

---

## Features

* Real-time public profile analysis
* Cross-platform username detection
* Exposure detection (email, phone, location, etc.)
* Rule-based and NLP-based analysis
* Privacy Risk Score generation
* Attacker-perspective insights
* Visualization and reporting

---

## Tech Stack

| Layer           | Tools & Technologies            |
| --------------- | ------------------------------- |
| Backend         | Python                          |
| Framework       | Flask                           |
| Database        | MongoDB                         |
| NLP             | Basic text processing           |
| OSINT Tools     | Sherlock, Instaloader, snscrape |
| Data Processing | Pandas, NumPy                   |
| Visualization   | Matplotlib                      |
| Communication   | HTTP APIs, JSON                 |

---

## System Flow

<img width="1201" height="1325" alt="image" src="https://github.com/user-attachments/assets/28bdb9cb-7bcd-4e98-baf3-9c26f6175077" />


---

## Screenshots


<img width="2512" height="1414" alt="image" src="https://github.com/user-attachments/assets/a4e824aa-3531-49e0-a701-c91b342b260f" />
<img width="2900" height="1631" alt="image" src="https://github.com/user-attachments/assets/06336a1e-674e-40fc-8ad7-a32beb6a2570" />
<img width="2938" height="1653" alt="image" src="https://github.com/user-attachments/assets/015bdc29-ad22-40aa-bd78-350004f04040" />
<img width="2912" height="1639" alt="image" src="https://github.com/user-attachments/assets/d6d20bc3-4b82-4c8f-9865-1359d114408d" />
<img width="2888" height="1625" alt="image" src="https://github.com/user-attachments/assets/2e53fc1b-fdfe-4a66-9fdc-3ecca3df6fcc" />
<img width="3013" height="1694" alt="image" src="https://github.com/user-attachments/assets/fe47997f-1dd8-44e7-9ede-9246d92c2867" />



---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-repo/sociotrace.git
cd sociotrace
```

---

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 3. Run the Application

```bash
python main.py
```

---

### 4. Use the System

* Enter a public profile URL
* View exposure analysis and risk report

---

## Outputs

* Extracted public profile data
* Exposure detection results
* Privacy Risk Score (Low / Medium / High)
* Graphical visualizations
* Privacy recommendations

---

## Example Inputs

```
https://github.com/torvalds
https://www.instagram.com/cristiano/
https://www.linkedin.com/in/satyanadella/
```

---

## Future Scope

* Support additional platforms (Facebook, Reddit, YouTube)
* Machine learning-based risk scoring
* Real-time monitoring and alerts
* User dashboard for tracking exposure
* Browser extension integration
* Multi-language NLP support

---

## Author

Simpal Chowdhary – [GitHub Profile](https://github.com/SimpalChowdhary)

---

## About

An end-to-end OSINT and NLP-based system for analyzing social media privacy exposure. It integrates automated data collection, exposure detection, risk scoring, and visualization to help users understand and manage their digital presence.

