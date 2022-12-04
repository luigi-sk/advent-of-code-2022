def show(name: str, test_results, expected_test: int, input_results):
    assert test_results == expected_test, f"expected: {expected_test}, give: {test_results}"
    print(f"{name} test: {test_results}")
    print(f"{name} input: {input_results}")
    print("----------------------------------------------------------------")
