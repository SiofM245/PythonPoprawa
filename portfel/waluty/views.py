from django.shortcuts import render
from .modules import miner
dt = miner.miner()

def index(request):
    return render(request, 'index.html', {})

def btc(request):
    dt.czytaj('BTC')
    return render(request, 'btc.html', {})

def eth(request):
    dt.czytaj('ETH')
    return render(request, 'eth.html', {})

def ltc(request):
    dt.czytaj('LTC')
    return render(request, 'LTC.html', {})

def bnb(request):
    dt.czytaj('BNB')
    return render(request, 'BNB.html', {})

def sol(request):
    dt.czytaj('SOL')
    return render(request, 'SOL.html', {})

def ada(request):
    dt.czytaj('ADA')
    return render(request, 'ADA.html', {})

def xrp(request):
    dt.czytaj('XRP')
    return render(request, 'XRP.html', {})

def busd(request):
    dt.czytaj('BUSD')
    return render(request, 'BUSD.html', {})

def atom(request):
    dt.czytaj('ATOM')
    return render(request, 'ATOM.html', {})
