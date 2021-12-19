from django import forms
from django.utils.translation import gettext_lazy as _
from entangled.forms import EntangledModelForm

from djangocms_frontend.models import FrontendUIItem
from djangocms_frontend.settings import COLOR_STYLE_CHOICES


class BadgeForm(EntangledModelForm):
    """
    Components > "Badge" Plugin
    https://getbootstrap.com/docs/5.0/components/badge/
    """

    class Meta:
        model = FrontendUIItem
        entangled_fields = {
            "config": [
                "badge_text",
                "badge_context",
                "badge_pills",
            ]
        }
        untangled_fields = ("tag_type", "attributes")

    badge_text = forms.CharField(
        label=_("Badge text"),
        max_length=255,
    )
    badge_context = forms.ChoiceField(
        label=_("Context"),
        choices=COLOR_STYLE_CHOICES,
        initial=COLOR_STYLE_CHOICES[0][0],
    )
    badge_pills = forms.BooleanField(
        label=_("Pills style"),
        initial=False,
        required=False,
        help_text=_("Activates the pills style."),
    )