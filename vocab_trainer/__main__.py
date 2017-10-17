from .app import VocabApp

if __name__ == '__main__':
    with VocabApp() as app:
        app.run()
