import json
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import FormView
from djng.forms import NgModelFormMixin, NgForm

class ContactForm(NgModelFormMixin, NgForm):
    form_name = 'contact_form'
    scope_prefix = 'contact_data'
    subject = fields.CharField()

class ContactFormView(FormView):
    template = 'contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('success-page')

    def post(self, request, **kwargs):
        assert request.is_ajax()
        request_data = json.loads(request.body)
        form = self.form_class(data=request_data[self.form_class.scope_prefix])
        if form.is_valid():
            return JsonResponse({'success_url': force_text(self.success_url)})
        else:
            response_data = {form.form_name: form.errors}
            return JsonResponse(response_data, status=422)