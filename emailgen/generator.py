
import jinja2

from .themes import DEFAULT_THEME


_default_product = {
    "name": "EmailGen",
    "copyright": "Copyright &copy; 2017, Finnesota LLC. All rights reserved."
}


class Generator(object):

    def __init__(self, theme=DEFAULT_THEME, text_direction="ltr", product=_default_product):
        """Generator facilitates the generation of emails.

        Example product
        ```
        {
            "name": "Example Corporation",
            "link": "https://example.com/",
            "logo": "https://example.com/static/images/logo.png",
            "copyright": "Copyright &copy; 2017, Example Corporation. All rights reserved.",
            "trouble": "If you're having trouble viewing this email in your email, view it <a href="#">here</a>."
        }
        ```

        :param theme: The theme that will be used when generating the email.
        :param text_direction: The html text direction of the email.
        :param product: A dictionary that provides information about your product/brand.
        """
        self.theme = theme
        self.text_direction = text_direction
        self.product = product

    def html(self, email):
        return self._generate(email, self.theme["html"])

    def plain(self, email):
        return self._generate(email, self.theme["plain"])

    def _generate(self, email, template_string):
        template = jinja2.Template(template_string)
        return str(template.render(generator=self, email=email))

