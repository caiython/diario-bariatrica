from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.utils.timezone import now
from api.models import RegistroDiarioModel


class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "app/index.html"
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        year = self.kwargs.get('year')
        month = self.kwargs.get('month')
        day = self.kwargs.get('day')

        if year and month and day:
            try:
                date_created = now().replace(year=int(year), month=int(month), day=int(day)).date()
            except ValueError:
                date_created = now().date()
        else:
            date_created = now().date()

        registro = RegistroDiarioModel.objects.filter(
            user=self.request.user, date_created=date_created
        ).first()

        context['registro'] = registro
        context['selected_date'] = date_created
        return context
