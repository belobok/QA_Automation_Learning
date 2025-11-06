# QA Automation Learning (Python + Selenium)

Minimal, educational project that demonstrates:
- Page Object basics (`pages/login_page.py`)
- Explicit waits after login redirect
- pytest structure & fixture
- Safari by default on macOS (no driver mismatch)

**Public demo only**:
- UI: https://practicetestautomation.com
- API: https://jsonplaceholder.typicode.com

## How to run (macOS, Safari)

```bash
# Clone the repository
git clone https://github.com/belobok/QA_Automation_Learning.git
cd QA_Automation_Learning

# Create and activate a virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Enable Safari driver once (macOS)
safaridriver --enable

# Run all tests
pytest -q

# Expected output:
..
2 passed in X.XXs

# Next steps:
# ✅ Negative login test included: tests/test_login_negative.py
# Parametrize valid/invalid credentials
# (Optional) Add Chrome via Selenium Manager

# License:
# MIT — educational/demo use

# 🧩 For Recruiters / Hiring Managers:
# This small open demo shows how I apply QA skills in both manual and automation testing.

# ✅ What this project demonstrates:
# - Real Python + Selenium + pytest setup (Safari/macOS)
# - Page Object pattern with explicit waits and assertions
# - Positive and negative login tests against a public demo site (PracticeTestAutomation)
# - Clear structure: pages/, tests/, conftest.py, requirements.txt
# - Professional .gitignore and MIT license (safe for public sharing)

# How to verify it works:
git clone https://github.com/belobok/QA_Automation_Learning.git
cd QA_Automation_Learning
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
safaridriver --enable
pytest -q

# Expected output:
..
2 passed in X.XXs
```
