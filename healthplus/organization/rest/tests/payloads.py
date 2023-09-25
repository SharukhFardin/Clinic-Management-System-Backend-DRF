from django.contrib.auth import get_user_model


def create_doctor():
    pass


def create_user():
    pass


def create_patient():
    pass


def doctor_registration_payload():
    payload = {
        "name": "John Doe",
        "phone_number": "1234567890",
        "email": "johndoe@example.com",
        "password": "testpassword",
        "address": "123 Main St",
        "designation": "Test Designation",
        "specialty": "Test Specialty",
        "expertise": "Test Expertise",
    }

    return payload


def patient_registration_payload():
    payload = {
        "name": "Jane Doe",
        "phone_number": "9876543210",
        "email": "janedoe@example.com",
        "password": "testpassword",
        "address": "456 Elm St",
    }

    return payload
