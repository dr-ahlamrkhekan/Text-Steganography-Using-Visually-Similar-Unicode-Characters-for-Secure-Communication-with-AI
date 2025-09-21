import tkinter as security    # to open the tkinter library
from tkinter import filedialog #     newwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww
root = security.Tk()          # make the root






def path_pln():

    file_path1 = filedialog.askopenfile(initialdir='/',title='select file',filetypes=(('text files','.txt'),('all files','*.*')))
    print (file_path1)


# def path_cover():
#     root.withdraw()
#     file_path2 = filedialog.askopenfilename()
#     root.pak()    in_binary = (''.join(format(ord(x), 'b').zfill(8) for x in x3))  # to convert the character to binary (8) digit

    first_eliment = 0   # make the first counter equal 0
    second_eliment = 2  # make the second counter equal 2 'take two digit'
    Bashkir = ''        # string to storage convert value from binary to bashkir language

    count = len(in_binary) # to storage the length of secrete message in binary

    for digit in range(count): # loop from digit=0 to length of secrete message in binary
        eliment = (in_binary[first_eliment:second_eliment]) # to take two digit every time
        if eliment == ('11'):
            Bashkir = Bashkir + "aа"
        elif eliment == ('10'):
            Bashkir = Bashkir + "cс"
        elif eliment == ('01'):
            Bashkir = Bashkir + "eе"
        elif eliment == ('00'):
            Bashkir = Bashkir + "oо"
        first_eliment += 2
        second_eliment += 2

    # to open two file the first one to reade from and the second to write in

    plan_text = open(x1, 'r')
    cover_text = open(x2, 'w')
    covet_text = open(x2, 'a')

    w = len(Bashkir) # w = the value of length bashkir language string

    counter = 1
    for line_word in plan_text: # loop to take character after character from the plan text

        for char in range(len(line_word)): # loop from 0 to length of line in plan text
            if (counter <= w) and (line_word[char]) == Bashkir[counter - 1]: # if the counter <= number of the character in baskir language string
                cover_text.write(Bashkir[counter]) # hide the secret character in cover text
                counter = counter + 2
            else:
                cover_text.write(line_word[char]) # where the character not equal to the secret character continue write the orignal character
    main_mainu.create_text(180, 310, text='YOUR SECRET MESSAGE WAS HIDDEN SUCCESSFULLY') # to make not that the processing is finsh

def unhiding_processing (): # function to unhiding process
    x4=entry4.get()         # the name of the cover text
    secrit_message = open(x4,'r') # open the cover file to read the secret message


    cover_text = '' # to create string hold the cover text file
    for x in secrit_message:
        cover_text = cover_text + x

    convert_binary = '' # to create string holding the binary digit

    for char in range(len(cover_text)):
        if cover_text[char] == "а":
            convert_binary = convert_binary + "11"
        elif cover_text[char] == "с":
            convert_binary = convert_binary + "10"
        elif cover_text[char] == "е":
            convert_binary = convert_binary + "01"
        elif cover_text[char] == "о":
            convert_binary = convert_binary + "00"

    w = len(convert_binary) / 1.145 # to remove the space after converting
    binary_int = int(convert_binary, 2) # convert to binary
    byte_number = binary_int.bit_length() - int(w)
    binary_array = binary_int.to_bytes(byte_number, "big")
    ascii_text = binary_array.decode()
    main_mainu.create_text(600, 100, text=ascii_text) # showing the secrete message in window


button_hidding = security.Button(text="HIDING",height = '3',width=40, bg='skyblue',command=hiding_processing) # create hidding button
button_hidding.pack()
button_hidding.place(x=40,y=400) #

button_unhiding = security.Button(text="UNHIDING",height = '3',width=40,bg='palegreen',command=unhiding_processing) # create unhiding button
button_unhiding.pack()
button_unhiding.place(x=460,y=400)


button_plan = security.Button(root,text='chose the plan text file',height='2', width='40',command=path_pln)
button_plan.pack()
button_plan.place(x=40,y=40)

# entry1 = security.Entry(root) # create the input for plan text bar in window
# main_mainu.create_window(186,60, window=entry1,height = 20 ,width = 290)
# main_mainu.create_text(180,30,text='INPUT THE TEXT PLAN NAME (.TXT)')

# button_cover = security.Button(text='chose the plan text file',height='3', width='30',command=path_cover)
# button_cover.pack()
# button_cover.place(x=10,y=30)

entry2 = security.Entry(root) # create the input for cover text bar in window
main_mainu.create_window(186,150, window=entry2,height = 20 ,width = 290)
main_mainu.create_text(180,120,text='INPUT THE TEXT COVER NAME (.TXT)')

entry3 = security.Entry(root) # create the input for secret message bar in window
main_mainu.create_window(186,240, window=entry3,height = 20 ,width = 290)
main_mainu.create_text(180,210,text='INPUT THE SECRET MESSAGE TO HIDINING')

entry4 = security.Entry(root) # create the input for cover text bar in window to unhiding
main_mainu.create_window(605,60, window=entry4,height = 20 ,width = 290)
main_mainu.create_text(600,30,text='INPUT THE TEXT COVER NAME (.TXT)')

root.mainloop() # loop to make the window still show