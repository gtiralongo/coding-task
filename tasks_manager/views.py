from django.views.generic import TemplateView


class Index(TemplateView):
    extra_context = {"comision": "TP Grupo 10"}
    template_name = "index.html"
