from cement.core.controller import CementBaseController, expose
from cement.core.foundation import CementApp

from vocab_trainer.util import load_vocab
from .signs import signs
from .vocab import training, test
from .stats import total_asked, average_answer_time


class VocabController(CementBaseController):
    class Meta:
        label = 'base'
        arguments = [
            (['-c', '--chapter'],
             dict(help='chapter to select', action='store')),
            (['-l', '--language'],
             dict(help='0=Japanese, 1=German', action='store')),
            (['sign_string'],
             dict(action='store', nargs='?'))
        ]

    def get_language(self):
        lang = self.app.pargs.language
        if not lang or lang not in ['0', '1']:
            return None
        return int(lang)

    def get_chapter(self):
        return self.app.pargs.chapter

    @expose(help="Lists all available chapters")
    def list(self):
        vocab = load_vocab()
        print("There are", len(vocab.keys()), "chapters.")
        print(', '.join(vocab.keys()))

    @expose(help="")
    def signs(self):
        signs(self.app.pargs.sign_string)
        print()

    @expose(help="")
    def training(self):
        chapter = self.get_chapter()
        lang = self.get_language()
        training(chapter, lang)
        print()

    @expose(help="")
    def test(self):
        chapter = self.get_chapter()
        lang = self.get_language()
        test(chapter, lang)
        print()


class StatisticsController(CementBaseController):
    class Meta:
        label = 'stats'
        arguments = []
        stacked_on = 'base'
        stacked_type = 'nested'
        description = 'Awesome statistics'

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
