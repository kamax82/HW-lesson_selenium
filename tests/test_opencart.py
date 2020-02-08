import pytest


def test_opencart(request_browser, request_params):
    '''Excepts two fixtures comteins requested browser and IP (if chosen) or default Chrome/127.0.0.1 '''
    request_browser.get(request_params['url'])
    assert request_browser.title == 'Your Store'
