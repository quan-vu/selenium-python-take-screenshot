# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

DOMAIN = '13cwine.com'
LINK = f"https://{DOMAIN}/collections/wines/products/planeta-eruzione-1614-pinot-nero-2017?variant=36987788198048"
SCRENNSHOT_FILENAME = f"screenshot_{DOMAIN}_add_to_cart_button.png"
CSS_SELECTOR = ".product__submit__buttons button"

try:
    # create headless options
    fireFoxOptions = webdriver.FirefoxOptions()
    fireFoxOptions.headless = True
    
    # create webdriver object
    browser = webdriver.Firefox(options=fireFoxOptions, executable_path='./drivers/geckodriver-v0.31.0-linux64')

    # Do something here   
    browser.get(LINK)

    ##================= Step 1: Find HTMl Element 
    element = browser.find_element(By.CSS_SELECTOR, ".product__submit__buttons button")

    ##================= Step 2: Take a screenshot
    element.screenshot(SCRENNSHOT_FILENAME)

    ##================= Step 3: Extract color from image 
    from PIL import Image
    img = Image.open(SCRENNSHOT_FILENAME)
    img.show()

    # Display image
    colors = img.getpixel((10,10))

    #Get the RGB values at coordinate x = 320, y = 240
    print(colors)
finally:
    try:
        browser.close()
    except:
        pass
