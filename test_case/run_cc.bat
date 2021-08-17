cd e:/Test/Interface_Test/test_case
pytest -sq ./ --alluredir=../Report
allure serve ../Report -p 9999
