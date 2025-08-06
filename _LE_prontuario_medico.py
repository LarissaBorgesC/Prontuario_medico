
class Prontuario:
    def __init__(self, paciente, diagnostico, tratamento, proximo=None):
        self.paciente = paciente
        self.diagnostico = diagnostico
        self.tratamento = tratamento
        self.proximo = proximo

    
    def __repr__(self):
        return f"{self.__class__.__name__}: paciente={self.paciente}, diagnostico={self.diagnostico}, tratamento={self.tratamento}"



class LE_prontuarios:
    def __init__(self):
        self.cabeca = None

    def insert_prontuario(self, paciente, diagnostico, tratamento):
        novo_pronturario = Prontuario(paciente, diagnostico, tratamento, self.cabeca)
        self.cabeca = novo_pronturario

    def select_pronturario(self, nome_paciente):
        atual = self.cabeca
        
        while atual is not None:
            if atual.paciente == nome_paciente:
                return atual
            atual = atual.proximo
        else:
            return f"{nome_paciente} não encontrado!"
        
    def remove_prontuario(self, nome_paciente):
        if self.cabeca is None:
            return None
        
    
        if self.cabeca.paciente == nome_paciente:
            prontuario_removido = self.cabeca
            self.cabeca = self.cabeca.proximo
            return prontuario_removido 

        atual = self.cabeca
        anterior = None

        while atual is not None and atual.paciente != nome_paciente:
            anterior = atual
            atual = atual.proximo
        
        if atual is not None:
            anterior.proximo = atual.proximo
            return atual
        
        return f"{nome_paciente} não encontrado!"
    

    

Sistema_prontuarios = LE_prontuarios()
Sistema_prontuarios.insert_prontuario("Alice Santos", "Diabetes TIPO 2", "Metformina")
Sistema_prontuarios.insert_prontuario("João Silva", "Hipertensão", "Losartana")
Sistema_prontuarios.insert_prontuario("Marcelo Fontes", "Hernia", "Cirurgia laparoscópica")
print(Sistema_prontuarios.select_pronturario("João Silva"))
print(Sistema_prontuarios.remove_prontuario("Alice Santos"))
print(Sistema_prontuarios.select_pronturario("Alice Santos"))
