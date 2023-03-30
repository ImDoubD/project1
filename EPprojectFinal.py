import tkinter as tk
from tkinter import *
from tkinter import ttk, Label
import tkinter.font as font
import math
from PIL import ImageTk, Image
from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

root = tk.Tk()
root.geometry('1080x720')
root.resizable()
root.title("Planck's Constant Experiment")
root.configure(bg='lightsteelblue3')

actual_label= Label(root, text="Determination Of Planck's Constant Using Photo Cells", font=('Helvetica',28))
actual_label.config(bg='lightskyblue1')
actual_label.place(x=360, y=10)

filter_label= Label(root, text='Filter:', font=('Helvetica',20))
filter_label.config(bg='grey')
filter_label.place(x=30, y=90)

def Simpletoggle():
    if toggle_button.config('text')[-1] == 'Start':
        toggle_button.config(text='green')
        root.configure(bg='green')
    elif toggle_button.config('text')[-1] == 'green':
        toggle_button.config(text='blue')
        root.configure(bg='blue')
    elif toggle_button.config('text')[-1] == 'blue':
        toggle_button.config(text='orange')
        root.configure(bg='orange')
    elif toggle_button.config('text')[-1] == 'orange':
        toggle_button.config(text='yellow')
        root.configure(bg='yellow')
    elif toggle_button.config('text')[-1] == 'yellow':
        toggle_button.config(text='red')
        root.configure(bg='red')

myFont = font.Font(size=15, weight='bold', family='Courier')
toggle_button = Button(text="Start", width=10, height=2, command=Simpletoggle, bg='pink')
toggle_button['font'] = myFont
toggle_button.place(x=125, y=130)

# wavelength consideration
# slider current value
current_value = tk.DoubleVar()

def get_current_value():
    return '{: .2f}'.format(current_value.get())
def slider_changed(event):
    value_label.configure(text=get_current_value())

# label for the slider
slider_label = Label(root, text='Wavelength:', font=('Helvetica',20))
slider_label.config(bg='grey')
slider_label.place(x=30, y=210)
#  slider
slider = Scale(root, from_=400, to=600, orient='horizontal', command=slider_changed, variable=current_value, width=20 , length=300)
slider.place(x=125, y=265)
# current value label
current_value_label = Label(root, text='Current Wavelength:', font=('Helvetica',15))
current_value_label.config(bg='grey')
current_value_label.place(x=130, y=323)
# value label
value_label = ttk.Label(root, text=get_current_value() ,font=10)

value_label.place(x=130, y=360)

n=0
def lambdaone():
    global a
    a=get_current_value()
    print(a)
def lambdatwo():
    global b
    b=get_current_value()
    print(b)
lambdan= Button(root, text='λ1', command=lambdaone, width=6, bg='pink')
lambdan.place(x=330, y=323)
lamb= Button(root, text='λ2', command=lambdatwo, width=6, bg='pink')
lamb.place(x=390, y=323)

# frequency consideration
# slider current value
current_value_one = tk.DoubleVar()

def get_current_value_freq():
    return '{: .2f}'.format(current_value_one.get())
def slider_changed_freq(event):
    value_label_freq.configure(text=get_current_value_freq())

# label for the slider
slider_label_freq = Label(root, text='Frequency:', font=('Helvetica',20))
slider_label_freq.config(bg='grey')
slider_label_freq.place(x=30, y=400)
#  slider
slider_freq = tk.Scale(root, from_=0, to=7, orient='horizontal', digits=4, resolution=0.001,command=slider_changed_freq, variable=current_value_one, width=20 , length=300)
slider_freq.place(x=125, y=445)
# current value label
current_value_label_freq = Label(root, text='Current Frequency:', font=('Helvetica',15))
current_value_label_freq.config(bg='grey')
current_value_label_freq.place(x=130, y=500)
# value label
value_label_freq = ttk.Label(root, text=get_current_value_freq() ,font=10)
current_value_label_freq.config(bg='grey')
value_label_freq.place(x=130, y=540)
# message
lb = Label(root,text='( x 10^14)', font=('Helvetica',12))
lb.config(bg='white')
lb.place(x=310, y=502)

# stopping potential consideration
# slider current value
current_value_two = tk.DoubleVar()

def get_current_value_stp():
    return '{: .2f}'.format(current_value_two.get())
def slider_changed_stp(event):
    value_label_stp.configure(text=get_current_value_stp())

# label for the slider
slider_label_stp = Label(root, text='Stopping Potential:', font=('Helvetica',20))
slider_label_stp.config(bg='grey')
slider_label_stp.place(x=30, y=580)
#  slider
slider_stp = Scale(root, from_=0, to=2, orient='horizontal',digits=3, resolution=0.001, command=slider_changed_stp, variable=current_value_two, width=20 , length=300)
slider_stp.place(x=125, y=630)
# current value label
current_value_label_stp = Label(root, text='Current Stopping Potential:', font=('Helvetica',15))
current_value_label_stp.config(bg='grey')
current_value_label_stp.place(x=130, y=690)
# value label
value_label_stp = ttk.Label(root, text=get_current_value_stp() ,font=10)
current_value_label_stp.config(bg='grey')
value_label_stp.place(x=130, y=730)

n=0
def stpone():
    global p
    p=get_current_value_stp()
    print(p)
def stptwo():
    global q
    q=get_current_value_stp()
    print(q)
sp= Button(root, text='V1', command=stpone, width=6, bg='pink')
sp.place(x=390, y=690)
st= Button(root, text='V2', command=stptwo, width=6, bg='pink')
st.place(x=450, y=690)

# image
canvas = Canvas(root, width = 500, height = 370)
canvas.place(x=850, y=70)
img = ImageTk.PhotoImage(Image.open(r"C:\Users\DUKE\OneDrive\Pictures\Saved Pictures\epproject.jpg"))
canvas.create_image(1,1, anchor=NW, image=img)

# info table
def info_table():
    newtab = Toplevel(root)
    newtab.title("Information Table")
    newtab.geometry("400x250")

    tab = ttk.Treeview(newtab)
    tab.pack()
    tab['columns']= ('color','wavelength','frequency','stopping potential')
    tab.column("#0", width=0, stretch=NO)
    tab.column("color", anchor=CENTER, width=80)
    tab.column("wavelength", anchor=CENTER, width=80)
    tab.column("frequency", anchor=CENTER, width=80)
    tab.column("stopping potential", anchor=CENTER, width=150)
    tab.heading("#0", text="", anchor=CENTER)
    tab.heading("color", text="Color", anchor=CENTER)
    tab.heading("wavelength", text="Wavelength", anchor=CENTER)
    tab.heading("frequency", text="Frequency", anchor=CENTER)
    tab.heading("stopping potential", text="Stopping Potential", anchor=CENTER)

    tab.insert(parent='', index='end', iid='0', text='',
    values=('Blue','460','6.521 x 10^14', '-1.13'))
    tab.insert(parent='', index='end', iid='1', text='',
    values=('Green','500','6 x 10^14', '-0.92'))
    tab.insert(parent='', index='end', iid='2', text='',
    values=('Yellow','540','5.55 x 10^14', '-0.70'))
    tab.insert(parent='', index='end', iid='3', text='',
    values=('Orange','570','5.263 x 10^14', '-0.58'))
    tab.insert(parent='', index='end', iid='4', text='',
    values=('Red','635','4.724 x 10^14', '-0.40'))

table_button= Button(root, text='Information Table', command=info_table, width=23,height=3, bg='pink')
table_button.place(x=853, y=450)

# graph ( frequency vs stopping potential )
def view_graph():

    data2 = {'Frequency': [4.724, 5.263, 5.550, 6, 6.521],
             'Stopping Potential': [0.40, 0.60, 0.72, 0.91, 1.13]
             }
    df2 = DataFrame(data2, columns=['Frequency', 'Stopping Potential'])

    graph = plt.Figure(figsize=(5, 4), dpi=75)
    g1 = graph.add_subplot(111)
    line2 = FigureCanvasTkAgg(graph, root)
    line2.get_tk_widget().place(x=460  ,y=140)
    df2 = df2[['Frequency', 'Stopping Potential']].groupby('Frequency').sum()
    df2.plot(kind='line', legend=True, ax=g1, color='brown', marker='o', fontsize=10)
    g1.set_title('Frequency Vs. Stopping Potential')

graph_button= Button(root,text='View Graph', command= view_graph, width=20, height=3, bg='pink')
graph_button.place(x=1200, y=449)

# constant calculation, 5**3 means 5 raised to the power 3
def formula():
    global e,c,l,m,k,o, i,w,y,r, constan
    l=pow(10,-19)
    m=pow(10,8)
    k=pow(10,-9)
    e= float(1.6 * l)
    c= float(3 * m)
    i= float(float(a) * k)
    w= float(float(b) * k)
    y= float(p)
    r= float(q)

    constan= float(((e * (y-r)) * (i*w)) / (c * (w-i)))
    print(constan)
    res.set(constan)
def err():
    global f,t,error
    t=pow(10,-34)
    f= float(6.62607015 * t)
    if (f>constan):
        error= float(((f-constan)/f) * 100)
    else:
        error = float(((constan-f)/f) * 100)
    print(error)
    per.set(error)

# result label showcase
res= StringVar()
result= Label(root, text="", textvariable=res)
result.config(font=15)
result.place(x=950, y=614)
per= StringVar()
percent= Label(root, text="", textvariable=per)
percent.config(font=15)
percent.place(x=950, y=694)
#calculate button
form= Button(root, text='Calculate', command=formula, width=11, height=2, bg='pink')
form.place(x=853, y=610)
#error calculate
form= Button(root, text='Error %', command=err, width=11, height=2, bg='pink')
form.place(x=853, y=690)
# calculated planck's constant labe;
planck= Label(root, text="Planck's Constant:-", font=('Helvetica',30))
planck.config(bg='grey')
planck.place(x=853, y=540)

#quit
exit= Button(root, text="Quit", command=root.destroy, width=11, height=2, bg='pink')
exit.place(x=1260, y=750)

root.mainloop()