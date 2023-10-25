from selene import browser, have, be
#browser.config.browser_name = 'firefox'
#browser.config.hold_browser_open = True

def test_can_login():
    browser.element('.login-form [name=password]').type('qagurupassword').press_enter()
    browser.open('https://qa.guru/cms/system/login')
    browser.element('.login-form [name=email]').type('qagurubot@gmail.com').press_enter()

    browser.element('main-header_login').click()
    browser.element('.logined-form').should(have.text('QA_GURU_BOT'))
