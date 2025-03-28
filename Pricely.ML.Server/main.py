import tkinter as tk
from tkinter import ttk
import sv_ttk
import numpy as np
from sklearn.linear_model import LinearRegression


root = tk.Tk()
sv_ttk.set_theme("dark")

root.title("Pricely Desktop")
root.iconphoto(True, tk.PhotoImage(file="Pricely.ML.Server/assets/pricely.png"))
#Rows
root.grid_rowconfigure(0, weight=1)  
root.grid_rowconfigure(1, weight=1)  

#Columns
root.grid_columnconfigure(0, weight=1) 
root.grid_columnconfigure(1, weight=1)  

#Input Panel
input_frame = ttk.Frame(root)
input_frame.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="ew")

#Price List
inputs = [3879, 3949, 3649, 3949, 3925, 3949,3390,3949,3649,3739,3637,3549 ]


price_input = ttk.Entry(input_frame, width=30)
price_input.pack(padx=20, pady=5)


def add_input():
    price = price_input.get()
    if price:  
        inputs.append(price)
        price_input.delete(0, tk.END)  
        update_table()

add_button = ttk.Button(input_frame, text="Add Price", width=20, command=add_input)
add_button.pack(pady=10)

columns = ("Price History")
price_table = ttk.Treeview(root, columns=columns, show="headings")
price_table.grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="ew")


def update_table():
    for row in price_table.get_children():
        price_table.delete(row)
    
    for price in inputs:
        price_table.insert("", "end", values=(price,))



def predict_next_price():
    if len(inputs) < 2:
        print("Not enough data to predict.")
        return
    
    
    x = np.array(range(len(inputs))).reshape(-1, 1) 
    y = np.array(inputs, dtype=np.float16)  
    
    
    model = LinearRegression()
    model.fit(x, y)
    
    next_index = len(inputs) 
    predicted_price = model.predict([[next_index]]) 
    
    print(f"Next Price: {predicted_price[0]}")



predict_button = ttk.Button(root, text="Predict Next Price", width=20, command=predict_next_price)
predict_button.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
