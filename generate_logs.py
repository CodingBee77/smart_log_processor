# This script generates a mock log file named `large_system.log` with 10,000 lines for testing purposes.

messages = [
    {
        "timestamp": "2025-12-31T14:23:45.123Z",
        "level": "ERROR",
        "service": "payment-api",
        "version": "1.4.2",
        "host": "api-prod-3",
        "pid": 1427,
        "duration_ms": 427,
        "tags": ["payments", "critical"],
    },
    {
        "timestamp": "2024-11-12T14:45:43.123Z",
        "level": "INFO",
        "service": "payment-api",
        "version": "1.4.2",
        "host": "api-prod-3",
        "pid": 1434,
        "duration_ms": 426,
        "tags": ["payments", "critical"],
    },
    {
        "timestamp": "2023-12-02T11:24:45.123Z",
        "level": "DEBUG",
        "service": "payment-api",
        "version": "1.4.2",
        "host": "api-prod-3",
        "pid": 1227,
        "duration_ms": 227,
        "tags": ["payments", "critical"],
    },
    {
        "timestamp": "2025-04-13T14:23:44.123Z",
        "level": "WARNING",
        "service": "payment-api",
        "version": "1.4.2",
        "host": "api-prod-3",
        "pid": 445,
        "duration_ms": 145,
        "tags": ["payments", "critical"],
    },
]

n_lines = 10_000
path = "large_system_extended.log"

with open(path, "w", encoding="utf-8") as f:
    for i in range(n_lines):
        msg = messages[i % len(messages)]
        line = (
            f"{msg['timestamp']} | {msg['level']} | {msg['service']} | v{msg['version']} | "
            f"{msg['host']} | PID:{msg['pid']} | Duration:{msg['duration_ms']}ms | "
            f"Tags:{','.join(msg['tags'])}\n"
        )
        f.write(line)

print(f"Created `{path}` with {n_lines} lines.")
