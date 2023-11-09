from .models import Product
from django.forms import ModelForm
from django_toggle_switch_widget.widgets import DjangoToggleSwitchWidget


class ProductModelForm(ModelForm):
    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            "active": DjangoToggleSwitchWidget(klass="django-toggle-switch-dark-primary"),
            "can_be_sale": DjangoToggleSwitchWidget(klass="django-toggle-switch-success"),
            "can_be_purchased": DjangoToggleSwitchWidget(klass="django-toggle-switch-success"),
        }