import pytest
from apilist.login import login
from common.hashlibSHA1 import get_str_sha1
from conf.meiziku import username,password


@pytest.fixture(scope='session')
def login_start():
    password_shal = get_str_sha1(password)
    token = login(username=username, password=password_shal)['token']
    return token



