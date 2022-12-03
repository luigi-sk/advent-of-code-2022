def show(name: str, test_results, expected_test: int, input_results):
    assert test_results == expected_test
    print(f"{name} test: {test_results}")
    print(f"{name} input: {input_results}")
    print("----------------------------------------------------------------")
