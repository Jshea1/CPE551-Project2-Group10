# Author:
# Date: 5-5-2024
# Description:
# I pledge my honor that I have abided by the Stevens Honor System


import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Recommender import Recommender
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class RecommenderGUI:
    def __init__(self):
        self._recommender = Recommender()

        self._rootWindow = tk.Tk()
        self._rootWindow.title("Movie Recommender")
        self._rootWindow.geometry("1200x800")
        # self._rootWindow.resizable(False, False)

        self._notebook = ttk.Notebook(self._rootWindow)
        self._notebook.pack(expand=True, fill="both")

        # Movies tab begins

        self._moviesTab = ttk.Frame(self._notebook)
        self._notebook.add(self._moviesTab, text="Movies")

        self._movieTitleText = tk.Text(self._moviesTab, height=10, wrap='word', state='disabled')
        self._movieTitleText.pack(padx=10, pady=10, fill='both', expand=True)

        self._movieStatsText = tk.Text(self._moviesTab, height=10, wrap='word', state='disabled')
        self._movieStatsText.pack(padx=10, pady=10, fill='both', expand=True)

        # Movies tab ends

        # TV tab begins

        self._tvTab = ttk.Frame(self._notebook)
        self._notebook.add(self._tvTab, text="TV Shows")

        self._tvShowTitleText = tk.Text(self._tvTab, height=10, wrap='word', state='disabled')
        self._tvShowTitleText.pack(padx=10, pady=10, fill='both', expand=True)

        self._tvShowStatsText = tk.Text(self._tvTab, height=10, wrap='word', state='disabled')
        self._tvShowStatsText.pack(padx=10, pady=10, fill='both', expand=True)

        self._tvScrollbar = tk.Scrollbar(self._tvTab, command=self._tvShowTitleText.yview)
        self._tvScrollbar.pack(side='right', fill='y')
        self._tvShowTitleText.config(yscrollcommand=self._tvScrollbar.set)

        # TV tab ends

        # Books tab begins

        self._booksTab = ttk.Frame(self._notebook)
        self._notebook.add(self._booksTab, text="Books")

        self._bookTitleText = tk.Text(self._booksTab, height=10, wrap='word', state='disabled')
        self._bookTitleText.pack(padx=10, pady=10, fill='both', expand=True)

        self._bookStatsText = tk.Text(self._booksTab, height=10, wrap='word', state='disabled')
        self._bookStatsText.pack(padx=10, pady=10, fill='both', expand=True)

        self._booksScrollbar = tk.Scrollbar(self._booksTab, command=self._bookTitleText.yview)
        self._booksScrollbar.pack(side='right', fill='y')
        self._bookTitleText.config(yscrollcommand=self._booksScrollbar.set)

        # Books tab ends

        # Search Movies/TV tab begins

        self._searchMoviesTab = ttk.Frame(self._notebook)
        self._notebook.add(self._searchMoviesTab, text="Search Movies/TV")

        self._TypeLabel = ttk.Label(self._searchMoviesTab, text="Type:")
        self._TypeLabel.grid(row=0, column=0, padx=10, pady=5, sticky='w')
        self._typeCombobox = ttk.Combobox(self._searchMoviesTab, values=["Movie", "TV Show"])
        self._typeCombobox.grid(row=0, column=1, padx=0, pady=10,sticky='w')
        self._typeCombobox.set("Movie")  # showing movie as default

        self._titleLabel = ttk.Label(self._searchMoviesTab, text="Title:")
        self._titleLabel.grid(row=1, column=0, padx=10, pady=5, sticky='w')
        self._MtitleEntry = ttk.Entry(self._searchMoviesTab, width=50)
        self._MtitleEntry.grid(row=1, column=1, padx=0, pady=5, sticky='w')

        self._directorLabel = ttk.Label(self._searchMoviesTab, text="Director:")
        self._directorLabel.grid(row=2, column=0, padx=10, pady=5, sticky='w')
        self._directorEntry = ttk.Entry(self._searchMoviesTab, width=50)
        self._directorEntry.grid(row=2, column=1, padx=0, pady=5, sticky='w')

        self._actorLabel = ttk.Label(self._searchMoviesTab, text="Actor:")
        self._actorLabel.grid(row=3, column=0, padx=10, pady=5, sticky='w')
        self._actorEntry = ttk.Entry(self._searchMoviesTab, width=50)
        self._actorEntry.grid(row=3, column=1, padx=0, pady=5, sticky='w')

        self._genreLabel = ttk.Label(self._searchMoviesTab, text="Genre:")
        self._genreLabel.grid(row=4, column=0, padx=10, pady=5, sticky='w')
        self._genreEntry = ttk.Entry(self._searchMoviesTab, width=50)
        self._genreEntry.grid(row=4, column=1, padx=0, pady=5, sticky='w')

        self._searchButton = ttk.Button(self._searchMoviesTab, text="Search", command=self.searchShows)
        self._searchButton.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky='w')

        self._MtextResults = tk.Text(self._searchMoviesTab, height=30, wrap='none', state='disabled', width=148)
        self._MtextResults.grid(row=6, column=0, columnspan=150, padx=5, pady=10, sticky='ew')

        self._MresultsScrollbar = ttk.Scrollbar(self._searchMoviesTab, command=self._MtextResults.yview)
        self._MresultsScrollbar.grid(row=6, column=149, sticky='ns')
        self._MtextResults.config(yscrollcommand=self._MresultsScrollbar.set)
        
        self._vscroll = ttk.Scrollbar(self._searchMoviesTab, orient='horizontal', command=self._MtextResults.xview)
        self._vscroll.grid(row=7, column=0, columnspan=150, sticky='ew')
        self._MtextResults.config(xscrollcommand=self._vscroll.set)

        # Search Movies/TV tab ends

        # Search books tab begins

        self._searchBooksTab = ttk.Frame(self._notebook)
        self._notebook.add(self._searchBooksTab, text="Search Books")

        self._titleLabel = ttk.Label(self._searchBooksTab, text="Title:")
        self._titleLabel.grid(row=1, column=0, padx=10, pady=5)
        self._titleEntry = ttk.Entry(self._searchBooksTab)
        self._titleEntry.grid(row=1, column=1, padx=10, pady=5)

        self._directorLabel = ttk.Label(self._searchBooksTab, text="Author:")
        self._directorLabel.grid(row=2, column=0, padx=10, pady=5)
        self._AuthorEntry = ttk.Entry(self._searchBooksTab)
        self._AuthorEntry.grid(row=2, column=1, padx=10, pady=5)

        self._actorLabel = ttk.Label(self._searchBooksTab, text="Publisher:")
        self._actorLabel.grid(row=3, column=0, padx=10, pady=5)
        self._PublisherEntry = ttk.Entry(self._searchBooksTab)
        self._PublisherEntry.grid(row=3, column=1, padx=10, pady=5)

        self._searchButton = ttk.Button(self._searchBooksTab, text="Search", command=self.searchBooks)
        self._searchButton.grid(row=5, column=0, columnspan=2, pady=10)

        self._BtextResults = tk.Text(self._searchBooksTab, height=30, wrap='word', state='disabled',width=148)
        self._BtextResults.grid(row=6, column=0, columnspan=150, padx=5, pady=10,sticky='ew')

        self._resultsScrollbar = ttk.Scrollbar(self._searchBooksTab, command=self._BtextResults.yview)
        self._resultsScrollbar.grid(row=6, column=149, sticky='ns')
        self._BtextResults.config(yscrollcommand=self._resultsScrollbar.set)
        
        self._vscroll = ttk.Scrollbar(self._searchBooksTab, orient='horizontal', command=self._BtextResults.xview)
        self._vscroll.grid(row=7, column=0, columnspan=150, sticky='ew')
        self._BtextResults.config(xscrollcommand=self._vscroll.set)        

        # Search books tab ends

        # Recommendations tab begins

        self._recommendationsTab = ttk.Frame(self._notebook)
        self._notebook.add(self._recommendationsTab, text="Recommendations")

        self._TypeLabel = ttk.Label(self._recommendationsTab, text="Type:")
        self._TypeLabel.grid(row=0, column=0, padx=0, pady=5)
        self._typeCombobox = ttk.Combobox(self._recommendationsTab, values=["Movie", "TV Show", "Book"])
        self._typeCombobox.grid(row=0, column=1, padx=0, pady=10)
        self._typeCombobox.set("Movie")  # showing movie as default

        self._directorLabel = ttk.Label(self._recommendationsTab, text="Title:")
        self._directorLabel.grid(row=2, column=0, padx=10, pady=5)
        self._RtitleEntry = ttk.Entry(self._recommendationsTab)
        self._RtitleEntry.grid(row=2, column=1, padx=10, pady=5)

        self._searchButton = ttk.Button(self._recommendationsTab, text="Get recommendation",
                                        command=self.getRecommendations)
        self._searchButton.grid(row=5, column=0, columnspan=2, pady=10)

        self._RtextResults = tk.Text(self._recommendationsTab, height=30, wrap='word', state='disabled',width=148)
        self._RtextResults.grid(row=6, column=0, columnspan=150, padx=5, pady=10,sticky='ew')

        self._resultsScrollbar = ttk.Scrollbar(self._recommendationsTab, command=self._RtextResults.yview)
        self._resultsScrollbar.grid(row=6, column=150, sticky='ns')
        self._RtextResults.config(yscrollcommand=self._resultsScrollbar.set)
        
        self._vscroll = ttk.Scrollbar(self._recommendationsTab, orient='horizontal', command=self._RtextResults.xview)
        self._vscroll.grid(row=7, column=0, columnspan=150, sticky='ew')
        self._RtextResults.config(xscrollcommand=self._vscroll.set)

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

        # Bonus tab begins

        self._BonusTab = ttk.Frame(self._notebook)
        self._notebook.add(self._BonusTab, text="Ratings")
        self._nestedbonusFrame = ttk.Frame(self._BonusTab, width=200, height=100, relief="solid")
        self._nestedbonusFrame.pack(side='top',pady=20, padx=20)
        # # Bonus code
        # bonusButton = tk.Button(self._BonusTab, text="Bonus Button", command=self.bonusButtonFunc)
        # bonusButton.grid(row=0, column=0, padx=10, pady=10, sticky='w')
        # bonusButton.pack(padx=10, pady=10, side='top')

        # Bonus tab ends
    def bonusButtonFunc(self):
        # Check if there is already a canvas, and remove it if it exists
        if hasattr(self, "_canvas"):
            self._canvas.get_tk_widget().pack_forget()
            self._canvas.get_tk_widget().destroy()

        moviesList = self._recommender.getMovies()
        movRatingDict = {}
        tvList = self._recommender.getTVShows()
        tvRatingDict = {}

        for movie in moviesList.values():
            if movie.getRating() not in movRatingDict:
                movRatingDict[movie.getRating()] = 1
            else:
                movRatingDict[movie.getRating()] += 1

        for tv in tvList.values():
            if tv.getRating() not in tvRatingDict:
                tvRatingDict[tv.getRating()] = 1
            else:
                tvRatingDict[tv.getRating()] += 1

        fig, ax = plt.subplots(1, 2, figsize=(15, 5))

        ax[0].pie(movRatingDict.values(), labels=movRatingDict.keys(), autopct='%1.2f%%')
        ax[0].set_title("Movie Ratings")
        # ax[0].legend(loc='upper left', fontsize='10')

        ax[1].pie(tvRatingDict.values(), labels=tvRatingDict.keys(), autopct='%1.2f%%')
        ax[1].set_title("TV Show Ratings")
        # ax[1].legend(loc='upper right', fontsize=10)
        fig.tight_layout()

        self._canvas = FigureCanvasTkAgg(fig, master=self._nestedbonusFrame)
        self._canvas.draw()
        self._canvas.get_tk_widget().pack(padx=10, pady=10, expand=True, fill='both', side='top')

            
        
        
    def loadShows(self):
        self._recommender.loadShows()

        moviesList = self._recommender.getMovieList()
        moviesStats = self._recommender.getMovieStats()

        tvList = self._recommender.getTVList()
        tvStats = self._recommender.getTVStats()

        self._movieTitleText.config(state='normal')
        self._movieTitleText.delete(1.0, tk.END)
        self._movieTitleText.insert(tk.END, moviesList)
        self._movieTitleText.config(state='disabled')

        self._movieStatsText.config(state='normal')
        self._movieStatsText.delete(1.0, tk.END)
        self._movieStatsText.insert(tk.END, moviesStats)
        self._movieStatsText.config(state='disabled')

        self._tvShowTitleText.config(state='normal')
        self._tvShowTitleText.delete(1.0, tk.END)
        self._tvShowTitleText.insert(tk.END, tvList)
        self._tvShowTitleText.config(state='disabled')

        self._tvShowStatsText.config(state='normal')
        self._tvShowStatsText.delete(1.0, tk.END)
        self._tvShowStatsText.insert(tk.END, tvStats)
        self._tvShowStatsText.config(state='disabled')
        self.bonusButtonFunc()

    def loadBooks(self):
        self._recommender.loadBooks()

        booksList = self._recommender.getBookList()
        booksStats = self._recommender.getBookStats()

        self._bookTitleText.config(state='normal')
        self._bookTitleText.delete(1.0, tk.END)
        self._bookTitleText.insert(tk.END, booksList)
        self._bookTitleText.config(state='disabled')

        self._bookStatsText.config(state='normal')
        self._bookStatsText.delete(1.0, tk.END)
        self._bookStatsText.insert(tk.END, booksStats)
        self._bookStatsText.config(state='disabled')

    def loadAssociations(self):
        self._recommender.loadAssociations()

    def creditInfoBox(self):
        messagebox.showinfo("Information", "Saurabh Raman Parkar     Yash Patel     John Shea\n"
                                           "Project completed on May-05-2024")

    def searchShows(self):
        choiceType = self._typeCombobox.get()
        title = self._MtitleEntry.get()
        director = self._directorEntry.get()
        actor = self._actorEntry.get()
        genre = self._genreEntry.get()
        print(choiceType, title, director, actor, genre)
        if choiceType == "Movie":
            results = self._recommender.searchTVMovies(title=title, director=director, cast=actor, genre=genre)
        elif choiceType == "TV Show":
            results = self._recommender.searchTVMovies(title=title, director=director, cast=actor, genre=genre)

        # not sure if combobox options should be separated like this

        self._MtextResults.config(state='normal')
        self._MtextResults.delete(1.0, tk.END)

        maxtitlelength = len('Title') + 1
        maxdirectorlength = len('Director') + 1
        maxactorlength = len('Cast') + 1

        if results:
            for result in results:
                # self._textResults.insert(tk.END, f"{result}\n")
                if len(result.getTitle()) > maxtitlelength:
                    maxtitlelength = len(result.getTitle())
                if len(result.getDirectors()) > maxdirectorlength:
                    maxdirectorlength = len(result.getDirectors())
                if len(result.getCast()) > maxactorlength:
                    maxactorlength = len(result.getCast())
            self._MtextResults.insert(tk.END,
                                      f"{'Title':<{maxtitlelength}} {'Director':<{maxdirectorlength}} {'Cast':<{maxactorlength}} Genre\n")
            for result in results:
                self._MtextResults.insert(tk.END,
                                          f"{result.getTitle():<{maxtitlelength}} {result.getDirectors():<{maxdirectorlength}} {result.getCast():<{maxactorlength}} {result.getGenres()}\n")
            self._MtextResults.config(state='disabled')

    def searchBooks(self):
        title = self._titleEntry.get()
        author = self._AuthorEntry.get()
        publisher = self._PublisherEntry.get()
        print(title, author, publisher)
        results = self._recommender.searchBooks(title=title, author=author, publisher=publisher)
        self._BtextResults.config(state='normal')
        self._BtextResults.delete(1.0, tk.END)

        maxtitlelength = len('Title') + 1
        maxauthorlength = len('Author') + 1

        if results:
            for result in results:
                if len(result.getTitle()) > maxtitlelength:
                    maxtitlelength = len(result.getTitle())
                if len(result.getAuthor()) > maxauthorlength:
                    maxauthorlength = len(result.getAuthor())

            self._BtextResults.insert(tk.END, f"{'Title':<{maxtitlelength}} {'Author':<{maxauthorlength}} Publisher\n")
            for result in results:
                self._BtextResults.insert(tk.END,
                                          f"{result.getTitle():<{maxtitlelength}} {result.getAuthor():<{maxauthorlength}} {result.getPublisher()}\n")

            self._BtextResults.config(state='disabled')

    def getRecommendations(self):
        recommendationType = self._typeCombobox.get()
        title = self._titleEntry.get()
        recommendations = self._recommender.getRecommendations(recommendationType, title)
        self._RtextResults.config(state='normal')
        self._RtextResults.delete(1.0, tk.END)

        if recommendations:
            for recommendation in recommendations:
                self._RtextResults.insert(tk.END, f"{recommendation}\n")

        self._RtextResults.config(state='disabled')

    def rootWindow(self):
        return self._rootWindow


if __name__ == "__main__":
    gui = RecommenderGUI()
    gui.rootWindow().mainloop()
