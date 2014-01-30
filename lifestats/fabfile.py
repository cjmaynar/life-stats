from fabric.api import local

def ci():
    local('python manage.py test')
    local('git add -p && git commit')

def load():
    local('rm db.sqlite3')
    local('python manage.py syncdb --noinput')
    local('python manage.py autofixtures -u 2 -e 20')
