import re
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path


def log_reader(file_path: Path) -> str:
    """Generator to read a file line by line."""
    with open(file_path, "r") as f:
        for line in f:
            yield line.strip()


def clean_log(line: str) -> str | None:
    """Check if the word 'ERROR' is in the line and if so, returns the line, otherwise None."""
    if m := re.search(r"ERROR", line, re.IGNORECASE):
        return line.upper()
    return None


def process_logs(file_path: Path):
    """Process logs in parallel and print cleaned lines."""

    reader = log_reader(file_path)

    with ProcessPoolExecutor() as executor:
        results = executor.map(clean_log, reader)

    # Filter out None results and print the errors
    for entry in results:
        if entry:
            print(f"Found: {entry}")


if __name__ == "__main__":
    process_logs("large_system.log")
