from selene import browser, by, be


def test_github():
    browser.open('/')

    browser.element('[data-target="qbsearch-input.inputButton"]').click()
    browser.element("#query-builder-test").type("eroshenkoam/allure-example")
    browser.element("#query-builder-test").press_enter()

    browser.element(by.link_text("eroshenkoam/allure-example")).click()

    browser.element("#issues-tab").click()

    browser.element(by.text("Issue for HW qa.guru")).should(be.visible)
