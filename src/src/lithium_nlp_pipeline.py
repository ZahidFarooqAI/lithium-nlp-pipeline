df.to_csv("output/lithium_extraction_results.csv", index=False)
with open("output/lithium_extraction_results.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)
