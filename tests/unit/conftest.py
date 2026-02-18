import pytest
def pytest_runtest_makereport(item, call):
    if call.when == 'call':  # After the test runs (not before)
        if call.excinfo is None:
            print(f"{item.nodeid} - Duration: {call.duration:.2f}s - PASSED")
        else:
            print(f"{item.nodeid} - Duration: {call.duration:.2f}s - FAILED: {call.excinfo}")