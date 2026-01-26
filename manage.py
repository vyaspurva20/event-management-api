#!/usr/bin/env python
import os
import sys


def main():
    # 👇 ADD THIS LINE HERE (TEMPORARY – ONLY FOR TESTING AGENT)
    raise Exception("CI agent test failure")

    os.environ.setdefault(
        "DJANGO_SETTINGS_MODULE",
        "config.settings"   # this matches your repo structure
    )

    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable?"
        ) from exc

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
