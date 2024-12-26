from django.views.generic import CreateView
from django.http import HttpResponseRedirect
from .models import RegistroDiarioModel


class RegistroDiarioCreateView(CreateView):
    model = RegistroDiarioModel
    fields = ['musculacao', 'aerobico', 'agua', 'vitaminas',
              'zero_alcool', 'zero_acucar', 'zero_doces', 'observacoes']
    template_name = 'preferences_form.html'

    def form_valid(self, form):
        date_created = self.request.POST.get('date_created')
        registro_existente = RegistroDiarioModel.objects.filter(
            user=self.request.user, date_created=date_created
        ).first()

        if registro_existente:
            for field in self.fields:
                setattr(registro_existente, field, form.cleaned_data[field])
            registro_existente.save()
            self.object = registro_existente
        else:
            form.instance.user = self.request.user
            form.instance.date_created = date_created
            self.object = form.save()

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return self.request.META.get('HTTP_REFERER', '/')
