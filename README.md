# writing_tests_help
Objective: This repo solely exists to show how to write tests for CI. just for practice.
DateCreated: 190113

## How to run tests

### FIRST-TIME RUN IN PYCHARM:
1. Edit Configurations...
2. Add new configuration >> Python Tests >> Unittests
    a. single item: Target = "Module name", path = tests.test_modulelib.TestModulelib2
    b. single file: Target = "Module name", path = tests.test_modulelib
    c. single folder: Target = "Module name", path = tests
3. if you have a test file that doesn't start with "test_", then you will need to add pattern that 
    will correctly find all tests, such as "-p *.py" (ensure all tests in one folder) 
4. click "OK"

### RUN FROM COMMAND LINE:
1. go to top-level folder
2. `python -m unittest discover -s tests -p *.py` (run all tests in folder)
