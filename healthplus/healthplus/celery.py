import os

from celery import Celery

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "proj.settings")

app = Celery("healthplus")

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django apps.
app.autodiscover_tasks()


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f"Request: {self.request!r}")


"""
Celery Workter : A seperate proess that executes tasks. Workers listen to
message broker. When a task is recieved, a worker picks it up, executes it and
optionally sends back the response. We cam have multiple workers.

celery Message Broker : A message broker is a middleware that facilitates
communication between the application and Celery workers. Popular message 
brokrs used in celery are Redis, RabbitMQ, Apache Kafka and Amazon SQS.

"""
