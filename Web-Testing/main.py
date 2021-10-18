import pytest
import sys


if __name__ == "__main__":
    sys.exit(pytest.main(["-s", "-n3", "--dist=loadfile", "--html=test_report.html"]))
