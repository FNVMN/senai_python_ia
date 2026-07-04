import argparse
from task_manager import TaskManager


def main():
    manager = TaskManager()
    parser = argparse.ArgumentParser(description="Agendador de Tarefas - CLI")
    subparsers = parser.add_subparsers(dest="comando", help="Comandos disponíveis")

    # Adicionar tarefa
    add = subparsers.add_parser("add", help="Adicionar nova tarefa")
    add.add_argument("descricao", help="Descrição da tarefa")
    add.add_argument("data", help="Data (YYYY-MM-DD)")
    add.add_argument("hora_inicial", help="Hora inicial (HH:MM)")
    add.add_argument("hora_final", help="Hora final (HH:MM)")

    # Listar
    subparsers.add_parser("list", help="Listar todas as tarefas")
    subparsers.add_parser("pendentes", help="Listar apenas tarefas pendentes")

    # Concluir
    complete = subparsers.add_parser("complete", help="Marcar tarefa como concluída")
    complete.add_argument("id", type=int, help="ID da tarefa")

    # Remover
    remove = subparsers.add_parser("remove", help="Remover tarefa")
    remove.add_argument("id", type=int, help="ID da tarefa")

    args = parser.parse_args()

    try:
        if args.comando == "add":
            manager.adicionar_tarefa(args.descricao, args.data, args.hora_inicial, args.hora_final)
        elif args.comando == "list":
            manager.listar_tarefas()
        elif args.comando == "pendentes":
            manager.listar_tarefas(apenas_pendentes=True)
        elif args.comando == "complete":
            manager.marcar_concluida(args.id)
        elif args.comando == "remove":
            manager.remover_tarefa(args.id)
        else:
            parser.print_help()
    except ValueError as e:
        print(f"\n❌ Erro: {e}")
    except Exception as e:
        print(f"\n❌ Erro inesperado: {e}")


if __name__ == "__main__":
    main()