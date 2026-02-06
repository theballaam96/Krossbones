import tkinter as tk

class KrossbonesLib:
    def log_debug(self, message: str):
        """Log debug message."""
        if self.debug_output:
            self.debug_output.insert(tk.END, f"{message}\n")
            self.debug_output.see(tk.END)
        # print(message)