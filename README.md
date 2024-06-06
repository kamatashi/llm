# Tutorial para Rodar o Código

Esse readme é um guia para executar os códigos do pipeline usando um ambiente virtual com o UV, um gerenciador de pacotes global para Python.

### Passos para Configuração e Execução

1.  **Instalar o UV**

    Baixe e UV e o ative:

    ``` cmd
    pip install uv
    ```

    ``` cmd
    uv venv 
    ```

    ``` cmd
    source .venv/bin/activate
    ```

2.  **Baixar as bibliotecas**

    ``` cmd
    uv pip install -r requirements.txt
    ```

3.  **Rodar o código**

    ``` cmd
    cd pipeline
    ```

    ``` python
    python3 zero-shot.py
    ```