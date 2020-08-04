import tkinter as tk
from tkinter import ttk
from tkinter import messagebox,font,colorchooser,filedialog
import os

main_application=tk.Tk()
# main_application.geometry('1200*800')
main_application.title('TEXT EDITOR')

#  main menu
main_menu=tk.Menu(main_application)

# add icons for file menu
new_icon=tk.PhotoImage(file=r'F:\python course\new.png')
open_icon=tk.PhotoImage(file=r'F:\python course\open.png')
save_icon=tk.PhotoImage(file=r'F:\python course\save.png')
save_as_icon=tk.PhotoImage(file=r'F:\python course\save_as.png')
exit_icon=tk.PhotoImage(file=r'F:\python course\exit.png')

file_menu=tk.Menu(main_menu,tearoff=0)

# add icons for edit menu
copy_icon=tk.PhotoImage(file=r'F:\python course\copy.png')
cut_icon=tk.PhotoImage(file=r'F:\python course\cut.png')
paste_icon=tk.PhotoImage(file=r'F:\python course\paste.png')
find_icon=tk.PhotoImage(file=r'F:\python course\find.png')
clear_all_icon=tk.PhotoImage(file=r'F:\python course\clear_all.png')

edit_menu=tk.Menu(main_menu,tearoff=0)

# add icons for view menu
tool_bar_icon=tk.PhotoImage(file=r'F:\python course\tool_bar.png')
status_bar_icon=tk.PhotoImage(file=r'F:\python course\status_bar.png')

view_menu=tk.Menu(main_menu,tearoff=0)

# add icons for color theme menu
light_default_icon=tk.PhotoImage(file=r'F:\python course\light_default.png')
light_plus_icon=tk.PhotoImage(file=r'F:\python course\light_plus.png')
dark_icon=tk.PhotoImage(file=r'F:\python course\dark.png')
red_icon=tk.PhotoImage(file=r'F:\python course\red.png')
monokai_icon=tk.PhotoImage(file=r'F:\python course\monokai.png')
night_blue_icon=tk.PhotoImage(file=r'F:\python course\night_blue.png')

color_theme_menu=tk.Menu(main_menu,tearoff=0)

theme_choice=tk.StringVar()
color_icons=(light_default_icon,light_plus_icon,dark_icon,red_icon,monokai_icon,night_blue_icon)
color_dict={
    'Light Default' :('#000000','#ffffff'),
    # (foreground,background)
    'Light Plus' :('#474747','#e0e0e0'),
    'Dark' :('#c4c4c4','#2d2d2d'),
    'Red' :('#2d2d2d','#ffe8e8'),
    'Monokai' :('#d3b774','#474747'),
    'Night Blue' :('#ededed','#6b9dc2')
}

# main menu cascade
main_menu.add_cascade(label='File',menu=file_menu)
main_menu.add_cascade(label='Edit',menu=edit_menu)
main_menu.add_cascade(label='View',menu=view_menu)
main_menu.add_cascade(label='Color Theme',menu=color_theme_menu)

# create toolbar
tool_bar=ttk.Label(main_application)
tool_bar.pack(side=tk.TOP,fill=tk.X)

# font box
font_tuple=tk.font.families()
font_family=tk.StringVar()
font_box=ttk.Combobox(tool_bar,width=30,textvariable=font_family,state='readonly')
font_box['values']=font_tuple
font_box.grid(row=0,column=0,padx=5)
font_box.current(font_tuple.index('Arial'))

# size box
size_var=tk.IntVar()
font_size=ttk.Combobox(tool_bar,width=14,textvariable=size_var,state='readonly')
font_size['values']=tuple(range(8,81))
font_size.grid(row=0,column=1,padx=5)
font_size.current(4)

# bold button
bold_icon=tk.PhotoImage(file=r'F:\python course\bold.png')
bold_btn=ttk.Button(tool_bar,image=bold_icon)
bold_btn.grid(row=0,column=2,padx=5)

italic_icon=tk.PhotoImage(file=r'F:\python course\italic.png')
italic_btn=ttk.Button(tool_bar,image=italic_icon)
italic_btn.grid(row=0,column=3,padx=5)

underline_icon=tk.PhotoImage(file=r'F:\python course\underline.png')
underline_btn=ttk.Button(tool_bar,image=underline_icon)
underline_btn.grid(row=0,column=4,padx=5)

# font_color button
font_color_icon=tk.PhotoImage(file=r'F:\python course\font_color.png')
font_color_btn=ttk.Button(tool_bar,image=font_color_icon)
font_color_btn.grid(row=0,column=5,padx=5)

# left align button
align_left_icon=tk.PhotoImage(file=r'F:\python course\align_left.png')
align_left_btn=ttk.Button(tool_bar,image=align_left_icon)
align_left_btn.grid(row=0,column=6,padx=5)

# center align button
align_center_icon=tk.PhotoImage(file=r'F:\python course\align_center.png')
align_center_btn=ttk.Button(tool_bar,image=align_center_icon)
align_center_btn.grid(row=0,column=7,padx=5)

# right align button
align_right_icon=tk.PhotoImage(file=r'F:\python course\align_right.png')
align_right_btn=ttk.Button(tool_bar,image=align_right_icon)
align_right_btn.grid(row=0,column=8,padx=5)

#  ------------------&&&&&&&&&&& end toolbar &&&&&&&&&&&---------------------

# create text editor
text_editor=tk.Text(main_application)
text_editor.config(wrap='word',relief=tk.FLAT)

scroll_bar=tk.Scrollbar(main_application)
text_editor.focus_set()
scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
text_editor.pack(fill=tk.BOTH,expand=True)
scroll_bar.config(command=text_editor.yview)
text_editor.config(yscrollcommand=scroll_bar.set)

# font family and font size functionality
cur_font_family='Arial'
cur_font_size=12


def change_font(event=None):
    global cur_font_family
    cur_font_family=font_family.get()
    text_editor.configure(font=(cur_font_family,cur_font_size))

font_box.bind("<<ComboboxSelected>>",change_font)

def change_fontsize(event=None):
    global cur_font_size
    cur_font_size=size_var.get()
    text_editor.configure(font=(cur_font_family,cur_font_size))

font_size.bind("<<ComboboxSelected>>",change_fontsize)


# bold button functionality
# actual() gives dictionary
def change_bold(event=None):
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(cur_font_family,cur_font_size,'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(cur_font_family,cur_font_size,'normal'))

bold_btn.configure(command=change_bold)

def change_italic(event=None):
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(cur_font_family,cur_font_size,'italic'))
    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(cur_font_family,cur_font_size,'normal'))

italic_btn.configure(command=change_italic)


def change_underline(event=None):
    text_property=tk.font.Font(font=text_editor['font'])
    if text_property.actual()['underline']==0:
        text_editor.configure(font=(cur_font_family,cur_font_size,'underline'))
    if text_property.actual()['underline']=='underline':
        text_editor.configure(font=(cur_font_family,cur_font_size,0))

underline_btn.configure(command=change_underline)

text_editor.configure(font=('Arial',12))

# font color functionality
def change_font_color():
    color_var=tk.colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=change_font_color)

# align funvtionality
def align_left(event=None):
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('left',justify=tk.LEFT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'left')

align_left_btn.configure(command=align_left)

def align_center(event=None):
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('center',justify=tk.CENTER)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'center')

align_center_btn.configure(command=align_center)

def align_right(event=None):
    text_content=text_editor.get(1.0,'end')
    text_editor.tag_config('right',justify=tk.RIGHT)
    text_editor.delete(1.0,tk.END)
    text_editor.insert(tk.INSERT,text_content,'right')

align_right_btn.configure(command=align_right)

text_editor.configure(font=('Arial',12))

# status bar functionality
status_bar=ttk.Label(main_application,text='Status bar')
status_bar.pack(side=tk.BOTTOM)

text_changed=False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        # check wether something is typed or not
        text_changed = True
        words=len(text_editor.get(1.0,'end-1c').split())
        # 1c is written so that it does nt count new line as a character
        characters=len(text_editor.get(1.0,'end-1c'))
        status_bar.config(text=f'Characters :{characters} Words :{words}')
    text_editor.edit_modified(False)

text_editor.bind("<<Modified>>",changed)


# main menu functionality

# variable
url=''

# NEW functionality
def new_file(event=None):
    global url
    url=''
    text_editor.delete(1.0,tk.END)

# file menu commands
file_menu.add_command(label='New',image=new_icon,compound=tk.LEFT,accelerator='Ctrl+N',command=new_file)

# OPEN functionality
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select File',filetypes=(('Text file','.txt'),('All file','*.*')))
    try:
        with open(url,'r') as fr:
            text_editor.delete(1.0,tk.END)
            text_editor.insert(1.0,fr.read())
    except FileNotFoundError:
        return
    except:
        # jb koi file select ni hogi
        return

file_menu.add_command(label='Open',image=open_icon,compound=tk.LEFT,accelerator='Ctrl+O',command=open_file)
file_menu.add_separator()

# SAVE functionality
def save_file(event=None):
    global url
    try:
        if url:
            content = str(text_editor.get(1.0,tk.END))
            with open(url,'w',encoding='utf-8') as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode= 'w',defaultextension='.txt',filetypes=(('Text file','.txt'),('All file','*.*')))
            content2=text_editor.get(1.0,tk.END)
            url.write(content2)
            url.close()
    except:
        return
    
file_menu.add_command(label='Save',image=save_icon,compound=tk.LEFT,accelerator='Ctrl+S',command=save_file)

# SAVE AS functionality
def save_as_file(event=None):
    global url
    try:
            content = str(text_editor.get(1.0,tk.END))
            url=filedialog.asksaveasfile(mode= 'w',defaultextension='.txt',filetypes=(('Text file','.txt'),('All file','*.*')))
            url.write(content)
            main_application.title(os.path.basename(url))
            url.close()
    except:
        return
    
file_menu.add_command(label='Save As',image=save_as_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+S',command=save_as_file)
file_menu.add_separator()

# EXIT functionality
def exit_func(event=None):
    global url,text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel('Warning','Do you want to save the file ?')
            if mbox is True :
                if url:
                    content = text_editor.get(1.0,tk.END)
                    with open (url,'w',encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2=text_editor.get(1.0,tk.END)
                    url=filedialog.asksaveasfile(mode= 'w',defaultextension='.txt',filetypes=(('Text file','.txt'),('All file','*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

file_menu.add_command(label='Exit',image=exit_icon,compound=tk.LEFT,accelerator='Ctrl+Q',command=exit_func)


# edit menu commands

edit_menu.add_command(label='Copy',image=copy_icon,compound=tk.LEFT,accelerator='Ctrl+C',command=lambda:text_editor.event_generate("<Control c>"))

edit_menu.add_command(label='Cut',image=cut_icon,compound=tk.LEFT,accelerator='Ctrl+X',command=lambda:text_editor.event_generate("<Control x>"))

edit_menu.add_command(label='Paste',image=paste_icon,compound=tk.LEFT,accelerator='Ctrl+V',command=lambda:text_editor.event_generate("<Control v>"))

edit_menu.add_command(label='Clear All',image=clear_all_icon,compound=tk.LEFT,accelerator='Ctrl+Alt+x',command=lambda:text_editor.delete(1.0,tk.END))

# find functionality
def find_func(event=None):

    def find():
        word=find_input.get()
        text_editor.tag_remove('match','1.0',tk.END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word,start_pos,stopindex=tk.END)
                if not start_pos:
                    break
                end_pos=f'{start_pos} + {len(word)}c'
                text_editor.tag_add('match',start_pos,end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match',foreground='red',background='yellow')
    def replace():
        word=find_input.get()
        replace_text=replace_input.get()
        content=text_editor.get(1.0,tk.END)
        new_content=content.replace(word,replace_text)
        text_editor.delete(1.0,tk.END)
        text_editor.insert(1.0,new_content)
        

    find_dialogue=tk.Toplevel()
    find_dialogue.geometry('450x250+500+200')
    find_dialogue.title('Find')
    find_dialogue.resizable(0,0)
    
    # frame
    find_frame=ttk.LabelFrame(find_dialogue,text='Find/Replace')
    find_frame.pack(pady=20)
    #  frame labels
    text_find_label=ttk.Label(find_frame,text='Find: ')
    text_replace_label=ttk.Label(find_frame,text='Replace: ')
    text_find_label.grid(row=0,column=0,padx=4,pady=4)
    text_replace_label.grid(row=1,column=0,padx=4,pady=4)
    
    find_input=ttk.Entry(find_frame,width=30)
    replace_input=ttk.Entry(find_frame,width=30)
    find_input.grid(row=0,column=1,padx=4,pady=4)
    replace_input.grid(row=1,column=1,padx=4,pady=4)

    find_btn=ttk.Button(find_frame,text='Find',command=find)
    replace_btn=ttk.Button(find_frame,text='Replace',command=replace)
    find_btn.grid(row=2,column=0,padx=8,pady=4)
    replace_btn.grid(row=2,column=1,padx=8,pady=4)

    find_dialogue.mainloop()
edit_menu.add_command(label='Find',image=find_icon,compound=tk.LEFT,accelerator='Ctrl+F',command=find_func)



# view menu commands

show_statusbar=tk.BooleanVar()
show_statusbar.set(True)
show_toolbar=tk.BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=tk.TOP,fill=tk.X)
        text_editor.pack(fill=tk.BOTH,expand=True)
        status_bar.pack(side=tk.BOTTOM)
        show_toolbar=True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=tk.BOTTOM)
        show_statusbar=True

view_menu.add_checkbutton(label='Tool Bar',onvalue=True,offvalue=0,variable=show_toolbar,image=tool_bar_icon,compound=tk.LEFT,command=hide_toolbar)
view_menu.add_checkbutton(label='Status Bar',onvalue=1,offvalue=False,variable=show_statusbar, image=status_bar_icon,compound=tk.LEFT,command=hide_statusbar)

# color theme menu commands
def change_theme():
    chosen_theme=theme_choice.get()
    color_tuple=color_dict.get(chosen_theme)
    fg_color,bg_color=color_tuple[0],color_tuple[1]
    text_editor.config(background=bg_color,foreground=fg_color)

c=0
for i in color_dict:
    color_theme_menu.add_radiobutton(label=i,image=color_icons[c],variable=theme_choice,compound=tk.LEFT,command=change_theme)
    c+=1
    

main_application.config(menu=main_menu)

# bind shortcut keys
main_application.bind("<Control-n>",new_file)
main_application.bind("<Control-o>",open_file)
main_application.bind("<Control-s>",save_file)
main_application.bind("<Control-Alt-s>",save_as_file)
main_application.bind("<Control-q>",exit_func)
main_application.bind("<Control-f>",find_func)
main_application.bind("<Control-l>",align_left)
main_application.bind("<Control-e>",align_center)
main_application.bind("<Control-r>",align_right)
main_application.bind("<Control-b>",change_bold)
main_application.bind("<Control-i>",change_italic)
main_application.bind("<Control-u>",change_underline)

main_application.mainloop()
