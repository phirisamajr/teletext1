from django.apps import AppConfig


class StudentResultsConfig(AppConfig):
    name = 'student_results'

    def ready(self):
        import student_results.signals
