import json
import pandas as pd

def save_results_csv_json(results, base_path="output/lithium_extraction_results"):
    """Save NLP results to both CSV and JSON."""
    from .lithium_nlp_pipeline import results_to_dataframe
    df = results_to_dataframe(results)
    df.to_csv(f"{base_path}.csv", index=False)
    with open(f"{base_path}.json", "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    print(f"Saved results to {base_path}.csv and {base_path}.json")
    return df
