from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import FormView
from .forms import FarmerImport
# Create your views here.


class ViewImportFarmer(LoginRequiredMixin, FormView):
    template_name = "admin/import.html"
    form_class = FarmerImport
    success_url = reverse_lazy('import-farmer')

    def form_valid(self, form):
        context = FormView.get_context_data(self)
        context['excel'] = form.send_file()
        return FormView.render_to_response(self, context)
