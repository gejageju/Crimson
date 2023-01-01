from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

def search_amazon(link):
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)
    productName = driver.find_element_by_id('productTitle').text
    print(productName)
    driver.get(link)
    print([my_elem.get_attribute("src") for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div#altImages>ul li[data-ux-click] img")))])

search_amazon('https://www.amazon.in/Camlin-Kokuyo-Artist-Water-Color/dp/B0752KW82G/?_encoding=UTF8&pd_rd_w=E32aA&content-id=amzn1.sym.1f592895-6b7a-4b03-9d72-1a40ea8fbeca&pf_rd_p=1f592895-6b7a-4b03-9d72-1a40ea8fbeca&pf_rd_r=ZK8AQDAYDDH1JPJX5CFP&pd_rd_wg=JHq7e&pd_rd_r=ddfe1fc2-3025-4561-b0e4-82d59ffa3ece&ref_=pd_gw_ci_mcx_mr_hp_atf_m')
