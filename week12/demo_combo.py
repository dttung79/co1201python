from tkinter import *
from tkinter.ttk import Combobox

movies_dict = {'The Matrix': ['Lana Wachowski, Lilly Wachowski', 'Keanu Reeves, Laurence Fishburne, Carrie-Anne Moss'], \
                'The Lord of the Rings': ['Peter Jackson', 'Elijah Wood, Ian McKellen, Orlando Bloom'], \
                'The Dark Knight': ['Christopher Nolan', 'Christian Bale, Heath Ledger, Aaron Eckhart'], \
                'Inception': ['Christopher Nolan', 'Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page'], \
                'Interstellar': ['Christopher Nolan', 'Matthew McConaughey, Anne Hathaway, Jessica Chastain']}
                

### EVENT HANDLERS ###

### CREATE WINDOW ###
window = Tk()
window.title('Demo Combobox')
window.geometry('400x300')

### CREATE WIDGETS ###
lbl_title = Label(window, text='Select your favourite movie:')
lbl_title.grid(row=0, column=0, columnspan=2, sticky=W)

movie_list = ['The Matrix', 'The Lord of the Rings', 'The Dark Knight', 'Inception', \
                'Interstellar']
cbb_movies = Combobox(window, values=movie_list)
cbb_movies.grid(row=1, column=0, columnspan=2, sticky=W)

lbl_info = Label(window, text='Movie info: ')
lbl_info.grid(row=2, column=0, sticky=W)

lbl_director = Label(window, text='Director: ')
lbl_director.grid(row=3, column=0, columnspan=2, sticky=W)

lbl_actors = Label(window, text='Actors: ')
lbl_actors.grid(row=4, column=0, columnspan=2, sticky=W)

### START THE GUI ###
window.mainloop()