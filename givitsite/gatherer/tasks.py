from __future__ import unicode_literals
from background_task import background
from .agora import givit_main


@background(schedule=60)
def gatherer_task():
    givit_main()
