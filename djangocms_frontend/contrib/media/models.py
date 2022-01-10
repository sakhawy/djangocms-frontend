from cms.models import CMSPlugin

from djangocms_frontend.fields import AttributesField, TagTypeField
from djangocms_frontend.models import FrontendUIItem


class Media(FrontendUIItem):
    """
    Layout > "Media" Plugin
    http://getbootstrap.com/docs/4.0/layout/media-object/
    """

    class Meta:
        proxy = True

    def get_short_description(self):
        return ""


class MediaBody(FrontendUIItem):
    """
    Layout > "Media body" Plugin
    http://getbootstrap.com/docs/4.0/layout/media-object/
    """

    class Meta:
        proxy = True

    def get_short_description(self):
        return ""
