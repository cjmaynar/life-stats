from django.shortcuts import render
from django.views.generic import View

class HomeView(View):
    '''The home page.'''
    def get(self, request):
        '''If the user is not logged in show the splash page, otherwise
        show their home page'''
        if request.user.is_authenticated():
            template = 'home_loggedin.html'
        else:
            template = 'home.html'
        return render(request, template, {})
