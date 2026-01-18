# LearnCPP to PDF Book

A simple Python script that scrapes webpages from **learncpp.com** and converts them into a single **PDF book** for offline reading, easy access, and distraction-free learning.

This project was created to practice **web scraping** while solving a personal problem: turning valuable online content into a portable, readable format without requiring an internet connection.

---

## 📖 How It Works

- Scrapes the `<article>` content from LearnCPP pages
- Stores the extracted content in a structured list
- Wraps the content in a custom HTML template
- Overrides website CSS to improve readability and formatting
- Converts the final HTML into a PDF using **WeasyPrint**

---

## 🛠 Requirements

- Python **3.9+** (recommended)
- `pip`
- Linux / macOS  
  (Windows users can use **WSL** or **Git Bash**)

---

## 📁 Project Structure

```text
project/
├── script.py
├── requirements.txt
└── README.md

## Setup Instructions

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
### 2. Create a virtual environmnet

```bash
python -m venv .venv
source .venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the script

#### Method 1:

```bash
python script.py
```
#### Method 2:

Make the script executable (only once):

```bash
chmod +x script.py
```

Run it,

```bash
./script.py
```
## Notes:

- The script uses a shebang (#!/usr/bin/env python3) so it can be run directly.
- All dependencies are listed in requirements.txt.
- If something breaks, delete the virtual environment and recreate it.
- Since LearnCPP is a live website, HTML/CSS changes over time may affect scraping or PDF styling.
- If formatting issues appear, check and update the overridden CSS.

## Disclaimer

This project is intended for educational and personal offline use only.
All content belongs to learncpp.com and its respective authors.

## License

This project is open-source and intended for learning and experimentation.

