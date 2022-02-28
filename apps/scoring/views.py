from django.template.response import TemplateResponse

from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)


def form(request):
    return TemplateResponse(request, 'scoring/Form.html', {})
