# Setup
```bash
python3.11 -m venv venv
source venv/bin/activate
pip install -r docs/requirements.txt
```

# To run the tests
```bash
python -m pytest
```

# To run the formatter
```bash
python -m black -l 100 .
```