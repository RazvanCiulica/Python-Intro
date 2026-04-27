name = "Razvan"
years = 8
is_engineer = True

print(name, years, is_engineer)


def greet(name):
    return f"Hello {name}"

print(greet("Razvan"))

def level(years):
    if years >= 3:
        return "mid"
    else:
        return "junior"

print(level(3))            


logs = ["ok", "error", "fail"]

for log in logs:
    print(log)

test_case = {
    "name" : "brake_test", 
    "status" : "fail"
}

print(test_case["name"])
