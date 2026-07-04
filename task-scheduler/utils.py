from datetime import datetime
import json
import os
from typing import List

def limpar_tela():
    """Limpa o terminal (funciona no Windows, Linux e Mac)"""
    os.system('cls' if os.name == 'nt' else 'clear')

def validar_data(data_str: str) -> bool:
    try:
        datetime.strptime(data_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validar_hora(hora_str: str) -> bool:
    try:
        datetime.strptime(hora_str, "%H:%M")
        return True
    except ValueError:
        return False

def carregar_tarefas(arquivo: str = "tasks.json") -> list:
    try:
        with open(arquivo, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def salvar_tarefas(tarefas: list, arquivo: str = "tasks.json"):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, ensure_ascii=False, indent=4)