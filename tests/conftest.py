import pytest
from selenium import webdriver


def pytest_addoption(parser):
    '''Set the available params and also set default if nothing given'''
    parser.addoption('--browser', default='Chrome', help='A browser which will be launched. Default Chrome')
    parser.addoption('--url', default='http://127.0.0.1/', help='Url to make request to. Default Opencart URL')


@pytest.fixture
def request_params(request):
    '''1st fixture handling the command line params'''
    param = {}
    param['browser'] = request.config.getoption('--browser')
    param['url'] = request.config.getoption('--url')
    return param


@pytest.fixture
def request_browser(request_params, request):
    '''2nd fixture handling the browser choose'''
    if request_params['browser'] == 'IE':
        options = webdriver.IeOptions()
        options.headless = True
        options.add_argument('start-maximized')
        webdr = webdriver.Ie(options=options,
                             executable_path='d:\\PycharmProjects\\HW-lesson_selenium\\drivers\\IEDriverServer.exe')
        request.addfinalizer(webdr.quit)
        return webdr
    elif request_params['browser'] == 'Firefox':
        options = webdriver.FirefoxOptions()
        options.headless = True
        options.add_argument('--start-maximized')
        webdr = webdriver.Firefox(options=options,
                                  executable_path='d:\\PycharmProjects\\HW-lesson_selenium\\drivers\\geckodriver.exe')
        request.addfinalizer(webdr.quit)
        return webdr
    else:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('--start-fullscreen')
        webdr = webdriver.Chrome(options=options,
                                 executable_path='d:\\PycharmProjects\\HW-lesson_selenium\\drivers\\chromedriver.exe')
        return webdr
