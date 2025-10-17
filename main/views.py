import requests
from django.shortcuts import render

def index(request):
    rate = None

    if 'from_currency' in request.GET and 'to_currency' in request.GET:
        from_currency = request.GET['from_currency']
        to_currency = request.GET['to_currency']

        url = f"https://api.exchangerate.host/convert?from={from_currency}&to={to_currency}"
        response = requests.get(url)
        data = response.json()

        if data.get('success'):
            rate = data['result']

    return render(request, 'main/index.html', {'rate': rate})
