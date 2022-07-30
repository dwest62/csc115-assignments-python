from dataclasses import dataclass
from types import FunctionType
from typing import Dict, List
from calc_funcs.calc_funcs import *


@dataclass
class Command:
    '''Represents a command with a func and name'''
    name: str
    func: FunctionType
    
    def execute(self, *args) -> None:
        '''Execute command'''
        self.func(*args)


@dataclass
class CommandOptions:
    map: Dict[str, Command]
    
    def get_map(self) -> Dict[str, Command]:
        return self.map
    
    def get_command(self, choice) -> Command:
        return self.map.get(choice)

    
class Menu:
    command_options: CommandOptions

    def __init__(self, options: CommandOptions) -> None:
        self.command_options = options
    
    def show_menu(self, sep = ". ") -> None:
        menu = self.command_options.get_map()
        for choice, command in menu.items():
            print(choice, command.name, sep=sep)
    
    def run_command(self, choice: str) -> None:
        command = self.command_options.get_command(choice)
        command.execute()
    
    def read_choice_from_input(self, prompt):
        return input(prompt)
  

class File:
    data: str

    def load(self):
        file_name = input("File name: ")
        with open(file_name, "r") as f:
            self.data = f.readlines()
    
    def save(self):
        file_name = input("File name: ")
        with open(file_name, "w") as f:
            f.writelines()
            
    def get_data(self):
        return self.data
    
    def receive_data(self, data):
        self.data = data

class StatsCalc(Calc):
    
    @staticmethod
    def calc_stats(raw_data) -> None:
        arr = [int(stat) for stat in raw_data]
        stats = {
            "Min": int(min(arr)),
            "Max": int(max(arr)),
            "Mean": int(mean(arr)),
            "Median": int(median(arr))
        }

    @staticmethod        
    def get_stats_str(stats: Dict) -> str:
        s = ""
        for k, v in stats.items():
            s += f"{k:12} = {v}\n"
        return s   
    
    def display_stats(self, stats) -> None:
        print(self.get_stats_str())


class App:

    def __init__(self):
        self.file = File()
        self.stats = GradeStats
        command_options_map = {
            "1": Command("Load data.", self.file.load),
            "2": Command("Display computed stats.", GradeStats.display_stats),
            "3": Command("Save computed stats.", self.file.save),
            "4": Command("Exit.", self.exit),
        }
        self.menu = Menu(CommandOptions(command_options_map))
    
    def run(self):
        choice = 1
        while choice != 4:
            self.menu.show_menu()
            choice = self.menu.read_choice_from_input("Choice: ")
            self.menu.run_command(choice)

    def exit(self):
        print("Goodbye!")
        exit()


if __name__ == "__main__":
    App().run()

