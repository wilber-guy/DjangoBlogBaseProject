from django.apps import AppConfig


class UsersConfig(AppConfig):
    name = 'users'

    # this links to functions that create a profile everytime a user is created and links them together
    def ready(self):
        import users.signals
