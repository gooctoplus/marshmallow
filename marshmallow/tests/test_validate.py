import pytest
from marshmallow import ValidationError
from marshmallow.validate import Email

def test_email_validation():
    valid_emails = [
        "email@domain.com",
        "firstname.lastname@domain.com",
        "email@subdomain.domain.com",
        "firstname+lastname@domain.com",
        "email@123.123.123.123",
        "email@[123.123.123.123]",
        "\"email\"@domain.com",
        "1234567890@domain.com",
        "email@domain-one.com",
        "_______@domain.com",
        "email@domain.name",
        "email@domain.co.jp",
        "firstname-lastname@domain.com"
    ]
    
    invalid_emails = [
        "plainaddress",
        "@missingusername.com",
        "email.domain.com",
        "email@domain@domain.com",
        ".email@domain.com",
        "email.@domain.com",
        "email..email@domain.com",
        "email@domain.com (Joe Smith)",
        "email@domain",
        "email@-domain.com",
        "email@domain..com",
        "email@domain.com\n",
        "email\n@domain.com",
        "email\n@domain.com\n"
    ]

    validator = Email()

    for valid_email in valid_emails:
        validator(valid_email)  # Should not raise an exception

    for invalid_email in invalid_emails:
        with pytest.raises(ValidationError):
            validator(invalid_email)  # Should raise a ValidationError