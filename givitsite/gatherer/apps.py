from django.apps import AppConfig
from django.db.models.signals import post_migrate


def my_callback(sender, **kwargs):
    from gatherer.tasks import gatherer_task
    from background_task.models import Task
    gatherer_task(repeat=Task.HOURLY, repeat_until=None)
    pass


class GathererConfig(AppConfig):
    name = 'gatherer'

    def ready(self):
        post_migrate.connect(my_callback, sender=self)
