from log_parser import LogAnalyzer

def test_extract_errors():
    logs = ["ERROR: fail", "INFO: ok"]
    analyzer = LogAnalyzer(logs)
    
    errors = analyzer.extract_by_level("ERROR")
    assert len(errors) == 1

def test_extract_infos():
    logs = ["ERROR: fail", "INFO: ok"]
    analyzer = LogAnalyzer(logs)
    
    infos = analyzer.extract_by_level("INFO")
    assert len(infos) == 1
