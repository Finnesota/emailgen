EmailGen
========

Python Email Generation for Humans

EmailGen is a python port of the great mailgen engine for Node.js. Check their
work, it's awesome! It's a package that generates clean, responsive HTML
e-mails for sending transactional e-mails (welcome e-mails, reset password
e-mails, receipt e-mails and so on), and associated plain text fallback.

## Installation

```
$ pip install emailgen
```

## Usage

Start by importing the library and configuring a generator.


```python
import emailgen

# For most simple use cases, this should be all you need to define.
generator = emailgen.Generator(product={
    "name": "Example Corporation",
    "link": "https://example.com/",
    "logo": "https://example.com/static/images/logo.png",
    "copyright": "Copyright &copy; 2017, Example Corporation. All rights reserved.",
    "trouble": "If you're having trouble viewing this email in your email, view it <a href="#">here</a>."
})
```

Next, you can generate an email by creating an instance of `Email`, adding in
the content pieces you want and then generating the email with your newly
configured generator.

```python
email = emailgen.Email("John Doe")  # Enter in the name of the recipient
email.add_intro("Welcome to our product! We're very excited to have you on board.")
email.add_action("To get started with Hermes, please click here:",
                 emailgen.Button("Confirm your account", "http://example.com/confirm-account"))
email.add_outros("Need help, or have questions? Just reply to this email, we'd love to help.")

html_output = generator.html(email)
plain_text_output = generator.plain(email)
```
