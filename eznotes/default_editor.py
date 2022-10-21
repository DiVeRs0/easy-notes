import os
import readline

from .const import DEFAULT_EDITOR_FILE_PATH
from .logs import DefaultEditorLogs
from .logs.error import executable_does_not_exist_error
from .utils import executable_exists


def editor_file_exists():
    return True if os.path.isfile(DEFAULT_EDITOR_FILE_PATH) else False


def change_default_editor(new_editor):
    if executable_exists(new_editor):
        with open(DEFAULT_EDITOR_FILE_PATH, "w") as f:
            f.write(new_editor)
    else:
        executable_does_not_exist_error(new_editor)


def get_default_editor():
    with open(DEFAULT_EDITOR_FILE_PATH) as f:
        default_editor = f.read().strip()
    return default_editor


def editor_initiate():
    # added this because sometimes the db might be not
    # configured properly and in those cases this function
    # also gets called.
    if editor_file_exists():
        return

    logs = DefaultEditorLogs()
    logs.first()

    editor_exists = False
    while not editor_exists:
        logs.input_prompt()
        new_editor = input()
        if new_editor == "":
            new_editor = "vim"
        editor_exists = executable_exists(new_editor)
    change_default_editor(new_editor)
