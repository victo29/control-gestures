import subprocess

from app.infra.actions.interfaces.gesture_action import GestureActions as GestureActionsInterface

class GestureActions(GestureActionsInterface):

    def __init__(self):
        self.notepad_process = None

    def handle(self, gesture:str):
        if gesture == "EXIT":
            exit()
        elif gesture == "OPEN_NOTEPAD" and self.notepad_process is None:
            self.notepad_process = subprocess.Popen("notepad", shell=True)
