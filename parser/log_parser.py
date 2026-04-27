def extract_errors(logs):
    errors = []

    for log in logs:
        if "ERROR" in log:
            errors.append(log)

    return {
        "total_error" : len(errors),
        "errors" : errors
    }