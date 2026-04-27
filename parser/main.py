from log_parser import extract_errors

logs = [
    "INFO : System started",
    "ERROR: Break failure",
    "INFO: Speed  ok",
    "ERROR: Sensor issue"
]

result = extract_errors(logs)
print(result)