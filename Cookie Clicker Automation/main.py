from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, "cookie")


def buy():
    m1 = driver.find_element(By.ID, "money")
    money = int("".join(m1.text.split(",")))

    c1 = driver.find_element(By.CSS_SELECTOR, "#buyCursor b")
    p1 = driver.find_element(By.CSS_SELECTOR, "#buyPortal b")
    a1 = driver.find_element(By.XPATH, '//*[@id="buyAlchemy lab"]/b')
    s1 = driver.find_element(By.CSS_SELECTOR, "#buyShipment b")
    m1 = driver.find_element(By.CSS_SELECTOR, "#buyMine b")
    f1 = driver.find_element(By.CSS_SELECTOR, "#buyFactory b")
    g1 = driver.find_element(By.CSS_SELECTOR, "#buyGrandma b")
    t1 = driver.find_element(By.XPATH, '//*[@id="buyTime machine"]/b')

    cm = int("".join(c1.text.split()[-1].split(",")))
    pm = int("".join(p1.text.split()[-1].split(",")))
    am = int("".join(a1.text.split()[-1].split(",")))
    sm = int("".join(s1.text.split()[-1].split(",")))
    mm = int("".join(m1.text.split()[-1].split(",")))
    fm = int("".join(f1.text.split()[-1].split(",")))
    gm = int("".join(g1.text.split()[-1].split(",")))
    tm = int("".join(t1.text.split()[-1].split(",")))

    if money >= tm:
        time_machine.click()
    elif money >= pm:
        portal.click()
    elif money >= am:
        alchemy.click()
    elif money >= sm:
        shipment.click()
    elif money >= mm:
        mine.click()
    elif money >= fm:
        factory.click()
    elif money >= gm:
        grandma.click()
    elif money >= cm:
        cursor.click()


clicks = 0
while True:
    cookie.click()
    clicks += 1
    if clicks >= 300:
        portal = driver.find_element(By.ID, "buyPortal")
        alchemy = driver.find_element(By.ID, "buyAlchemy lab")
        shipment = driver.find_element(By.ID, "buyShipment")
        mine = driver.find_element(By.ID, "buyMine")
        factory = driver.find_element(By.ID, "buyFactory")
        grandma = driver.find_element(By.ID, "buyGrandma")
        cursor = driver.find_element(By.ID, "buyCursor")
        time_machine = driver.find_element(By.ID, "buyTime machine")
        clicks = 0
        buy()
