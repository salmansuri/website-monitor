import time
import cv2
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def take_screenshot(url, save_path="screenshot.png"):
    options = Options()
    options.add_argument("--headless")  # Run without UI
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    
    driver.get(url)
    time.sleep(2)  # Wait for page to load
    driver.save_screenshot(save_path)
    driver.quit()
    return save_path

def compare_images(img1_path, img2_path):
    img1 = cv2.imread(img1_path, cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img2_path, cv2.IMREAD_GRAYSCALE)
    
    if img1 is None or img2 is None:
        return 100  # Consider fully changed if missing

    diff = cv2.absdiff(img1, img2)
    non_zero_count = np.count_nonzero(diff)
    return (non_zero_count / diff.size) * 100  # Percentage difference