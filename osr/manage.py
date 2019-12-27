import os
import sys

# © by w-team
# Владимир Киселев
# Саплев Максим
# Харитонов Игорь
# Назаренко Денис
# Мальнев Андрей
# Незаконное распространение данного программного продукта карается законом РФ

def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'osr.settings')
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
