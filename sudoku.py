import tkinter

root = tkinter.Tk()
root.geometry("700x350")
root.title("Sudoku Solver")

def solve_sudoku():
    #firt step: find the next not filled area --> find_next_area()
    #when found a not filled area try possibble values and check is it valid ---> is_valid(sudoku,guess,row,column)
    #if is_valid() returns True we solved the sudoku. Otherwise we need to call function recursively. If none of the tries worked this means that SUDOKU IS UNSOLVEABLE.

    pass

entries = []

# create entry areas for each number
for y in range(9):
    for x in range(9):
        entry = tkinter.Entry(root, width=1)
        entry.grid(row=y, column=x, padx=10, pady=10)
        entries.append(entry)

btn_solve = tkinter.Button(root, text="SOLVE", command=solve_sudoku)
btn_solve.grid(row=5, column=10)

# I tried to create and to locate entry areas manually but I give up .d
"""
txt_1 = tkinter.Entry(root, width=1)
txt_2 = tkinter.Entry(root, width=1)
txt_3 = tkinter.Entry(root, width=1)
txt_4 = tkinter.Entry(root, width=1)
txt_5 = tkinter.Entry(root, width=1)
txt_6 = tkinter.Entry(root, width=1)
txt_7 = tkinter.Entry(root, width=1)
txt_8 = tkinter.Entry(root, width=1)
txt_9 = tkinter.Entry(root, width=1)

txt_1.grid(row=0, column=0, padx=10)
txt_2.grid(row=0, column=1, padx=10)
txt_3.grid(row=0, column=2, padx=10)
txt_4.grid(row=1, column=0, padx=10)
txt_5.grid(row=1, column=1, padx=10)
txt_6.grid(row=1, column=2, padx=10)
txt_7.grid(row=2, column=0, padx=10)
txt_8.grid(row=2, column=1, padx=10)
txt_9.grid(row=2, column=2, padx=10)
"""

root.mainloop()
