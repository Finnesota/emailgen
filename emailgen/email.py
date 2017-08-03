
import markdown2


class Email(object):

    def __init__(self, name):
        self.name = name
        self.intros = []
        self.dictionary = []
        # self.table =
        self.actions = []
        self.outros = []
        self.greeting = "Hey"
        self.signature = "Yours truly"
        self.title = None
        self.raw_markdown = None
        self.free_markdown = None

    def add_intro(self, intro):
        self.intros.append(intro)

    def add_dictionary(self, key, value):
        self.dictionary.append((key, value))

    def add_action(self, text, button):
        self.actions.append((text, button))

    def add_outros(self, outro):
        self.outros.append(outro)

    def markdown(self, md):
        self.raw_markdown = md
        self.free_markdown = markdown2.markdown(md)


class Button(object):

    def __init__(self, text, link, color="red"):
        self.text = text
        self.link = link
        self.color = color
