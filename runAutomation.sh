#!/bin/bash
#########################################################################################
# This is the script to run automation. The only parameter is: <tag name>
# Examples:
#            # This runs all tests:
#            ./runAutomation.sh
#            # This runs only login tests:
#            ./runAutomation.sh login
#
# Explanation:
# python -m pytest         - Runs Pytest.
# -c componentTest.cfg     - This defines the pytest configuration file.
# --html=./log/report.html - This tells pytest to create an HTML report. This requires
#                            installing pytest-html.
# --self-contained-html    - This tells pytest-html to include the report's CSS code
#                            inside the HTML file and not in a separate CSS file.
# -n 4                     - This tells pytest to run 4 test in parallel. Valid values
#                            are [1, 4] inclusive. This requires installing both
#                            pytest-parallel and pytest-xdist.
#########################################################################################
if [ "$1" != "" ]; then
  python -m pytest -c componentTest.cfg --html=./log/report.html --self-contained-html -n 4 -m $1
else
  python -m pytest -c componentTest.cfg --html=./log/report.html --self-contained-html -n 4
fi
