from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


def test_login_success():
    # 1. Khởi tạo trình duyệt
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    # 2. Mở trang login
    driver.get("https://the-internet.herokuapp.com/login")

    # 3. Tìm phần tử và thao tác
    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # 4. Kiểm tra kết quả
    message = driver.find_element(By.ID, "flash").text
    assert "You logged into a secure area!" in message

    # 5. Đóng trình duyệt
    driver.quit()


def test_login_wrong_password():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("tomsmith")
    driver.find_element(By.ID, "password").send_keys("sai_mat_khau")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    message = driver.find_element(By.ID, "flash").text
    assert "Your password is invalid!" in message

    driver.quit()


def test_login_wrong_username():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://the-internet.herokuapp.com/login")

    driver.find_element(By.ID, "username").send_keys("sai_ten")
    driver.find_element(By.ID, "password").send_keys("SuperSecretPassword!")
    driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    message = driver.find_element(By.ID, "flash").text
    assert "Your username is invalid!" in message

    driver.quit()