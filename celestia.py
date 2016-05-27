"""The FiM++ module

Written for Python by Jared Newsom (AKA Jared M.F.)
FiM++ is a programming language created by Kylie Rouge (AKA SupuhStar)

Inspired by Karol Stasiak's FiM++ interpreter
Currently a work-in-progress"""

class Twilight:
    """This is an intergrated development enviroment for the
    language, but, it is also built into the module as well.

    Almost like writing scrolls!"""
    def __init__():
        import tkinter

        global master
        master = tkinter.Tk()

        master.geometry('640x480')
        frame = tkinter.Frame(master=master)
        Twilight.createText()
        Twilight.createMenu()
        Twilight.newFile()
        master.mainloop()

    def createText():
        import tkinter, sys

        global text

        text = tkinter.Text(master=master,foreground='purple',background='#ff64d0',
                            font='Ubuntu' if sys.platform.startswith('linux') else 'San Francisco' if sys.platform.startswith('darwin') else 'Calibri',
                            selectforeground='#ff64d0',selectbackground='purple',wrap='word',undo=True,autoseparators=True,maxundo=-1)
        text.bind('<Button-3>',Twilight.popMenu)
        text.bind('<Key>',Twilight.keyCallback)
        text.pack(side='left', fill='both', expand=1)

    def createMenu():
        import tkinter

        menubar = tkinter.Menu(master=master)

        filemenu = tkinter.Menu(master=menubar,tearoff=0)
        filemenu.add_command(label='New',command=Twilight.newFile,accelerator='Ctrl+N')
        filemenu.add_command(label='Open',command=Twilight.loadFile,accelerator='Ctrl+O')
        filemenu.add_command(label='Save',command=Twilight.saveFile,accelerator='Ctrl+S')
        filemenu.add_command(label='Save As...',command=Twilight.saveAs,accelerator='Ctrl+Shift+S')
        filemenu.add_separator()
        filemenu.add_command(label='Exit',accelerator='Ctrl+Q')
        menubar.add_cascade(label='File',menu=filemenu)

        editmenu = tkinter.Menu(master=menubar,tearoff=0)
        editmenu.add_command(label='Undo',command=Twilight.undo)
        editmenu.add_command(label='Redo',command=Twilight.redo)
        editmenu.add_separator()
        editmenu.add_command(label='Cut')
        editmenu.add_command(label='Copy')
        editmenu.add_command(label='Paste')
        editmenu.add_separator()
        editmenu.add_command(label='Find')
        editmenu.add_command(label='Replace')
        menubar.add_cascade(label='Edit',menu=editmenu)

        master.config(menu=menubar)

    def newFile():
        global filename
        
        if master.title().startswith('*'):
            Twilight.save_question()
        if text.get('1.0','end') != None:
            text.delete('1.0','end')
        text.insert('1.0','Dear Princess Celestia: Letter One:\n\n'
                    'Today I learned:\n\nBy the way, this is a placeholder.\n\n'
                    'Your faithful student, Twilight Sparkle.')
        filename = 'Untitled'
        master.title('(' + filename + ') Project Twilight - The FiM++ IDE')
        text.edit_reset()

    def saveFile():
        global filename
        
        import os.path
        if os.path.exists(filename) and filename != 'Untitled':
            save = open(filename, mode='w')
            save.write(text.get('1.0','end-1c'))
            save.close()
            master.title('(' + filename + ') Project Twilight - The FiM++ IDE')
            text.edit_reset()
        else:
            Twilight.saveAs()

    def loadFile():
        global filename
        
        if master.title().startswith('*'):
            Twilight.save_question()
        f = FlashSentry.load()
        if f != None:
            if f.endswith('.fimpp'):
                load = open(f, mode='r')
                contents = load.read()
                text.delete('1.0','end')
                text.insert('1.0',contents)
                load.close()
                filename = f
                master.title('(' + filename + ') Project Twilight - The FiM++ IDE')
                text.edit_reset()
            else:
                import tkinter.dialog
                d = tkinter.dialog.Dialog(master=None,title='Invalid file',
                                          text="That ain't no file I've ever heard of.\n"
                                          'TO THE MOOOOOOOON!!!\n\n-Princess Luna',
                                          bitmap='warning',default=0,strings=('Okay...?','Try again!'))
                if d != 0:
                    Twilight.loadFile()

    def saveAs():
        f = FlashSentry.save()
        if f != None:
            if f.endswith('.fimpp'):
                filename = f
                Twilight.saveFile()
            else:
                import tkinter.dialog
                d = tkinter.dialog.Dialog(master=None,title='Invalid file',
                                          text="I'm not sure if that file will save properly, Anon.\n"
                                          'Remember, try, try again. ;)\n\n-Twilight Sparkle',
                                          bitmap='questhead',default=0,strings=('Nevermind...','Thank you, Twilight! ^w^'))
                if d != 0:
                    Twilight.saveAs()

    def undo():
        try:
            text.edit_undo()
        except:
            pass

    def redo():
        try:
            text.edit_redo()
        except:
            pass

    def save_question():
        import tkinter.dialog
        d = tkinter.dialog.Dialog(master=None,title='Hold your horses!',
                                  text='Are you sure you want to save changes to this file?'
                                  "\nThey would be lost if you didn't!\n"
                                  '\n-Twilight Sparkle',
                                  bitmap='questhead',default=0,strings=('Eeyup','Nah'))
        if d.num != 1:
            Twilight.save()

    def keyCallback(event):
        """This command may not be recommended for use, but,
        It will tell you if you make a change in the text
        using the very convenient keyboard."""
        global filename
        
        if not master.title().startswith('*'):
            master.title('*(' + filename + ') Project Twilight - The FiM++ IDE')

    def popMenu(event):
        """This command may not be recommended for use, but,
        It will tell you if you right click on the IDE,
        and show the very convenient pop-up menu."""
        import tkinter
        pop = tkinter.Menu(master=master,tearoff=0)

        popfile = tkinter.Menu(master=pop,tearoff=0)
        popfile.add_command(label='New',command=Twilight.newFile,accelerator='Ctrl+N')
        popfile.add_command(label='Open',command=Twilight.loadFile,accelerator='Ctrl+O')
        popfile.add_command(label='Save',command=Twilight.saveFile,accelerator='Ctrl+S')
        popfile.add_command(label='Save As...',command=Twilight.saveAs,accelerator='Ctrl+Shift+S')
        popfile.add_separator()
        popfile.add_command(label='Exit',accelerator='Ctrl+Q')
        pop.add_cascade(label='File',menu=popfile)

        popedit = tkinter.Menu(master=pop,tearoff=0)
        popedit.add_command(label='Undo',command=Twilight.undo)
        popedit.add_command(label='Redo',command=Twilight.redo)
        popedit.add_separator()
        popedit.add_command(label='Cut')
        popedit.add_command(label='Copy')
        popedit.add_command(label='Paste')
        popedit.add_separator()
        popedit.add_command(label='Find')
        popedit.add_command(label='Replace')
        pop.add_cascade(label='Edit',menu=popedit)

        pop.post(event.x_root,event.y_root)

class FlashSentry:
    """This is a helper class for compiling FiM++ files
    into Python files, just like magic.

    Plus, it has a load file function and a save file function!

    You might just need it for anything cool. B)"""
    def compile(x):
        """This function will do the magic of compilation,
        just like Flash Sentry's cousin, Vinyl Scratch.

        By the way, have you listened to dubstep?"""
        code = []
        if x != None:
            if x.endswith('.fimpp'):
                print(x, end='\n\n')
                import fileimport as Spike
                f = Spike.input(files=(x))
                for line in f:
                    if line != '\n':
                        import shlex as DerpyHooves
                        k = DerpyHooves.split(line, posix=False)
                        if k[0] == 'Dear':
                            for i in k:
                                if i.endswith(':') or i.endswith(','):
                                    for j in k:
                                        if j != k[i]:
                                            del k[j]
                                        else:
                                            className = None
                                            from string import punctuation
                                            for c in k:
                                                className = className + k[c]
                                            className = className.strip(punctuation)
                                            code.append('class', className + ':\n')
                                            break
                        elif k[0] == 'My' and k[1] == 'dear':
                            for i in k:
                                if i.endswith(':') or i.endswith(','):
                                    for j in k:
                                        if j != k[i]:
                                            del k[j]
                                        else:
                                            className = None
                                            from string import punctuation
                                            for c in k:
                                                className = className + k[c]
                                            className = className.strip(punctuation)
                                            code.append('class', className + ':\n')
                                            break
            else:
                FlashSentry.compile_error()
        else:
            FlashSentry.no_file()

    def load():
        """This function will load the file.

        We all have to start somewhere..."""
        from tkinter import Tk
        import tkinter.filedialog
        root = Tk()
        root.withdraw()
        fd = tkinter.filedialog.LoadFileDialog(master=root,title='Project Celestia')
        loadfile = fd.go()
        if loadfile != None:
            return loadfile
        root.destroy()

    def save():
        """This function will save the file.
        It will also save the day, too!

        You just might be safe with this one!"""
        from tkinter import Tk
        import tkinter.filedialog
        root = Tk()
        root.withdraw()
        fd = tkinter.filedialog.FileDialog(master=root,title='Project Celestia')
        savefile = fd.go()
        if savefile != None:
            import os.path, tkinter.dialog
            if os.path.exists(savefile):
                if os.path.isdir(savefile):
                    tkinter.filedialog.FileDialog.master.bell()
                    return savefile
                d = tkinter.dialog.Dialog(master=None,title='Hold your horses!',
                                          text='Are you sure you want to rewrite this file?'
                                          '\nI mean, I have already seen the file before...\n'
                                          '\n-Twilight Sparkle',
                                          bitmap='questhead',default=0,strings=('Eeyup','Nah'))
                if d.num != 1:
                    return savefile
        else:
            FlashSentry.save_error()
        root.destroy()

    def compile_error():
        """This function will tell you if the class can't
        compile the file.

        It is very important!"""
        import tkinter.dialog
        k = tkinter.dialog.Dialog(master=None,title='Hold your horses!',
                                  text="I can't compile this file right away!\n"
                                  "It won't work, even if I try to do it!\n\n-Flash Sentry\n\nP.S. Maybe you could get a different file?\n"
                                  "That would be really awesome if you did.",
                                  bitmap='warning',default=0,strings=('Okay...?','Try again!'))
        if k.num != 0:
            x = FlashSentry.load()
            FlashSentry.compile(x)

    def no_file(editor=False):
        """This is a function for telling you when there is no file.

        That is all about this function that I can tell you."""
        import tkinter.dialog
        k = tkinter.dialog.Dialog(master=None,title='File not found',
                                  text="No file found, but, you can always try again! ;)\n\n-Twilight Sparkle",
                                  bitmap='questhead',default=0,strings=('Nevermind...','Thank you, Twilight! ^w^'))
        if k.num != 0:
            if editor is True:
                Twilight.openFile()
            else:
                x = FlashSentry.load()
                FlashSentry.compile(x)

    def save_error():
        """This is a function for telling you when the file
        cannot be saved...at all.

        Be a wary person, or a wary pony."""
        import tkinter.dialog
        k = tkinter.dialog.Dialog(master=None,title='Oh no...',
                                  text="I tried to save the file...\nBut it was too late...\nI...I'm sorry, Anon. :'(\n\n-Rainbow Dash",
                                  bitmap='questhead',default=0,strings=('Awww...',"It's okay, Rainbow Dash."))
        if k.num != 0:
            x = FlashSentry.save()

class Trollestia:
    """This is a helper class for providing error messages.

    It consists of error related functions."""
    def program_error(x):
        """The program error function.

        This handles program errors, hence its name."""
        if x == 1:
            print("That ain't no program I've ever heard of.\nTO THE MOOOOOOOON!!!\n\n-Princess Luna")
        elif x == 2:
            print("Now, you have to tell me:\nWhat did you learn today?\n\n-Princess Celestia")
        elif x == 3:
            print("Before I read this file:\nI want to know who this is for.\n\n-Princess Celestia")

    def math_error(x):
        """The math error function.

        It knows math and it may also know what happens when you try to
        change something that's not a number."""
        if x == 1:
            print("Trying to add a number to something else, eh?\nDo you know math at all?\n\n-Twilight Sparkle")
        elif x == 2:
            print("Trying to subtract a number from something else, eh?\nDo you know math at all?\n\n-Twilight Sparkle")
        elif x == 3:
            print("Trying to multiply a number by something else, eh?\nDo you know math at all?\n\n-Twilight Sparkle")
        elif x == 4:
            print("Trying to divide a number by something else, eh?\nDo you know math at all?\n\n-Twilight Sparkle")
        elif x == 5:
            print("WHAT?!? Division by zero?\nCould that be the worst possible thing?\n\n-Ms. Rarity")

    def invalid(x, y, z):
        """This function tells you if something is invalid.

        For example, invalid identifiers."""
        if x == 1:
            lineset_1 = "Now, say, do you like mmm-syntax errors?\nYou have one in this function after all:\n'" + y
            lineset_2 = "'\nNo? So, let me get it straight:\nYou're a mmm-biatch that does not like syntax errors."
            lineset_3 = "\nThat's good, because there are no syntax errors...ON THE MOOOOOOOON!!!\n\n-Princess Celestia"
            print(lineset_1 + lineset_2 + lineset_3)
        elif x == 2:
            print("Mmm-" + y + "...\nI've never heard of such a pony, you know.\nDo they have tea parties with", y + "?\n\n-Princess Celestia")
        elif x == 3:
            print("This function is a changeling!\nAt the beginning, it was named", y + ", and now it's", z + "!\n\n-Princess Celestia")

    def what_went_wrong():
        """The unknown error function.

        A classic running gag in programming language interpreters."""
        from random import randrange
        oh_noez = ["To the moon with that code!\n\n-Princess Celestia and Princess Luna", "I just don't know what went wrong. :'(\n\n-Derpy Hooves",
                   "Look, I may not understand that program:\nBut, here are two little words:\nTry again! ;)\n\n-Twilight Sparkle",
                   "Hahaha, you're so funny! XD\nAnd so is your program! :)\n\n-Pinkie Pie", "This program must be...DISCORDED.\n\n-Discord",
                   "Well, um...\nI don't know what to say about this.\n\n-Your dear Fluttershy", "Alright, Anon, we get it.\nYou wanted to run it, ok?\n\n-Scootaloo",
                   "PLBLBLBLBLBLBLBLBLBLT!!!\n\n-Fluffle Puff\n\nP.S. She was trying to tell you that your code was not valid. -Queen Chrysalis",
                   "Wahahahahahaha! >:)\nNow fix that code right away! >:)\n\n-Ms. Rarity", "That program doubts all logic, my friend. ¬_¬\n\n-Doctor Whooves",
                   "...\n\n-Maud Pie", "Sorry, sug'r-cube, but, this program ain't programmed right.\n\n-Applejack", "Hey, no fair, you cheated! >:(\n\n-Rainbow Dash"]
        idk = oh_noez[randrange(13)]
        print(idk)

def check_footer(footer):
    """Tells you if the footer matches the name.

    If not, then, Princess Celestia will accuse it of being a changeling."""
    if footer:
        return True
    else:
        return False

def parse_cmd(line, code, var):
    """This will parse the program's lines, in the main function,
    so it can be executed properly.

    Do note that it may not parse all lines."""
    if line != '\n':
        import shlex as DerpyHooves
        x = DerpyHooves.split(line, posix=False)
        func_call_keywords = ['did', 'caused', 'made', 'remembered', 'would', 'knew']
        var_assign_keywords = ['is', 'are', 'likes', 'loves', 'was', 'were', 'liked', 'loved']
        incr_keywords = ['more', 'fewer', 'less', 'another']
        bool_keywords = ['harmony', 'chaos', 'nothing', 'nopony', 'nobody', 'no-one', 'something',
                         'somepony', 'somebody', 'someone', 'good', 'bad', 'neutral', 'evil', 'discorded',
                         'nice', 'mean', 'kind', 'rude', 'real', 'fake', 'facts', 'lies', 'fiction', 'non-fiction']
        if x[0] == "I":
            if x[1].startswith('said') or x[1].startswith('wrote') or x[1].startswith('sang'):
                if x[2].startswith("nothing") or x[2].startswith("nopony") or x[2].startswith("nobody"):
                    print(None)
                elif x[2].startswith("harmony"):
                    print(True)
                elif x[2].startswith("chaos"):
                    print(False)
                elif x[2] in var:
                    print(var[x[2]])
                else:
                    if x[2].startswith('"') and x[2].endswith('"'):
                        k = x[2].split('"')
                        print(k[1])
                    elif x[2].startswith("'") and x[2].endswith("'"):
                        k = x[2].split("'")
                        print(k[1])
                    else:
                        Trollestia.what_went_wrong()
            elif x[1] in func_call_keywords:
                if x[1] == func_call_keywords[4]:
                    k = "I learned how to", x[2]
                else:
                    k = "I learned", x[2]

                if k in code:
                    for p in code:
                        while p != k:
                            pass
                        else:
                            if not p.startswith("That's about") and not p.startswith("That is about"):
                                parse_cmd(p, code, var)
                            else:
                                r = DerpyHooves.split(p, posix=False)
                                if r[0] == "That's" and r[1] == "about":
                                    if check_footer(r[2]):
                                        pass
                                    else:
                                        Trollestia.invalid(3, x[2], r[2])
                                        break
                                elif r[0] == "That" and r[1] == "is" and r[2] == "about":
                                    if check_footer(r[3]):
                                        pass
                                    else:
                                        Trollestia.invalid(3, x[2], r[3])
                                        break
                else:
                    Trollestia.what_went_wrong()
            elif x[1] == asked and x[2].startswith(var[x[2]]):
                if x[3].startswith('"') and x[3].endswith('"'):
                    k = x[3].split('"')
                    var[x[2]] = input(k)
                elif x[3].startswith("'") and x[3].endswith("'"):
                    k = x[3].split("'")
                    var[x[2]] = input(k)
                else:
                    Trollestia.what_went_wrong()
        elif x[0] == "Did" and x[1] == "you" and x[2] == "know":
            if x[3] == "that":
                if x[5] in var_call_keywords:
                    if x[6] in var:
                        var[x[4]] = var[x[6]]
                    else:
                        var[x[4]] = eval(x[6])
                else:
                    Trollestia.invalid(2, x[5], None)
            else:
                if x[4] in var_call_keywords:
                    var[x[3]] = eval(x[5])
                else:
                    Trollestia.invalid(2, x[4], None)
        elif x[0] in var:
            if x[1] == "got":
                if x[3] in incr_keywords:
                    if x[3] == incr_keywords[0] or x[3] == incr_keywords[3]:
                        var[x[0]] = eval(x[0]) + eval(x[2])
                    elif x[3] == incr_keywords[1] or x[3] == incr_keywords[2]:
                        var[x[0]] = eval(x[0]) - eval(x[2])
            elif x[1] in func_call_keywords:
                if x[1] == func_call_keywords[4]:
                    k = "I learned how to", x[2]
                else:
                    k = "I learned", x[2]

                if k in code:
                    temp_var = {}
                    for p in code:
                        while p != k:
                            pass
                        else:
                            if not p.startswith("That's about") and not p.startswith("That is about"):
                                r = DerpyHooves.split(p, posix=False)
                                if r[0] == "Then" and r[1] == "you" and r[2] == "get":
                                    if r[3] in temp_var:
                                        var[x[0]] = temp_var[p[3]]
                                    else:
                                        Trollestia.invalid(2, p[3], None)
                                else:
                                    parse_cmd(p, code, temp_var)
                            else:
                                r = DerpyHooves.split(p, posix=False)
                                if r[0] == "That's" and r[1] == "about" and r[3] == "with" and r[4] in temp_var:
                                    if check_footer(r[2]):
                                        var[x[0]] = temp_var[r[4]]
                                    else:
                                        Trollestia.what_went_wrong()
                                        break
                                elif r[0] == "That" and r[1] == "is" and r[2] == "about" and r[4] == "with" and r[5] in temp_var:
                                    if check_footer(r[3]):
                                        var[x[0]] = temp_var[r[5]]
                                    else:
                                        Trollestia.what_went_wrong()
                                        break
                else:
                    Trollestia.what_went_wrong()
    else:
        pass

def run(x):
    """This will run the FiM++ file's program.

    Do beware for if you try to run any file other than an FiM++ file,
    Princess Luna will (maybe threaten to) send you to the moon."""
    if x != None:
        print(x, end='\n\n')
        if x.endswith('.fimpp'):
            import fileinput as Spike
            with Spike.input(files=(x)) as f:
                var = {}
                start = 0
                for line in f:
                    if start == 0:
                        if line.startswith('Dear') or line.startswith('My dear'):
                            start = 1
                        else:
                            Trollestia.program_error(3)
                            Spike.close()
                    elif start == 1:
                        if not line.startswith('Today I learned'):
                            pass
                        else:
                            if start == 1:
                                start = 2
                            else:
                                Trollestia.program_error(2)
                                Spike.close()
                    elif start == 2:
                        while not line.startswith('Your faithful student,') or line.startswith('Yours truly,') or line.startswith('Love,'):
                            parse_cmd(line, f, var)
                        else:
                            print("\n\nProgram successfully interpretered!")
        else:
            Trollestia.program_error(1)
    else:
        FlashSentry.no_file(editor=False)

if __name__ == '__main__':
    import sys as fimpp
    try:
        run(sys.argv[1])
    except:
        pass
