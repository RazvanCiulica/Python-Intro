from log_parser import LogAnalyzer

logs = [
    "INFO : System started",
    "ERROR: Break failure",
    "INFO: Speed  ok",
    "ERROR: Sensor issue"
]

analyzer = LogAnalyzer(logs)
print(analyzer.summary())
