cd e:/Test/Interface_Test/test_case
pytest -sq ./ --alluredir=../Report/tmp
allure generate ../Report/tmp -o ../Report/report --clean

