from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import sys
import time
from PIL import Image
from pytesseract import pytesseract
from Features import sndisplay

# Captcha file name
img_name = f"Images\captcha.png"
# Chrome Options
chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
service = Service('D:\\Chromedriver\\chromedriver.exe')


# Class for Bot
class uimsBot:
    # constructor to initialize the instance
    def __init__(self, username, password, url):
        self.username = username
        self.password = password
        self.url = url
        self.login()

    def login(self):
        driver = webdriver.Chrome(service=service, options=chrome_options)
        driver.maximize_window()
        driver.get(self.url)
        count = 0

        try:
            driver.find_element(By.XPATH, '//*[@id="txtUserId"]').send_keys(self.username)
            driver.find_element(By.XPATH, '//*[@id="btnNext"]').click()
            driver.find_element(By.XPATH, '//*[@id="txtLoginPassword"]').send_keys(self.password)
            while True:
                if count >= 1:
                    driver.find_element(By.XPATH, '// *[ @ id = "login-page"] / div / div[2] / button[2]').click()
                    time.sleep(1)
                    driver.find_element(By.XPATH, '//*[@id="lnkupCaptcha"]').click()
                    driver.find_element(By.XPATH, '//*[@id="txtLoginPassword"]').send_keys(self.password)
                    time.sleep(1)
                    driver.find_element(By.XPATH, '// *[ @ id = "txtcaptcha"]').clear()
                # time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="imgCaptcha"]''').screenshot(img_name)
                time.sleep(1)
                captcha = self.charRecognition()
                print(captcha)
                print(f"{len(captcha)}, Datatype:{type(captcha)}")
                # time.sleep(1)
                driver.find_element(By.XPATH, '// *[ @ id = "txtcaptcha"]').send_keys(captcha)
                time.sleep(1)
                driver.find_element(By.XPATH, '//*[@id="btnLogin"]').click()
                time.sleep(2)
                count += 1
                if 'Student' in driver.current_url:
                    sndisplay("Congats, You have successfully logged-in into Chandigarh University Student Portal")
                    sys.exit()

        except Exception as e:
            sndisplay("Sorry!, an error occurred during login")

    def charRecognition(self):
        time.sleep(2)
        # Defining paths to tesseract.exe
        # and the image we would be using
        path_to_tesseract = r"C:\Program Files (x86)\Tesseract-OCR\tesseract.exe"
        image_path = img_name
        # Opening the image & storing it in an image object
        img = Image.open(image_path)
        # Providing the tesseract executable
        # location to pytesseract library
        pytesseract.tesseract_cmd = path_to_tesseract
        # Passing the image object to image_to_string() function
        # This function will extract the text from the image
        text = pytesseract.image_to_string(img)
        if len(text) < 4 or text == "" or text == "":
            return "NULL"
        return text[:4]


file = open("E:\\Learn_Python\Pass_file.txt", "r")
url = "https://uims.cuchd.in/uims/"
data = file.read()
data = data.replace(": ", " ").replace("\n", " ")
data = data.split(" ")
uimsBot(data[1], data[3], url)
