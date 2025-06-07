# **Controle de Equipamentos**

Este software foi desenvolvido para simplificar e otimizar o controle de equipamentos, com foco inicial em **geladeiras**, dentro de qualquer organização. Funcionalidades para gerenciar o ciclo de vida completo de cada equipamento, desde o seu registro até a sua baixa.

## **Funcionalidades Principais:**

### Equipamentos:
* **`cadastrar_equipamento()`**: Registre novos equipamentos no sistema, incluindo informações detalhadas como gesp, código do modelo e o modelo.

* **`alterar_informacoes_equipamento()`**: Permite alterar informações de equipamentos já cadastrados.

* **`excluir_equipamentos()`**: Faz a exclusão de equipamentos do sistema para sempre.

* **`emprestar_equipamento()`**: Facilite o processo de empréstimo de equipamentos, registrando quem está com o item e tualizando seu status para "emprestado"

* **`devolver_equipamento()`**: Registre a devolução de equipamentos, atualizando seu status para "disponível" e liberando-o para um novo uso.

* **`dar_baixa_equipamento()`**: Gerencie a desativação de equipamentos por motivo de descarte, quebra ou perda.

### Responsáveis:
* **`cadastrar_responsavel()`**: Mantenha um registro de todos os responsáveis por equipamentos, associando-os a um equipamento específico.

* **`alterar_informacoes_responsavel()`**: Permite a alteração de informações de um responsável já cadastrado.

* **`excluir_responsavel()`**: Permite a exclusão de responsáveis cadastrados.

### Listagem

* **`listagem_equipamentos()`**: Acesse uma lista completa de todos os equipamentos cadastrados, com filtros e opções de visualização.

* **`listagem_responsaveis()`**: Permite acessar uma lista completa de todos os responsáveis cadastrados com filtros.

* **`listagem_clientes()`**: Permite o acesso a uma lista com todos os clientes cadastrados no sistema, com filtros.



## **Tecnologias Utilizadas**

- **Python 3.11.4+**
- **Tkinter 8.4+**
- **Sqlite3 3.45.3+**

## **Banco de Dados**

- **`Clientes`** - Contém todos os clientes. Com nome e razão social.

- **`Responsáveis`** - Contém os responsáveis atrelados aos clientes. Com código do cliente, nome, cpf e o email.

- **`Equipamentos`** - Contém todos os equipamentos (geladeiras). Com o gesp, código do modelo e a descrição do modelo.

- **`Equipamentos Emprestados`** - Contém os equipamentos emprestados, junto código do cliente onde o equipamento está. Com o gesp, código do cliente e o número do contrato.



## **Estrutura do Projeto**

```

├── app/
│   ├── main.py
|
├── backend/
|   │   
│   ├── validadores/
|   │   ├── __init__.py
|   │   ├── equipamentos.py
|   │   ├── responsaveis.py
|   |
|   ├── __init__.py
│   ├── controlador_equipamentos.py
│   ├── controlador_responsaveis.py
│   ├── controlador_listagem.py
|
├── database/
|   │   
|   ├── __init__.py
│   ├── banco_de_dados.py
│   ├── clientes.py
│   ├── equipamentos_emprestados.py
│   ├── equipamentos.py
│   ├── responsaveis.py
│   
├── frontend/
|   │   
|   ├── __init__.py
│   ├── frame_baixa.py
│   ├── frame_devolver.py
│   ├── frame_emprestrar.py
│   ├── frame_equipamentos.py
│   ├── frame_listagem.py
│   ├── frame_responsavel.py
│   ├── interface.py
│   ├── janela.py
|
├── servicos/
|   │   
│   ├── servico_banco_de_dados/
|   │   ├── __init__.py
|   │   ├── inicializador.py
|   |
|   ├── __init__.py
│   ├── servico_clientes.py
│   ├── servico_equipamentos.py
│   ├── servico_responsaveis.py
|
├── .gitignore
├── README.md
```

## **Como Executar**

1. Acesse a pasta `app/`
2. Execute o `main.py`.
   ```bash
   python main.py
   ```



## **Autoria**
- Lucas Pereira Silva Mello

<br>

Fique à vontade para contribuir!
