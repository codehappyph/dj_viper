from celery import current_app

import os
import subprocess

from django.conf import settings


@current_app.task(bind=True)
def run_duck_search(self, query):
    params = [
        'python',
        os.path.join(
            settings.SCRIPT_DIR, 'ducksearch.py'
        ),
        query,
    ]
    subprocess.check_call(params)