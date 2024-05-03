# Author:
# Date: 5-5-2024
# Description:
# I pledge my honor that I have abided by the Stevens Honor System


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Recommender import Recommender
class RecommenderGUI:
    def __init__(self):
        self._recommender = Recommender()

        self._rootWindow = tk.Tk()
        self._rootWindow.title("Movie Recommender")
        self._rootWindow.geometry("1200x800")

        self._notebook = ttk.Notebook(self._rootWindow)
        self._notebook.pack(expand=True, fill="both")

        # Movies tab begins

        self._moviesTab = ttk.Frame(self._notebook)
        self._notebook.add(self._moviesTab, text="Movies")

        self._movieText = tk.Text(self._moviesTab, height=10, wrap='word', state='disabled')
        self._movieText.pack(padx=10, pady=10, fill='both', expand=True)

        self._scrollbar = tk.Scrollbar(self._moviesTab, command=self._movieText.yview)
        self._scrollbar.pack(side='right', fill='y')
        self._movieText.config(yscrollcommand=self._scrollbar.set)

        # Movies tab ends

        # TV tab begins

        self._tvTab = ttk.Frame(self._notebook)
        self._notebook.add(self._tvTab, text="TV Shows")

        self._tvShowText = tk.Text(self._tvTab, height=10, wrap='word', state='disabled')
        self._tvShowText.pack(padx=10, pady=10, fill='both', expand=True)

        self._tvScrollbar = tk.Scrollbar(self._tvTab, command=self._tvShowText.yview)
        self._tvScrollbar.pack(side='right', fill='y')
        self._tvShowText.config(yscrollcommand=self._tvScrollbar.set)

        # TV tab ends

        # Books tab begins

        self._booksTab = ttk.Frame(self._notebook)
        self._notebook.add(self._booksTab, text="Books")

        self._bookText = tk.Text(self._booksTab, height=10, wrap='word', state='disabled')
        self._bookText.pack(padx=10, pady=10, fill='both', expand=True)

        self._booksScrollbar = tk.Scrollbar(self._booksTab, command=self._bookText.yview)
        self._booksScrollbar.pack(side='right', fill='y')
        self._bookText.config(yscrollcommand=self._booksScrollbar.set)

        # Books tab ends

        # Search Movies/TV tab begins

        self._searchMoviesTab = ttk.Frame(self._notebook)
        self._notebook.add(self._searchMoviesTab, text="Search Movies/TV")

        self._TypeLabel = ttk.Label(self._searchMoviesTab, text="Type:")
        self._TypeLabel.grid(row=0, column=0, padx=0, pady=5)
        self._typeCombobox = ttk.Combobox(self._searchMoviesTab, values=["Movie", "TV Show"])
        self._typeCombobox.grid(row=0, column=1, padx=0, pady=10)
        self._typeCombobox.set("Movie")  # Default value

        self._titleLabel = ttk.Label(self._searchMoviesTab, text="Title:")
        self._titleLabel.grid(row=1, column=0, padx=10, pady=5)
        self._titleEntry = ttk.Entry(self._searchMoviesTab)
        self._titleEntry.grid(row=1, column=1, padx=10, pady=5)

        self._directorLabel = ttk.Label(self._searchMoviesTab, text="Director:")
        self._directorLabel.grid(row=2, column=0, padx=10, pady=5)
        self._directorEntry = ttk.Entry(self._searchMoviesTab)
        self._directorEntry.grid(row=2, column=1, padx=10, pady=5)

        self._actorLabel = ttk.Label(self._searchMoviesTab, text="Actor:")
        self._actorLabel.grid(row=3, column=0, padx=10, pady=5)
        self._actorEntry = ttk.Entry(self._searchMoviesTab)
        self._actorEntry.grid(row=3, column=1, padx=10, pady=5)

        self._genreLabel = ttk.Label(self._searchMoviesTab, text="Genre:")
        self._genreLabel.grid(row=4, column=0, padx=10, pady=5)
        self._genreEntry = ttk.Entry(self._searchMoviesTab)
        self._genreEntry.grid(row=4, column=1, padx=10, pady=5)

        self._searchButton = ttk.Button(self._searchMoviesTab, text="Search")
        self._searchButton.grid(row=5, column=0, columnspan=2, pady=10)

        self._textResults = tk.Text(self._searchMoviesTab, height=30, wrap='word', state='disabled')
        self._textResults.grid(row=6, column=0, columnspan=15, padx=5, pady=10)

        self._resultsScrollbar = ttk.Scrollbar(self._searchMoviesTab, command=self._textResults.yview)
        self._resultsScrollbar.grid(row=6, column=15)
        self._textResults.config(yscrollcommand=self._resultsScrollbar.set)

        # Search Movies/TV tab begins

        # Search books tab begins

        self._searchBooksTab = ttk.Frame(self._notebook)
        self._notebook.add(self._searchBooksTab, text="Search Books")

        self._titleLabel = ttk.Label(self._searchBooksTab, text="Title:")
        self._titleLabel.grid(row=1, column=0, padx=10, pady=5)
        self._titleEntry = ttk.Entry(self._searchBooksTab)
        self._titleEntry.grid(row=1, column=1, padx=10, pady=5)

        self._directorLabel = ttk.Label(self._searchBooksTab, text="Author:")
        self._directorLabel.grid(row=2, column=0, padx=10, pady=5)
        self._directorEntry = ttk.Entry(self._searchBooksTab)
        self._directorEntry.grid(row=2, column=1, padx=10, pady=5)

        self._actorLabel = ttk.Label(self._searchBooksTab, text="Publisher:")
        self._actorLabel.grid(row=3, column=0, padx=10, pady=5)
        self._actorEntry = ttk.Entry(self._searchBooksTab)
        self._actorEntry.grid(row=3, column=1, padx=10, pady=5)

        self._searchButton = ttk.Button(self._searchBooksTab, text="Search")
        self._searchButton.grid(row=5, column=0, columnspan=2, pady=10)

        self._textResults = tk.Text(self._searchBooksTab, height=30, wrap='word', state='disabled')
        self._textResults.grid(row=6, column=0, columnspan=15, padx=5, pady=10)

        self._resultsScrollbar = ttk.Scrollbar(self._searchBooksTab, command=self._textResults.yview)
        self._resultsScrollbar.grid(row=6, column=15)
        self._textResults.config(yscrollcommand=self._resultsScrollbar.set)

        # Search books tab ends

        # Recommendations tab begins

        self._recommendationsTab = ttk.Frame(self._notebook)
        self._notebook.add(self._recommendationsTab, text="Recommendations")

        self._titleLabel = ttk.Label(self._recommendationsTab, text="Type:")
        self._titleLabel.grid(row=1, column=0, padx=10, pady=5)
        self._titleEntry = ttk.Entry(self._recommendationsTab)
        self._titleEntry.grid(row=1, column=1, padx=10, pady=5)

        self._directorLabel = ttk.Label(self._recommendationsTab, text="Title:")
        self._directorLabel.grid(row=2, column=0, padx=10, pady=5)
        self._directorEntry = ttk.Entry(self._recommendationsTab)
        self._directorEntry.grid(row=2, column=1, padx=10, pady=5)

        self._searchButton = ttk.Button(self._recommendationsTab, text="Get recommendation")
        self._searchButton.grid(row=5, column=0, columnspan=2, pady=10)

        self._textResults = tk.Text(self._recommendationsTab, height=30, wrap='word', state='disabled')
        self._textResults.grid(row=6, column=0, columnspan=15, padx=5, pady=10)

        self._resultsScrollbar = ttk.Scrollbar(self._recommendationsTab, command=self._textResults.yview)
        self._resultsScrollbar.grid(row=6, column=15)
        self._textResults.config(yscrollcommand=self._resultsScrollbar.set)

        # Recommendations tab ends

        # Bottom button code begins

        self._buttonFrame = tk.Frame(self._rootWindow)
        self._buttonFrame.pack(side='bottom', fill='x', padx=10, pady=10)

        self._buttons = []

        button = tk.Button(self._buttonFrame, text=f"Load Shows", command=self.loadShows)
        button.pack(side='left', padx=10, expand=True)
        self._buttons.append(button)

        button = tk.Button(self._buttonFrame, text=f"Load Books", command=self.loadBooks)
        button.pack(side='left', padx=10, expand=True)
        self._buttons.append(button)

        button = tk.Button(self._buttonFrame, text=f"Load Recommendations", command=self.loadAssociations)
        button.pack(side='left', padx=10, expand=True)
        self._buttons.append(button)

        button = tk.Button(self._buttonFrame, text=f"Information", command=self.creditInfoBox)
        button.pack(side='left', padx=10, expand=True)
        self._buttons.append(button)

        button = tk.Button(self._buttonFrame, text=f"Quit", command=self._rootWindow.destroy)
        button.pack(side='left', padx=10, expand=True)
        self._buttons.append(button)

    def loadShows(self):
        self._recommender.loadShows()

        moviesList = self._recommender.getMovieList()
        moviesStats = self._recommender.getMovieStats()

        tvList = self._recommender.getTVList()
        tvStats = self._recommender.getTVStats()

        self._movieText.config(state='normal')
        self._movieText.delete(1.0, tk.END)
        self._movieText.insert(tk.END, moviesList + "\n" + moviesStats)
        self._movieText.config(state='disabled')

        self._tvShowText.config(state='normal')
        self._tvShowText.delete(1.0, tk.END)
        self._tvShowText.insert(tk.END, tvList + "\n" + tvStats)
        self._tvShowText.config(state='disabled')

    def loadBooks(self):
        self._recommender.loadBooks()

        booksList = self._recommender.getBookList()
        booksStats = self._recommender.getBookStats()

        self._bookText.config(state='normal')
        self._bookText.delete(1.0, tk.END)
        self._bookText.insert(tk.END, booksList + "\n" + booksStats)
        self._bookText.config(state='disabled')

    def loadAssociations(self):
        self._recommender.loadAssociations()

    def creditInfoBox(self):
        messagebox.showinfo("Information", "Saurabh Raman Parkar     Yash Patel     John Shea\n"
                                           "Project completed on May-05-2024")



    @property
    def rootWindow(self):
        return self._rootWindow


if __name__ == "__main__":
    gui = RecommenderGUI()
    gui.rootWindow.mainloop()