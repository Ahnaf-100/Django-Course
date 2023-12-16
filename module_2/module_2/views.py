from django.shortcuts import render

def home(request):
    d = {
        'author' : 'Rahim',
        'age' : 20,
        'lst' : [1,2,3,4,5],

        'courses' : [
        {
            'name' : 'python',
            'fee' : 5000
        },
        {
            'name' : 'c',
            'fee' : 5000
        },
        {
            'name' : 'java',
            'fee' : 5000
        } 
        
    ]
    }
    
    return render(request,'index.html',d)