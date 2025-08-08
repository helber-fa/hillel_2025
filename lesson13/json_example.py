import json
import os
import pathlib
from  utils import validate_test_case


from constants import BASE_PATH

# reports_folder_path = os.path.join(BASE_PATH, "test_results", "test_cases.json").replace("\\\\","\\")
# test_folder_path = str(pathlib.Path(os.path.join(str(BASE_PATH), "test_folder")))
# results_directory = pathlib.Path(BASE_PATH) / "test_results"/"test_cases.json"
# print(reports_folder_path)

with open("test_cases.json", "r") as f:
    test_cases = json.load(f)

report = []

for case in test_cases:
    errors = validate_test_case(case)
    if errors:
        status = "FAIL"
    else:
        status = "PASS"
    report.append(
        {
            "id": case.get("id", "UNKNOWN"),
            "status": status,
            "errors": errors
        }
    )

with open("validated_test_cases.json", "w") as f:
    json.dump(report, f, indent=4)




