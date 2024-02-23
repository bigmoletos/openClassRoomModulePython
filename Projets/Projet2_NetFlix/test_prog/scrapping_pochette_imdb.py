from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

def get_movie_poster_with_selenium(tconst):
    options = Options()
    options.headless = True  # Run in headless mode, without a UI.
    driver= webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        url = f"https://www.imdb.com/title/{tconst}/mediaviewer/"
        driver.get(url)
        # Wait for the page to load, you can use WebDriverWait here to wait for a specific element to ensure the page has loaded
        driver.implicitly_wait(10) # This is not the best practice, it's better to use WebDriverWait
        # Find the image with 'mediaviewer' in the src attribute
        poster_imgs = driver.find_elements(By.CSS_SELECTOR, "img[src*='mediaviewer']")
        # Filter out any that start with the Amazon URL
        poster_img = next((img for img in poster_imgs if not img.get_attribute('src').startswith('https://m.media-amazon.com')), None)
        if poster_img:
            return poster_img.get_attribute('src')
    except Exception as e:
        print(f"Erreur lors du scrapping de l'image avec Selenium: {e}")
    finally:
        driver.quit()  # Make sure to quit the driver to free up resources

    return None  # Return None if no proper poster is found or an error occurred


print(get_movie_poster_with_selenium('tt0084555'))