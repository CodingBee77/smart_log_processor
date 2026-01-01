import re
import time
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path
from typing import Any, Generator


def log_reader(file_path: Path) -> Generator[str, Any, None]:
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
        results = executor.map(clean_log, reader, chunksize=500)
        error_count = sum(1 for entry in results if entry)
        print(f"Total Errors found: {error_count}")


if __name__ == "__main__":
    start = time.perf_counter()
    process_logs(Path("./large_system_extended.log"))
    print(f"Finished in {time.perf_counter() - start:.4f} seconds.")


# TODO 1: Add CLI argument parsing (argparse) to accept input file path, number of workers, and chunksize.
# TODO 2: Make `process_logs` return the count instead of printing it for better composability and easier testing.
# TODO 3: Add structured output (JSON/CSV) and streaming writes for downstream tools.
# TODO 4: Add logging, metrics, and error handling for robustness in production.
