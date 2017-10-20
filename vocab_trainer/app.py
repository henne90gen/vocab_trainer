from cement.core.controller import CementBaseController, expose
from cement.core.foundation import CementApp

from .signs import signs
from .vocab import training, test
from .stats import total_asked, average_answer_time


class VocabController(CementBaseController):
    class Meta:
        label = 'base'
        arguments = []

    @expose(help="")
    def signs(self):
        signs()
        print()

    @expose(help="")
    def training(self):
        training(None)
        print()

    @expose(help="")
    def test(self):
        test(None)
        print()


class StatisticsController(CementBaseController):
    class Meta:
        label = 'stats'
        arguments = []
        stacked_on = 'base'
        stacked_type = 'nested'
        description = 'Statistics'

    @expose(help="")
    def total_asked(self):
        total_asked()

    @expose(help="")
    def average_time(self):
        average_answer_time()


class VocabApp(CementApp):
    class Meta:
        label = 'vocab_trainer'
        base_controller = 'base'
        handlers = [VocabController, StatisticsController]
