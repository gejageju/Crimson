from django.shortcuts import render
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from .models import Products,Entry,Rewards
from django.shortcuts import redirect
from bs4 import BeautifulSoup
import requests
import time
# Create your views here.
def index(request):
    wishlist=Products.objects.filter(claimed=False)
    r=Rewards.objects.get(id=1)
    amount=r.coins
    wishlist_data=[]
    for i in wishlist:
        
        hide=False
        togo=0
        if amount>=i.price:
            hide=True
        else:
            togo=i.price-amount
        wishlist_data.append({
            'id' : i.id,
            'title' : i.title,
            'url' : i.url,
            'hide' : hide,
            'togo' : togo
        })
        print(i.title)
        print(hide)
        print(togo)


    entries=Entry.objects.all()
    
    claimed=Products.objects.filter(claimed=True)
    return render(request,'index.html',{'wishlist': wishlist_data,'entries':entries,'amount':amount,'claimed':claimed})

def addentry(request):
    item=request.POST.get('item')
    amount=request.POST.get('amount')
    entry=Entry(name=item,amount=amount)
    entry.save()
    reward=Rewards.objects.get(id=1)
    amt=int(amount)+reward.coins 
    Rewards.objects.filter(id=1).update(coins=amt)
    
    return redirect(index)

def getproduct(request):
    link=request.POST.get('addtolist')
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(link)
    productName = driver.find_element_by_id('productTitle').text
    print(productName)
    driver.get(link)
    data=[my_elem.get_attribute("src") for my_elem in WebDriverWait(driver, 20).until(EC.visibility_of_all_elements_located((By.CSS_SELECTOR, "div#altImages>ul li[data-ux-click] img")))]
    print(data[0]) 
    HEADERS = ({'User-Agent':
                'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko)Chrome/44.0.2403.157 Safari/537.36',
                                'Accept-Language': 'en-US, en;q=0.5'})
    
    # Making the HTTP Request
    webpage = requests.get(link, headers=HEADERS)
    # Creating the Soup Object containing all data
    soup = BeautifulSoup(webpage.content, "lxml")
    try:
        price = soup.find(
            "span", attrs={'class': 'a-price-whole'})
    
    except AttributeError:
        price = 0
    amt=int(float(price.text))
    print(type(amt))
    product=Products(title=productName,url=data[0],price=amt)
    product.save()
    
    return redirect(index)

def claim(request):

    key=request.POST.get('prod')
    
    print(key)
    time.sleep(5)
    Products.objects.filter(id=key).update(claimed=True)
    cost=Products.objects.get(id=key).price
    #item=Products.objects.get(id=key)
    r=Rewards.objects.get(id=1)
    amnt=r.coins 
    amnt=amnt-cost
    Rewards.objects.filter(id=1).update(coins=amnt)


    return redirect(index)