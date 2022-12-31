from django.shortcuts import render

# Create your views here.
def filters(request):
    import datetime
    dt=datetime.date.today()
    d={'data':'HAi DJANgo and PYthon','dt':dt,'c':2}
    return render(request,'filters.html',d)
def userdefinedfilters(request):
    d={'data':'HI python HOW are YOU'}
    return render(request,'userdefinedfilters.html',d)