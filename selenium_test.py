from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_selenium_script():
    print("準備設定WebDriver...")
    # 指定Chrome的二進制位置
    chrome_binary_path = r"C:\Users\User\Desktop\chrome-win64\chrome-win64\chrome.exe"
    # 指定ChromeDriver的路徑
    chromedriver_path = r"D:\chromedriverBETA.exe"

    chrome_options = Options()
    chrome_options.binary_location = chrome_binary_path

    # 初始化WebDriver服務
    webdriver_service = Service(executable_path=chromedriver_path)

    print("啟動WebDriver...")
    try:
        driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)
        print("WebDriver啟動成功，訪問Google...")
        driver.get("http://www.google.com")
        print("訪問成功！請檢查瀏覽器窗口。")
       
       # 点击“登录”按钮
        login_button = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'ServiceLogin')]"))
        )
        login_button.click()

        email_input = WebDriverWait(driver, 20).until(
            EC.visibility_of_element_located((By.ID, "identifierId"))
        )

        # 输入邮箱地址
        email_input.send_keys("")
        email_input.send_keys(Keys.ENTER)

    except Exception as e:
        print(f"在運行Selenium時發生錯誤: {e}")
    finally:
        # 使用input暫停，以便你可以看到打開的瀏覽器，然後手動關閉或等待腳本結束
        input("按Enter鍵退出並關閉瀏覽器...")
        driver.quit()
        print("WebDriver已關閉。")

if __name__ == "__main__":
    run_selenium_script()
