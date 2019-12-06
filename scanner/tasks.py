from celery import shared_task
import subprocess


@shared_task
def scan(host=None):
    result = subprocess.run(
        ['nmap', '-A', '-v', host],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    return result.stdout.decode()
