from tkinter import *
master = Tk()


master.title("My App!")
master.configure(bg='#1E1E1E')
master.geometry("1000x1000")


def lcsFN():
    l1 = StringEntry1.get()
    l2 = StringEntry2.get()
    len1 = len(l1)
    len2 = len(l2)

    dp_tbl_value = [[" " for x in range(len2)] for x in range(len1)]
    for i in range(len1):
        for j in range(len2):
            if l1[i] == l2[j]:
                if i == 0 or j == 0:
                    dp_tbl_value[i][j] = l1[i]
                else:
                    dp_tbl_value[i][j] = dp_tbl_value[i-1][j-1] + l1[i]
            else:
                dp_tbl_value[i][j] = max(
                    dp_tbl_value[i-1][j], dp_tbl_value[i][j-1])
    cs = dp_tbl_value[-1][-1]
    LabelString3 = Label(master, text="LCS IS : "+cs, fg='White',
                         bg='#C3602C', font=('Franklin Gothic Book (Body)', 25)).grid(row=12, column=1)


Title = Label(master, text="Longest Common Subsequence", fg='White',
              bg='#CCDDEA', font=('Algerian', 25))

LabelString1 = Label(master, text="String 1", fg='White', width=12,
                     bg='#C3602C', font=('Castellar', 15))

LabelString2 = Label(master, text="String 2", fg='White', width=12,
                     bg='#C3602C', font=('Castellar', 15))

StringEntry1 = Entry(master, width=30, font=('Franklin', 15))
StringEntry2 = Entry(master, width=30, font=('Franklin', 15))

my_button = Button(master, text="Find The LCS", bg='#C3602C', height=2, font=("Franklin", 12),
                   fg='white', width=40, command=lcsFN)
my_button.grid(row=10, column=1, pady=20)


Title.grid(row=0, column=1, sticky=W, pady=20)
LabelString1.grid(row=2, column=0, pady=20, padx=20)
LabelString2.grid(row=3, column=0, pady=20, padx=20)
StringEntry1.grid(row=2, column=1)
StringEntry2.grid(row=3, column=1)


master.mainloop()
