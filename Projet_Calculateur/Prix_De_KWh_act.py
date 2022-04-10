from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from Variables_Fixes import *

# Coef_De_Charge = {'Photovoltaique':0.3, 'CSP': 0.95, 'Dechets':0.95, 'Eolienne offshore': 0.4}
# Prix_du_kw = {'Photovoltaique':3000, 'CSP': 2000, 'Dechets':4200, 'Eolienne offshore':5000}
# Duree_De_Vie = {'Photovoltaique':75, 'CSP': 50, 'Dechets':20, 'Eolienne offshore':45}

#Root window
root = tk.Tk()
w = root.winfo_height
root.geometry("550x200")
root.title("Prix du KWh")
root.configure(bg = 'white')

#labels
label = Label(root,text = "Le prix du KWh est", font = 'arial', bg = 'white')
label.grid(row = 7,column = 0, sticky = 'e')
label_kw = Label(root , text = "Prix du KW est(en $) : ", font = 'arial', bg = 'white'). grid(row = 2, column = 0, sticky = 'w')
label_coef = Label(root , text = "Coefficient de charge est : ", font = 'arial', bg = 'white'). grid(row = 3, column = 0, sticky = 'w')
label_duree = Label(root , text = "La duree de vie est : ", font = 'arial', bg = 'white'). grid(row = 4, column = 0, sticky = 'w')
label_taux = Label(root , text = "Le taux de croissance économique est : ", font = 'arial', bg = 'white'). grid(row = 5, column = 0, sticky = 'w') 
prix = Label(root,text = "0.0$", font = 'arial', fg = 'red', bg = 'white')
prix.grid(row = 7,column = 2, sticky = 'w')


#Fonctions
def Button(event):
   kw.set(str(Prix_du_kw[drop.get()]))
   coef.set(str(Coef_De_Charge[drop.get()]))
   duree.set(str(Duree_De_Vie[drop.get()]))
   taux.set(str(taux_croiss_eco))

def calcul_de_prix():
   if(drop.get() == ''):
      messagebox.showerror(title = "Error", message = "Please select an energy source!")
   else:
      if(kw.get() == ''):
         kw.set(str(Prix_du_kw[drop.get()]))
      if(coef.get() == ''):
         coef.set(str(Coef_De_Charge[drop.get()]))
      if(duree.get() == ''):
         duree.set(str(Duree_De_Vie[drop.get()]))
      if(taux.get() == ''):
         taux.set(str(taux_croiss_eco))
      try:
         prix_kw=(float(kw.get())/(365*24*float(coef.get())*float(duree.get())))
         facteur=(1-(1/(1+float(taux.get()))**31))/float(taux.get())
         prix_kwh=prix_kw*facteur
         prix['text'] = str("%.3f" %prix_kwh)
      except ZeroDivisionError:
         messagebox.showerror('Division par 0', message =  "La durée de vie ne peut pas etre nulle!")

def reset():
   drop.set('')
   kw.set('')
   coef.set('')
   duree.set('')
   taux('')


#ComboBox
select = Label(root,text = 'Please select your energy source: ', font = 'arial', bg = 'white').grid(row = 1, column = 0, sticky = 'w')
drop = ttk.Combobox(root, width = 27, values = ["Photovoltaique","CSP","Dechets","Eolienne offshore"], state = "readonly" )
drop.grid(row = 1, column = 2, columnspan = 2)
drop.bind('<<ComboboxSelected>>', Button)

#variable
duree = StringVar()
kw = StringVar()
coef = StringVar()
taux = StringVar()

#Input labels
kw_input = tk.Entry(root, width = 30, textvariable = kw).grid(row = 2, column = 2, columnspan = 2)
coef_input = tk.Entry(root, width = 30, textvariable = coef).grid(row = 3, column = 2, columnspan = 2)
duree_input = tk.Entry(root, width = 30, textvariable = duree).grid(row = 4, column = 2, columnspan = 2)
taux_input = tk.Entry(root, width = 30, textvariable = taux).grid(row = 5, column = 2, columnspan = 2)

#buttons
button = ttk.Button( root , text = "Calcul", command = calcul_de_prix ).grid(row = 6, column = 3)
reset_btn = ttk.Button(root, text = "Reset", command = reset).grid(row = 6, column = 2)


root.mainloop()
