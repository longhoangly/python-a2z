#!/bin/sh

# Usage: ./run-tests.sh [TEST_FOLDER] [HEADLESS]
TEST_FOLDER="${1:-tests}"      # default = tests
HEADLESS="${2:-false}"         # default = true (headless)

echo "==> Starting test run"
echo "Test folder: $TEST_FOLDER"
echo "Headless mode: $HEADLESS"

# Ensure reports folder exists
mkdir -p reports/allure-results

# Copy history if available
if [ -d reports/allure-report/history ]; then
    cp -r reports/allure-report/history reports/allure-results/history
fi

# Loop each test file and run in parallel
find $TEST_FOLDER -type f -name 'test*.py' | while read -r test_file; do
  echo executing tests in file "$test_file"
  docker run --rm -v "$PWD":/app my-test-runner "$test_file" true &
done

# Wait for all
# wait
sleep 20

# Generate reports
allure generate reports/allure-results --clean -o reports/allure-report
echo "==> Report ready at reports/allure-report/index.html"

if [ "$HEADLESS" = "false" ]; then
  echo "==> Opening Allure report (headed mode)"
  allure open reports/allure-report
else
  echo "==> Headless mode detected, not opening report"
fi