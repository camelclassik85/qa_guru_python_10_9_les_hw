from selene import browser, be, by
import allure


@allure.step('Open main link')
def open_main_page():
    browser.open('/')


@allure.step('Find repository {repo}')
def search_repository(repo):
    browser.element('[data-target="qbsearch-input.inputButton"]').click()
    browser.element("#query-builder-test").type(repo)
    browser.element("#query-builder-test").press_enter()


@allure.step('Go to repo {repo}')
def go_to_repository(repo):
    browser.element(by.link_text(repo)).click()


@allure.step('Open tab issues')
def open_issue_tab():
    browser.element("#issues-tab").click()


@allure.step('Checking issue {name}')
def should_see_issue_with_number(name):
    browser.element(by.text(name)).should(be.visible)
