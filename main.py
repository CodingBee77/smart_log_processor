import re
from concurrent.futures import ProcessPoolExecutor


def log_reader(file_path):
    """Generator to read a file line by line."""
    with open(file_path, "r") as f:
        for line in f:
            yield line.strip()


def clean_log(line):
    """Check if the word 'ERROR' is in the line and if so, returns the line, otherwise None."""
    if m := re.search(r"ERROR", line, re.IGNORECASE):
        return line.upper()
    return None


if __name__ == "__main__":
    process_logs("large_system.log")
    pass
