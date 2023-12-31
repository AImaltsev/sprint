#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import os

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()


# Путь к каталогу bin в установке PostgreSQL
pgsql_bin_path = r'C:\Program Files\PostgreSQL\16rc1\bin'

# Добавить bin в переменную PATH
os.environ['PATH'] = f'{pgsql_bin_path};{os.environ["PATH"]}'


