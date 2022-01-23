from cms.api import add_plugin
from cms.test_utils.testcases import CMSTestCase

from djangocms_frontend.contrib.badge.cms_plugins import (
    BadgePlugin,
)

from ..fixtures import TestFixture


class BadgePluginTestCase(TestFixture, CMSTestCase):

    def test_plugin(self):
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=BadgePlugin.__name__,
            language=self.language,
            badge_text="some text",
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            '<span class="badge badge-primary">some text</span>',
            html=True,
        )

        # test with pills enabled
        plugin = add_plugin(
            placeholder=self.placeholder,
            plugin_type=BadgePlugin.__name__,
            language=self.language,
            badge_text="some text",
            badge_pills=True,
        )
        plugin.full_clean()
        self.page.publish(self.language)

        with self.login_user_context(self.superuser):
            response = self.client.get(self.request_url)
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            '<span class="badge badge-pill badge-primary">some text</span>',
            html=True,
        )