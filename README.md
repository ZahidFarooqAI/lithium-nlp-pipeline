# Lithium NLP Pipeline

This project extracts **lithium-related information** from unstructured text (news articles, press releases, reports) using spaCy, regex, and rule-based NLP.  

It is designed for **battery industry monitoring, supply chain risk analysis, and commodity intelligence**.

---

## Features
- Extracts:
  - Lithium mentions (`lithium carbonate`, `spodumene`, `brine lithium`, etc.)
  - Companies (ORG), money values (MONEY), dates, locations
  - Quantities (`tons`, `GWh`, `cells`, etc.)
- Flags shortage/production signals (`supply crunch`, `ramp up`, etc.)
- Outputs results to **CSV and JSON** for downstream analytics
- Easily extensible to **other metals** (nickel, cobalt, manganese)

---

##  Installation
```bash
# Clone repo
git clone https://github.com/yourusername/lithium-nlp-pipeline.git
cd lithium-nlp-pipeline

# Create virtual environment
python -m venv .venv
source .venv/bin/activate   # (Linux/macOS)
.venv\Scripts\activate      # (Windows)

# Install dependencies
pip install -r requirements.txt

# Download spaCy model
python -m spacy download en_core_web_sm
