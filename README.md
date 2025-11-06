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
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
safaridriver --enable   # run once
pytest -q



```

## Next steps
- Add negative login test
- Parametrize valid/invalid
- (Optional) Chrome via Selenium Manager

## License
MIT — educational/demo use
