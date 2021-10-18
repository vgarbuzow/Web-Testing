from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


def test_google_search(get_chrome_driver):
    driver = get_chrome_driver
    driver.get('https://google.com')
    driver.find_element(By.NAME, 'q').send_keys('купить кофемашину bork c804', Keys.ENTER)
    stats = driver.find_element(By.ID, 'result-stats')
    assert get_number_results(stats.text) > 10, 'Результатов выдачи меньше 10'

    is_found = False
    for tag in driver.find_elements(By.TAG_NAME, 'cite'):
        if 'mvideo.ru' in tag.text:
            is_found = True
            break
    assert is_found, 'В выдаче не присутствует MVideo'


def get_number_results(result_stats_text):
    number_result = ''
    for word in result_stats_text.split():
        if word.isdigit():
            number_result += word
    return int(number_result)
