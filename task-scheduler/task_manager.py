from utils import carregar_tarefas, salvar_tarefas, validar_data, validar_hora, limpar_tela
from datetime import datetime

class TaskManager:
    def __init__(self):
        self.tarefas = carregar_tarefas()

    def adicionar_tarefa(self, descricao: str, data: str, hora_inicial: str, hora_final: str):
        if not validar_data(data):
            raise ValueError("❌ Data inválida! Use o formato YYYY-MM-DD")
        if not validar_hora(hora_inicial) or not validar_hora(hora_final):
            raise ValueError("❌ Hora inválida! Use o formato HH:MM")

        tarefa = {
            "id": len(self.tarefas) + 1,
            "descricao": descricao,
            "data": data,
            "hora_inicial": hora_inicial,
            "hora_final": hora_final,
            "concluida": False,
            "criado_em": datetime.now().isoformat()
        }
        
        self.tarefas.append(tarefa)
        salvar_tarefas(self.tarefas)

        # === Nova funcionalidade solicitada ===
        limpar_tela()
        print("✅ TAREFA CRIADA COM SUCESSO!")
        print("=" * 50)
        print(f"ID:        {tarefa['id']}")
        print(f"Descrição: {tarefa['descricao']}")
        print(f"Data:      {tarefa['data']}")
        print(f"Horário:   {tarefa['hora_inicial']} - {tarefa['hora_final']}")
        print("=" * 50)
        print("\nTarefa adicionada com sucesso!\n")
    def listar_tarefas(self, apenas_pendentes: bool = False):
        tarefas_filtradas = [t for t in self.tarefas if not apenas_pendentes or not t["concluida"]]
        
        if not tarefas_filtradas:
            print("Nenhuma tarefa encontrada.")
            return

        print("\n" + "="*80)
        print(f"{'ID':<4} {'Data':<12} {'Horário':<13} {'Status':<10} Descrição")
        print("="*80)
        
        for t in tarefas_filtradas:
            status = "✓ Concluída" if t["concluida"] else "⏳ Pendente"
            print(f"{t['id']:<4} {t['data']:<12} {t['hora_inicial']}-{t['hora_final']:<13} {status:<10} {t['descricao']}")
        print("="*80)

    def marcar_concluida(self, tarefa_id: int):
        for t in self.tarefas:
            if t["id"] == tarefa_id:
                t["concluida"] = True
                salvar_tarefas(self.tarefas)
                print(f"Tarefa #{tarefa_id} marcada como concluída!")
                return
        print("Tarefa não encontrada.")

    def remover_tarefa(self, tarefa_id: int):
        for i, t in enumerate(self.tarefas):
            if t["id"] == tarefa_id:
                del self.tarefas[i]
                salvar_tarefas(self.tarefas)
                print(f"Tarefa #{tarefa_id} removida!")
                return
        print("Tarefa não encontrada.")