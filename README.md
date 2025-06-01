# **Controle de Equipamentos**




Este software foi desenvolvido para simplificar e otimizar o controle de equipamentos, com foco inicial em **geladeiras**, dentro de qualquer organização. Funcionalidades para gerenciar o ciclo de vida completo de cada equipamento, desde o seu registro até a sua baixa.

### **Funcionalidades Principais:**

* **`cadastrar_equipamento()`**: Registre novos equipamentos no sistema, incluindo informações detalhadas como gesp, código do modelo e o modelo.
* **`cadastrar_responsavel()`**: Mantenha um registro de todos os responsáveis por equipamentos, associando-os a um equipamento específico.
* **`emprestar_equipamento()`**: Facilite o processo de empréstimo de equipamentos, registrando quem está com o item e tualizando seu status para "emprestado"
* **`devolver_equipamento()`**: Registre a devolução de equipamentos, atualizando seu status para "disponível" e liberando-o para um novo uso.
* **`dar_baixa_equipamento()`**: Gerencie a desativação de equipamentos por motivo de descarte, quebra ou perda.
* **`listagem_equipamentos()`**: Acesse uma lista completa de todos os equipamentos cadastrados, com filtros e opções de visualização.



## **Tecnologias Utilizadas**

- **Python 3.11.4+**
- **Tkinter 8.4+**
- **Sqlite3 3.45.3+**


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
│   ├── frames.py
│   ├── interface.py
|
├── servicos/
|   │   
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
