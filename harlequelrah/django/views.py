from django.contrib.auth.views import LoginView


class CustomLoginView(LoginView):
    template_name = "authentification/login.html"
    redirect_authenticated_user = True

    def form_valid(self, form):
        messages.success(self.request, "Vous êtes connecté avec succès.")
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, "Identifiants invalides.")
        return super().form_invalid(form)
