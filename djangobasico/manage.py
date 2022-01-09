#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    # Variáveis de ambiente 
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangobasico.settings')
    try:
        # Importa um módulo para aceitar comandos via terminal
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    # Executa conforme os argumentos
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
