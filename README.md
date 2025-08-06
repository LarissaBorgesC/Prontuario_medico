# Sistema de Gerenciamento de Prontuários Médicos

Este projeto implementa uma **lista encadeada simples** em Python para gerenciar prontuários médicos, permitindo inserir, consultar e remover registros de pacientes.

## Descrição

O código contém duas classes principais:
- **`Prontuario`**: Representa um prontuário médico com informações do paciente, diagnóstico e tratamento.
- **`LE_prontuarios`**: Implementa uma lista encadeada para armazenar e gerenciar múltiplos prontuários.

### Funcionalidades
- **Inserção**: Adiciona um novo prontuário no início da lista.
- **Consulta**: Busca um prontuário pelo nome do paciente.
- **Remoção**: Remove um prontuário da lista com base no nome do paciente.

## Estrutura do Código

### Classe `Prontuario`
- **Atributos**:
  - `paciente`: Nome do paciente (string).
  - `diagnostico`: Diagnóstico médico (string).
  - `tratamento`: Tratamento prescrito (string).
  - `proximo`: Ponteiro para o próximo prontuário na lista (objeto `Prontuario` ou `None`).
- **Método `__repr__`**:
  - Retorna uma representação em string do prontuário, exibindo apenas `paciente`, `diagnostico` e `tratamento`.

### Classe `LE_prontuarios`
- **Atributos**:
  - `cabeca`: Referência ao primeiro nó da lista encadeada (`Prontuario` ou `None`).
- **Métodos**:
  - `insert_prontuario(paciente, diagnostico, tratamento)`: Insere um novo prontuário no início da lista.
  - `select_pronturario(nome_paciente)`: Busca um prontuário pelo nome do paciente e retorna o objeto `Prontuario` ou uma mensagem de erro se não encontrado.
  - `remove_prontuario(nome_paciente)`: Remove o prontuário de um paciente e retorna o objeto `Prontuario` removido ou uma mensagem de erro se não encontrado.

## Requisitos
- Python 3.x

## Como Usar
1. Crie uma instância de `LE_prontuarios`.
2. Use `insert_prontuario` para adicionar prontuários.
3. Use `select_pronturario` para consultar um prontuário pelo nome do paciente.
4. Use `remove_prontuario` para remover um prontuário.

### Exemplo de Uso
```python
# Criar uma lista de prontuários
Sistema_prontuarios = LE_prontuarios()

# Inserir prontuários
Sistema_prontuarios.insert_prontuario("Alice Santos", "Diabetes TIPO 2", "Metformina")
Sistema_prontuarios.insert_prontuario("João Silva", "Hipertensão", "Losartana")
Sistema_prontuarios.insert_prontuario("Marcelo Fontes", "Hernia", "Cirurgia laparoscópica")

# Consultar um prontuário
print(Sistema_prontuarios.select_pronturario("João Silva"))
# Saída: Prontuario: paciente=João Silva, diagnostico=Hipertensão, tratamento=Losartana

# Remover um prontuário
print(Sistema_prontuarios.remove_prontuario("Alice Santos"))
# Saída: Prontuario: paciente=Alice Santos, diagnostico=Diabetes TIPO 2, tratamento=Metformina

# Verificar se o prontuário foi removido
print(Sistema_prontuarios.select_pronturario("Alice Santos"))
# Saída: Alice Santos não encontrado!
