from fabric.api import local

def ci():
    local('python manage.py test')
    local('git add -p && git commit') # or local('hg add && hg commit')

def load():
    local('rm db.sqlite3')
    local('python manage.py syncdb --noinput')
    local('python manage.py loaddata users')
    local('python manage.py loaddata events')
