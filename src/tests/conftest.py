"""
TODO Add module docstring
"""


def pytest_configure(config):
    """Create a log file if log_file is not mentioned in *.ini file"""
    if not config.option.log_file:
        config.option.log_file = "logs/log.churn_library.log"
