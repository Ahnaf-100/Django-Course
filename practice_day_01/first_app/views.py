from django.shortcuts import render
import datetime

# Create your views here.


def home(request):



    d = {
        'author' : 'rahim',
        'age' : 20,
        'value' : ['a','b','c','d'],
        'intro' : "I'm Rahim",
        'val' : 'string with spaces',
        'birthdate' : datetime.datetime.now(),
        'x' :'',
        'lst' : [
                    {'name': 'zed', 'age': 19},
                    {'name': 'amy', 'age': 22},
                    {'name': 'joe', 'age': 31},
                ],
        'sum' : 123456789,
        'num' : 'one'
                "two"
               "three",
        'post' : 'my FIRST post',
        # 'var' :  [‘States’, [‘Kansas’, [‘Lawrence’, ‘Topeka’], ‘Illinois’]],
    }

    

    return render(request,'home.html',d)