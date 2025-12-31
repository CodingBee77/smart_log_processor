import re
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Any, Generator


def log_reader(file_path: Path) -> Generator[str, Any, None]:
    """Generator to read a file line by line."""
    # with open(file_path, "r") as f:
    #     for line in f:
    #         yield line.strip()

    mock_data = [
        "Info: system ok",
        "Error: disk full",
        "Debug: trace",
        "ERROR: auth fail",
    ] * 10000
    for line in mock_data:
        yield line


def clean_log(line: str) -> str | None:
    """Check if the word 'ERROR' is in the line and if so, returns the line, otherwise None."""
    if m := re.search(r"ERROR", line, re.IGNORECASE):
        return line.upper()
    return None


def process_logs(file_path: Path):
    """Process logs in parallel and print cleaned lines."""

    reader = log_reader(file_path)

    with ProcessPoolExecutor() as executor:
        results = executor.map(clean_log, reader, chunksize=500)
        error_count = sum(1 for entry in results if entry)
        print(f"Total Errors found: {error_count}")


if __name__ == "__main__":
    start = time.perf_counter()
    process_logs("large_system.log")
    print(f"Finished in {time.perf_counter() - start:.4f} seconds.")
