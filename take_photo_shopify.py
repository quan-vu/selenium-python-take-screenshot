# import webdriver
from selenium import webdriver
from selenium.webdriver.common.by import By

DOMAIN = '13cwine.com'
LINK = f"https://{DOMAIN}/collections/wines/products/planeta-eruzione-1614-pinot-nero-2017?variant=36987788198048"
SCRENNSHOT_FILENAME = f"screenshot_{DOMAIN}_add_to_cart_button.png"
CSS_SELECTOR = ".product__submit__buttons button"

##================= Step 1: Take a screen short

# create webdriver object
driver = webdriver.Firefox()

# get url
driver.get(LINK)

# get element
element = driver.find_element(By.CSS_SELECTOR, CSS_SELECTOR)

# Take a screenshot
element.screenshot(SCRENNSHOT_FILENAME)


##================= Step 2: Extract color from image 
from PIL import Image

img = Image.open(SCRENNSHOT_FILENAME)
img.show()

# Display image
colors = img.getpixel((10,10))

#Get the RGB values at coordinate x = 320, y = 240
print(colors)