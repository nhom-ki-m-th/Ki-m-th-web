from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_smoke():
    # 1. Khởi tạo Chrome
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # 2. Mở trang
    driver.get("https://the-internet.herokuapp.com")

    # 3. Kiểm tra tiêu đề
    assert driver.title == "The Internet"

    # 4. Đóng trình duyệt
    driver.quit()