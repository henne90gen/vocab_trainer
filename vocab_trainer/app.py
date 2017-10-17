from cement.core.controller import CementBaseController, expose
from cement.core.foundation import CementApp

from .signs import signs


class VocabController(CementBaseController):
    class Meta:
        label = 'base'
        arguments = []

    @expose(help="")
    def signs(self):
        signs()

    @expose(help="")
    def stats(self):
        # TODO use matplotlib to show statistics
        pass


class VocabApp(CementApp):
    class Meta:
        label = 'Vocabulary-Trainer'
        base_controller = 'base'
        handlers = [VocabController]
