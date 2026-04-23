class FimDeJogo(Exception):
    def __init__(self,mensagem:str):
        super().__init__(mensagem)
        self.message = mensagem