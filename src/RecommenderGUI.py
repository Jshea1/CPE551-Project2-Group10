import tkinter as tk
from tkinter import ttk
from Recommender import Recommender

class RecommenderGUI():
    def __init__(self):
        self.Recommender = Recommender()

        self.window=tk.Tk()
        self.window.title("title") # change name
        self.window.geometry("1200x800")

        self.tab_control = ttk.Notebook(self.window)

        self.notebook = ttk.Notebook(self.window)
        self.notebook.pack(expand=True, fill='both')
        
        self.setup_movies_tab()
        self.setup_tv_shows_tab()
        self.setup_books_tab()
        self.setup_search_tab()
        self.setup_recommendations_tab()







    


