from organization.models import User


class UserService:
    def create_user(
        self,
        phone: str,
        password: str,
        name: str = "",
        email: str = "",
        is_active: bool = True,
    ) -> User:
        return User.objects.create_user(
            name=name,
            phone=phone,
            password=password,
            email=email,
            is_active=is_active,
        )

    def get_user_by_phone(self, phone: str) -> User:
        return User.objects.get(phone=phone)

    def get_user_by_email(self, email: str) -> User:
        return User.objects.get(email=email)

    def get_user_by_either_phone_or_email(self, value) -> User:
        try:
            return self.get_user_by_email(email=value)

        except User.DoesNotExist:
            return self.get_user_by_phone(phone=value)
