from django.apps import AppConfig


class NamelistConfig(AppConfig):
    name = 'namelist'
    verbose_name = "Lista de nomes do capeta"
    def ready(self):
        import namelist.signals