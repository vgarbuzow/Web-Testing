from selenium.webdriver.common.by import By


#Enter your Yandex.Mail data in the following fields

YANDEX_LOGIN = "LOGIN_HERE"
YANDEX_PASSWORD = "PASSWORD_HERE"


def test_correct_auth(get_chrome_driver):
    driver = get_chrome_driver
    driver.get('https://mail.yandex.ru')
    driver.find_element(By.CLASS_NAME, "HeadBanner-Button-Enter").click()
    assert driver.title == "Авторизация"

    driver.find_element(By.NAME, "login").send_keys(YANDEX_LOGIN)
    driver.find_element(By.ID, "passp:sign-in").click()
    driver.find_element(By.NAME, "passwd").send_keys(YANDEX_PASSWORD)
    driver.find_element(By.ID, "passp:sign-in").click()

    if "passport.yandex.ru/auth/phone" in driver.current_url:
        driver.find_element(By.XPATH, '//div[@data-t="phone_actual_skip"]').click()
    assert driver.find_element(By.CLASS_NAME, 'mail-Page')
