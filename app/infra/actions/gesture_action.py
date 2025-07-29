import subprocess
import os

from app.infra.actions.interfaces.gesture_action import GestureActions as GestureActionsInterface

class GestureActions(GestureActionsInterface):

    def __init__(self):
        self.__notepad_process = None
        self.__calc_process = None

    def handle(self, gesture:str):
        if gesture == "EXIT":
            exit()
        elif gesture == "OPEN_NOTEPAD" and self.__notepad_process is None:
            self.__notepad_process = subprocess.Popen("notepad", shell=True)
        elif gesture == "OPEN_CALC" and self.__calc_process is None:
            self.__calc_process = subprocess.Popen("calc", shell=True)
        elif gesture == "CLOSE_ALL":
            self.__close_all()

    def __close_all(self):
        if self.__calc_process:
            os.system("TASKKILL /IM CalculatorApp.exe /F")
            self.__calc_process = None
        if self.__notepad_process:
            os.system("TASKKILL /IM notepad.exe /F")
            self.__notepad_process = None
