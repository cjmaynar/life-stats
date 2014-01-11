from fabric.api import local

def ci():
    local('python manage.py test events')
    local('git add -p && git commit') # or local('hg add && hg commit')
