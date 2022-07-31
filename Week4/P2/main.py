from menu import Menu, Command, CommandOptions
from calc_funcs import GradeStatsCalc
from file import PromptFile


class App:
    _file = PromptFile()
    _calc = GradeStatsCalc()

    def __init__(self):
        _command_options_map = {
            "1": Command("Load data from new file.", self._load),
            "2": Command("Display computed stats.", self._calc.display_stats),
            "3": Command("Save computed stats.", self._save),
            "4": Command("Exit.", self._exit),
        }
        self.menu = Menu(CommandOptions(_command_options_map))
    
    def run(self):
        self.welcome()
        self.menu.run()

    def welcome(self):
        print(
            "\nWelcome to Grade Stats App! To begin please provide the file",
            "whos statistics you would like to calculate.\n"
        )
        self._load()

    def _load(self):
        self._file.prompt_load()
        self._calc.set_stats(self._file.get_data())
    
    def _save(self):
        self._file.receive_data(self._calc.get_stats_str())
        self._file.prompt_save()

    def _exit(self):
        print("Goodbye!")
        exit()

if __name__ == "__main__":
    App().run()