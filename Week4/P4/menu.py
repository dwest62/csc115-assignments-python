from dataclasses import dataclass
from types import FunctionType
from typing import Dict

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
        return self.map.get(choice, False)
        
class Menu:
    command_options: CommandOptions

    def __init__(self, options: CommandOptions) -> None:
        self.command_options = options
    
    def run(self):
        while True:
            self.show_menu()
            choice = self.read_choice("Choice: ")
            print("")
            self.run_command(choice)

    def show_menu(self, sep = ". ") -> None:
        print("Choose an option.")
        menu = self.command_options.get_map()
        for choice, command in menu.items():
            print(choice, command.name, sep=sep)
    
    def run_command(self, choice: str) -> None:
        command = self.command_options.get_command(choice)
        if command == False:
            print(f"Invalid command {choice}.")
        else:
            command.execute()
    
    def read_choice(self, prompt):
        return input(prompt)