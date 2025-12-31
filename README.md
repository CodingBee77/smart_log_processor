# Smart Log Processor

Project demonstrates a parallel log processing using the standard library's
`concurrent.futures.ProcessPoolExecutor`.

This repository contains a single example script `main.py` that reads log lines,
filters lines that contain `ERROR` (case-insensitive), and counts them using a
process pool for parallel processing. The included `main.py` currently uses
`mock_data` for fast local testing.

Key features

- Simple, dependency-free Python script (standard library only).
- Example of splitting work across processes with `ProcessPoolExecutor`.
- Streaming-friendly `log_reader` generator (easy to replace with file reads).
- Small, clear `clean_log` function suitable for unit testing and extension.

Requirements

- Python 3.10+ recommended (the code uses modern type syntax like `str | None`).
- No external packages required.

Quick start

1. Run the script:

```bash
python3 main.py
```

You should see output similar to:

```
Total Errors found: 20000
Finished in 0.0XXX seconds.
```

Note: The example uses mock data duplicated to simulate a large file, so the
numbers and runtime are representative only.

Adapting to real logs

- Replace the `mock_data` block inside `log_reader` with a real file iterator:

```python
with open(file_path, "r", encoding="utf-8") as f:
    for line in f:
        yield line.rstrip("\n")
```

- Call `process_logs(Path("/path/to/your/logfile.log"))` or run the script
  with a modified `if __name__ == "__main__":` block to accept CLI args.




