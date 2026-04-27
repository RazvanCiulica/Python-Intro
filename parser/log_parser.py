class LogAnalyzer:
    def __init__(self, logs):
        self.logs = logs

    def extract_by_level(self, level):
        result = []

        for log in self.logs:
            if level in log:
                result.append(log)

        return result
    
    def summary(self):
        return {
            "errors": len(self.extract_by_level("ERROR")),
            "info": len(self.extract_by_level("INFO"))
        }