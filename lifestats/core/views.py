from django.contrib.auth.models import User
from django.views.generic import CreateView

class RegisterView(CreateView):
    template_name = 'register.html'
    model = User
    fields = ['username', 'password', 'email']

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.set_password(form.instance.password)
        self.object.save()
        return super(RegisterView, self).form_valid(form)
