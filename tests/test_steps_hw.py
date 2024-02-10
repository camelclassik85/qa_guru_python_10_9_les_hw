import allure
from allure_commons.types import Severity
from selene import browser, be, by
from helpers.actions import open_issue_tab, open_main_page, go_to_repository, search_repository, \
    should_see_issue_with_number


@allure.tag('GitHub')
@allure.severity(Severity.MINOR)
@allure.label('Owner', 'AD')
@allure.feature("Issue in repository dynamic_steps_version")
@allure.story('Find Issue for HW qa.guru')
@allure.link('https://github.com', name='Testing')
def test_dynamic_steps():
    browser.config.window_width = 1080
    browser.config.window_height = 720
    with allure.step('Open main link'):
        browser.open('https://github.com')
    with allure.step('Find repository'):
        browser.element('[data-target="qbsearch-input.inputButton"]').click()
        browser.element("#query-builder-test").type("eroshenkoam/allure-example")
        browser.element("#query-builder-test").press_enter()
    with allure.step('Go to repo'):
        browser.element(by.link_text("eroshenkoam/allure-example")).click()
    with allure.step('Open tab issues'):
        browser.element("#issues-tab").click()
    with allure.step('Checking issue visability with name "Issue for HW qa.guru"'):
        browser.element(by.text("Issue for HW qa.guru")).should(be.visible)


@allure.tag('GitHub')
@allure.severity(Severity.MINOR)
@allure.label('Owner', 'AD')
@allure.feature("Issue in repository steps_version")
@allure.story('Find Issue for HW qa.guru')
@allure.link('https://github.com', name='Testing')
def test_decorator_steps():
    open_main_page()
    search_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue_tab()
    should_see_issue_with_number('Issue for HW qa.guru')
