from django.shortcuts import render

# Create your views here.
def index(request,product,EA):
    
    product_price = {
        "라면":980,
        "홈런볼":1500,
        "칙촉":2300, 
        "식빵":1800
        }
    if product in product_price:
        price = product_price[product]
    else:
        price = 0
    
    context = {
        "product_price" : product_price,
        "product" : product,
        "EA" : EA,
        "price" : price
        
    }

    return render(request, 'prices/price.html', context)