# This script generates a mock log file named `large_system.log` with 10,000 lines for testing purposes.

messages = [
    "Info: system ok",
    "Error: disk full",
    "Debug: trace",
    "ERROR: auth fail",
]

n_lines = 10_000
path = "large_system.log"

with open(path, "w", encoding="utf-8") as f:
    for i in range(n_lines):
        f.write(messages[i % len(messages)] + "\n")

print(f"Created `{path}` with {n_lines} lines.")

# {"timestamp":"2025-12-31T14:23:45.123Z","level":"ERROR","service":"payment-api","version":"1.4.2","host":"api-prod-3","pid":1427,"thread":"Thread-9","trace_id":"4f8b2a1e9c3d4f5a","span_id":"a1b2c3d4","msg":"Failed to charge card","error":{"type":"StripeError","message":"card_declined","code":"card_declined"},"request":{"method":"POST","path":"/v1/charges","id":"req_9a8b7c"},"user":{"id":"user_1234","email":"redacted@example.com"},"duration_ms":427,"tags":["payments","critical"]}
