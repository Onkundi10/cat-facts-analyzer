"""
catfacts_analyzer.py
---------------------

This script loads a small dataset of cat facts (stored in ``data/cat_facts.json``),
computes basic statistics, and generates a simple histogram of fact lengths.

Features:

* Load facts from the bundled JSON file.
* Display the first few facts with their lengths.
* Compute and print descriptive statistics such as the average, minimum and maximum
  lengths of the facts.
* Plot a histogram of fact lengths and save it as ``output/cat_fact_length_hist.png``.

Usage:

```
python catfacts_analyzer.py
```

The script does not require any command line arguments. It will output the
statistics to the console and save a PNG image into the ``output`` directory.

The cat facts used in this project come from the public API at
``catfact.ninja``【28387644473468†L0-L17】【186839503980557†L0-L29】. For offline use the facts are cached in
``data/cat_facts.json``.
"""

import json
import os
from statistics import mean
import matplotlib.pyplot as plt


def load_facts(json_path: str) -> list:
    """Load cat facts from a JSON file.

    Args:
        json_path: Path to the JSON file containing the facts.

    Returns:
        A list of dictionaries with keys ``fact`` and ``length``.
    """
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    return data.get("facts", [])


def compute_statistics(facts: list) -> dict:
    """Compute simple statistics about fact lengths.

    Args:
        facts: List of fact dictionaries.

    Returns:
        A dictionary with the minimum, maximum and average length of the facts.
    """
    lengths = [fact["length"] for fact in facts]
    return {
        "count": len(lengths),
        "min_length": min(lengths),
        "max_length": max(lengths),
        "avg_length": mean(lengths),
    }


def plot_length_histogram(facts: list, output_path: str) -> None:
    """Create and save a histogram of fact lengths.

    Args:
        facts: List of fact dictionaries.
        output_path: File path where the histogram image will be saved.
    """
    lengths = [fact["length"] for fact in facts]
    plt.figure()
    plt.hist(lengths, bins=10)  # Default colors. Do not specify colors per guidelines
    plt.title("Distribution of Cat Fact Lengths")
    plt.xlabel("Fact Length (characters)")
    plt.ylabel("Frequency")
    plt.tight_layout()
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.savefig(output_path)
    plt.close()


def main() -> None:
    # Define paths relative to this script's location
    current_dir = os.path.dirname(os.path.abspath(__file__))
    data_path = os.path.join(current_dir, "data", "cat_facts.json")
    output_dir = os.path.join(current_dir, "output")
    image_path = os.path.join(output_dir, "cat_fact_length_hist.png")

    # Load data
    facts = load_facts(data_path)
    if not facts:
        print("No facts were loaded. Please check the data file.")
        return

    # Print the first few facts to the console
    print("Cat Facts:\n-----------")
    for idx, fact in enumerate(facts[:5], start=1):
        print(f"{idx}. {fact['fact']} (Length: {fact['length']})")

    # Compute statistics
    stats = compute_statistics(facts)
    print("\nStatistics:")
    print(f"Total facts: {stats['count']}")
    print(f"Shortest fact length: {stats['min_length']}")
    print(f"Longest fact length: {stats['max_length']}")
    print(f"Average fact length: {stats['avg_length']:.2f}")

    # Plot histogram
    plot_length_histogram(facts, image_path)
    print(f"\nHistogram saved to {image_path}")


if __name__ == "__main__":
    main()
