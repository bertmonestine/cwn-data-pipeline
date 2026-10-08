"""
Pipeline outline (simplified public version).

Shows the order of operations only.
Production logic, mappings and configuration values are intentionally omitted.
"""
import argparse


def load_config():
    """Read states, care-setting priority and rules from the config file."""
    ...


def load_source():
    """Read the public SAMHSA facility data."""
    ...


def filter_mental_health(rows):
    """Keep mental health facilities only; drop other types and out-of-scope states."""
    ...


def clean_record(row):
    """Standardize text, phones, ZIP codes and state names; add tags and description."""
    ...


def assign_category(row):
    """One category per facility by care-setting priority."""
    ...


def deduplicate(rows, live_rows):
    """Remove duplicates within the batch and against listings already live."""
    ...


def write_csvs(rows):
    """Write clean CSVs, split into import-sized parts."""
    ...


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--estimate", action="store_true", help="Report expected counts only")
    args = parser.parse_args()

    config = load_config()
    rows = filter_mental_health(load_source())
    rows = [assign_category(clean_record(r)) for r in rows]
    if args.estimate:
        print(len(rows))
        return
    write_csvs(deduplicate(rows, live_rows=[]))


if __name__ == "__main__":
    main()
