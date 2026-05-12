from django.shortcuts import render, redirect

# Create your views here.

from django.contrib.auth.views import LoginView
from django.contrib import messages



def inicio(request):
    return render(request, 'inicio/index.html')


class CustomLoginView(LoginView):
    def form_valid(self, form):
        # Aquí ya autenticamos al usuario
        user = form.get_user()
        if not user.is_active:
            messages.error(self.request, "Tu usuario está desactivado")
            return redirect("inicio")
        return super().form_valid(form)