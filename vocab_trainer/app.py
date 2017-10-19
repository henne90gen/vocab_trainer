from cement.core.controller import CementBaseController, expose
from cement.core.foundation import CementApp

from .signs import signs
from .vocab import vocab
from .stats import stats


class VocabController(CementBaseController):
    class Meta:
        label = 'base'
        arguments = []

    @expose(help="")
    def signs(self):
        signs()
        print()

    @expose(help="")
    def vocab(self):
        vocab()
        print()

    @expose(help="")
    def stats(self):
        stats()


class VocabApp(CementApp):
    class Meta:
        label = 'Vocabulary-Trainer'
        base_controller = 'base'
        handlers = [VocabController]
