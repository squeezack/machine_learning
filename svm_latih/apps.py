from django.apps import AppConfig


class SvmLatihConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'svm_latih'

    def ready(self):
        import svm_latih.views
        svm_latih.views.populate_database()

