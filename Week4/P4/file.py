class File:
    data: list = []

    def load(self, file_name: str):
        with open(file_name, "r") as f:
            self.data = f.read().splitlines()
        print("Data read successfully\n")
    
    def save(self, file_name):
        with open(file_name, "w") as f:
            f.write(self.data)
            
    def get_data(self):
        return self.data
    
    def receive_data(self, data):
        self.data = data

class PromptFile(File):
    def prompt_load(self):
        try:
            file_name = self._prompt_file_name()
            self.load(file_name)
        except:
            self._handle_load_err(file_name)
    
    def prompt_save(self):
        try:
            fname = self._prompt_file_name()
            self.save(fname)
            print("Result saved successful.\n")
        except:
            self._handle_save_err(fname)
    
    def _prompt_file_name(self):
        file_name = input("Enter the name of the file: ")
        return file_name

    def _handle_save_err(self, file_name):
        err_msg = f"Error saving file {file_name}."
        print(err_msg)
        try_again = self._prompt_try_again()
        if try_again:
            self.prompt_save()

    def _handle_load_err(self, file_name):
        err_msg = f"Error loading file {file_name}."
        if len(self.data) == 0:
            print(err_msg)
            self.prompt_load()
        else:
            print(err_msg)
            try_again = self._prompt_try_again()
            if try_again:
                self.prompt_load()
    
    def _prompt_try_again(self) -> str:
        read = lambda: input("(y/n) Would you like to try again? ")
        try_again = read()
        while try_again not in ["Y", "y", "N", "n"]:
            print(f"Invalid input, enter y or n. You entered {try_again}.")
            try_again = read()
        return try_again in ["Y", "y"]
