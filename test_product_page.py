import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage

import time

@pytest.mark.parametrize('num', [*range(1,7), pytest.param(7, marks=pytest.mark.xfail(reason='bugged')), *range(8,10)])
def test_guest_can_add_product_to_basket(browser,num):
    link = f'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{num}'
    page = ProductPage(browser,link)
    page.open()
    page.should_not_be_success_message()
    page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_product_into_basket()
    page.should_be_message_basket_total()