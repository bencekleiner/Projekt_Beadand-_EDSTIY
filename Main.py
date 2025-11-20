import tkinter as tk
from autokatalogus_KB import AppKB

def main():
    root = tk.Tk()
    app = AppKB(root)
    root.mainloop()

if __name__ == "__main__":
    main()