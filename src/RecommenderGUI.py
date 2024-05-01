import tkinter as tk
from tkinter import ttk


class Recommender:
    def __init__(self):
        self._movies = []
        self._tvShows = []
        self._books = []
        self._movieStats = "No stats"
        self._tvStats = "No TV show statistics"
        self._bookStats = "No book statistics"

    def loadData(self):
        self._movies = [("Example Movie", 120), ("Example Movie", 120), ("Example Movie", 120)]
        self._tvShows = [("Example TV Show", 120), ("Example TV show", 120), ("Example TV show", 120)]
        self._books = [("Example Book", "Author A"), ("Example Book", "Author B")]
        self._movieStats = "no stats"
        self._tvStats = "no stats"
        self._bookStats = "Total Books: 2"

    def getMovies(self):
        if not self._movies:
            return "No data is loaded yet"

        maxTitleLength = max(len(title) for title, _ in self._movies)

        header = f"{'Title'.ljust(maxTitleLength + 4)}Runtime"
        movieTabFormat = [f"{title.ljust(maxTitleLength + 4)}{runtime} min" for title, runtime in self._movies]
        return header + "\n" + "\n".join(movieTabFormat)

    def getTVShows(self):
        if not self._tvShows:
            return "No data is loaded yet"

        maxTitleLength = max(len(title) for title, _ in self._tvShows)

        header = f"{'Title'.ljust(maxTitleLength + 4)}Runtime"
        tvTabFormat = [f"{title.ljust(maxTitleLength + 4)}{runtime} min" for title, runtime in self._tvShows]
        return header + "\n" + "\n".join(tvTabFormat)

    def getBooks(self):
        if not self._books:
            return "No book data loaded yet"
        maxTitleLength = max(len(title) for title, _ in self._books)
        header = f"{'Title'.ljust(maxTitleLength + 4)}Author"
        formatted_books = [f"{title.ljust(maxTitleLength + 4)}{author}" for title, author in self._books]
        return header + "\n" + "\n".join(formatted_books)


class RecommenderGUI:
    def __init__(self):
        self._recommender = Recommender()

        self._root = tk.Tk()
        self._root.title("Movie Recommender")
        self._root.geometry("1200x800")

        self._notebook = ttk.Notebook(self._root)
        self._notebook.pack(expand=True, fill="both")

        self._notebook_tab = ttk.Frame(self._notebook)
        self._notebook.add(self._notebook_tab, text="Movies")

        self._movieText = tk.Text(self._notebook_tab, height=10, wrap='word', state='disabled')
        self._movieText.pack(padx=10, pady=10, fill='both', expand=True)

        self._scrollbar = tk.Scrollbar(self._notebook_tab, command=self._movieText.yview)
        self._scrollbar.pack(side='right', fill='y')
        self._movieText.config(yscrollcommand=self._scrollbar.set)

        self._tv_shows_tab = ttk.Frame(self._notebook)
        self._notebook.add(self._tv_shows_tab, text="TV Shows")

        self._tvShowText = tk.Text(self._tv_shows_tab, height=10, wrap='word', state='disabled')
        self._tvShowText.pack(padx=10, pady=10, fill='both', expand=True)

        self._tv_scrollbar = tk.Scrollbar(self._tv_shows_tab, command=self._tvShowText.yview)
        self._tv_scrollbar.pack(side='right', fill='y')
        self._tvShowText.config(yscrollcommand=self._tv_scrollbar.set)

        self._booksTab = ttk.Frame(self._notebook)
        self._notebook.add(self._booksTab, text="Books")

        self._bookText = tk.Text(self._booksTab, height=10, wrap='word', state='disabled')
        self._bookText.pack(padx=10, pady=10, fill='both', expand=True)

        self._booksScrollbar = tk.Scrollbar(self._booksTab, command=self._bookText.yview)
        self._booksScrollbar.pack(side='right', fill='y')
        self._bookText.config(yscrollcommand=self._booksScrollbar.set)

        self._buttonFrame = tk.Frame(self._root)
        self._buttonFrame.pack(side='bottom', fill='x', padx=10, pady=10)

        self._buttons = []

        button = tk.Button(self._buttonFrame, text=f"Load Shows")
        button.pack(side='left', padx=10, expand=True)
        self._buttons.append(button)

        button = tk.Button(self._buttonFrame, text=f"Load Books")
        button.pack(side='left', padx=10, expand=True)
        self._buttons.append(button)

        button = tk.Button(self._buttonFrame, text=f"Load Recommendations")
        button.pack(side='left', padx=10, expand=True)
        self._buttons.append(button)

        button = tk.Button(self._buttonFrame, text=f"Information")
        button.pack(side='left', padx=10, expand=True)
        self._buttons.append(button)

        button = tk.Button(self._buttonFrame, text=f"Quit")
        button.pack(side='left', padx=10, expand=True)
        self._buttons.append(button)

        self._recommender.loadData()
        self.updateMovies()
        self.updateTVshows()
        self.updateBooks()

    def updateMovies(self):
        data = self._recommender.getMovies()
        self._movieText.config(state='normal')
        self._movieText.delete(1.0, tk.END)
        self._movieText.insert(tk.END, data)
        self._movieText.config(state='disabled')

    def updateTVshows(self):
        data = self._recommender.getTVShows()
        self._tvShowText.config(state='normal')
        self._tvShowText.delete(1.0, tk.END)
        self._tvShowText.insert(tk.END, data)
        self._tvShowText.config(state='disabled')

    def updateBooks(self):
        data = self._recommender.getBooks()
        self._bookText.config(state='normal')
        self._bookText.delete(1.0, tk.END)
        self._bookText.insert(tk.END, data)
        self._bookText.config(state='disabled')

    @property
    def root(self):
        return self._root


if __name__ == "__main__":
    gui = RecommenderGUI()
    gui.root.mainloop()
