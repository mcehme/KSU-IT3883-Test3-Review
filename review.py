# #1
# mystery = {}
# print(type(mystery))

# #2
# mydict1 = dict()
# mydict2 = {}
# mydict3 = dict.fromkeys(())
# print(mydict1, mydict2, mydict3)

# #3
# mydict = {"key":"value", "other":"stuff"}
# mydict.remove("key")
# mydict.pop("key")
# mydict.popitem()
# del mydict["key"]

# print(mydict)

# #4
# mydict = {"key": "value"}
# # mydict["key"] = "value2"
# # mydict.set("key", "value3")
# mydict.setdefault("key", "value3")
# print(mydict)

# #5
# key = "key"
# mydict = dict()

# # value = mydict[key]

# # if key in mydict:
# #     value = mydict[key]
# # else:
# #     value = None

# value = mydict.get(key)

# # value = mydict.get(key,0)
# print(value)

# #6
# mydict = dict()

# # mydict["key1"] = mydict["key1"] + 1

# # mydict["key1"] = mydict.get("key1", 0) + 1

# # if "key1" in mydict:
# #     mydict["key1"] = mydict["key1"] + 1
# # else: 
# #     mydict["key1"] = 1

# # #7
# myset = {"value1"}
# myset.add("value2")
# print(myset)

# #8
myset = set()
print(myset)

# #9
# mydict = {"key1":"value1","key2":"value2"}
# # myset = set(mydict)
# # myset = set(mydict.items())
# # myset = set().update(mydict)
# # myset = set()
# # myset.update(mydict.items())
# # myset = {(key, value) for key, value in mydict.items()}
# print(myset)

# #10
# myset = set([1,2,3])
# # myset.remove(4)
# # myset.discard(4)

# #11
# a = {1,2,3,4,5}
# b = {4,5,6,7,8,9,10}
# # ans = a.difference(b)
# # ans = a.difference_update(b)
# # ans = a - b


# #13
# mylist1 = [1,2,3]
# mylist2 = [4,5,6]
# mydict1 = {"key1":mylist1, "key2":mylist2}
# mydict2 = mydict1.copy()
# mylist1.append(4)
# mylist2 = []
# mydict2["key2"] += [7]
# print(mydict1)
# print(mydict2)

# #14
# myset = set([1,2,3,4,5])
# myset.clear()
# print(myset)

# #15
# import tkinter as tk
# root = tk.Tk()
# tk.mainloop()

# #16
# import tkinter as tk
# root = tk.Tk()
# button1 = tk.Button(root, text="Button 1")
# button1.pack()
# button2 = tk.Button(root, text="Button 2")
# button2.pack()
# button3 = tk.Button(root, text="Button 3")
# button3.pack()
# tk.mainloop()

# #17
# import tkinter as tk
# root = tk.Tk()
# button1 = tk.Button(root, text="Button 1")
# button1.pack(expand=tk.YES)
# button2 = tk.Button(root, text="Button 2")
# button2.pack(expand=tk.YES)
# button3 = tk.Button(root, text="Button 3")
# button3.pack(expand=tk.YES)
# tk.mainloop()

# # 18
# import tkinter as tk
# root = tk.Tk()
# button1 = tk.Button(root, text="Button 1")
# button1.pack(fill=tk.BOTH)
# button2 = tk.Button(root, text="Button 2")
# button2.pack(fill=tk.BOTH)
# button3 = tk.Button(root, text="Button 3")
# button3.pack(fill=tk.BOTH)
# tk.mainloop()

# #19
# import tkinter as tk
# root = tk.Tk()
# button1 = tk.Button(root, text="Button 1")
# button1.pack(expand=tk.YES, fill=tk.BOTH)
# button2 = tk.Button(root, text="Button 2")
# button2.pack(expand=tk.YES, fill=tk.BOTH)
# button3 = tk.Button(root, text="Button 3")
# button3.pack(expand=tk.YES, fill=tk.BOTH)
# tk.mainloop()

# #20
# import tkinter as tk
# root = tk.Tk()
# button1 = tk.Button(root, text="Button 1")
# button1.pack(side=tk.BOTTOM, expand=tk.YES)
# button2 = tk.Button(root, text="Button 2")
# button2.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
# button3 = tk.Button(root, text="Button 3")
# button3.pack(side=tk.RIGHT)
# tk.mainloop()

# #21
# import tkinter as tk
# root = tk.Tk()
# button1 = tk.Button(root, text="Button 1")
# button1.grid(row=0, column=0)
# button2 = tk.Button(root, text="Button 2")
# button2.grid(row=1, column=1)
# button3 = tk.Button(root, text="Button 3")
# button3.grid(row=2, column=2)
# tk.mainloop()

# # 22
# import tkinter as tk
# root = tk.Tk()
# button1 = tk.Button(root,text="Button1")
# button1.grid(row=0,column=0,columnspan=3)
# button2 = tk.Button(root, text="Button 2")
# button2.grid(row=1, column=1,)
# button3 = tk.Button(root, text="Button 3")
# button3.grid(row=2, column=2)
# tk.mainloop()

# #22 corrected
# import tkinter as tk
# root = tk.Tk()
# button1 = tk.Button(root,text="Button1")
# button1.grid(row=0,column=0,columnspan=3,sticky='EW')
# button2 = tk.Button(root, text="Button 2")
# button2.grid(row=1, column=1, sticky='EW')
# button3 = tk.Button(root, text="Button 3")
# button3.grid(row=2, column=2, sticky='EW')
# root.columnconfigure(0, minsize=100)
# root.columnconfigure(1, minsize=100)
# root.columnconfigure(2, minsize=100)
# tk.mainloop()


# # 23
# import tkinter as tk
# root = tk.Tk()
# button1 = tk.Button(root,text="Button1")
# button1.pack()
# button2 = tk.Button(root, text="Button 2")
# button2.grid(row=0,column=1)
# tk.mainloop()

# # 24
# import tkinter as tk
# root = tk.Tk()
# button1 = tk.Button(root,text="Button1")
# button1.place(relx=0.5, rely=0.5, anchor="center")
# tk.mainloop()

# #25
# import tkinter as tk
# root = tk.Tk()
# button1 = tk.Button(root,text="Button1")
# button1.place(x=50, y=50, anchor="center")
# tk.mainloop()

# #26
# import tkinter as tk
# root = tk.Tk()
# button1 = tk.Button(root,text="Button1")
# button1.place(relx=1, rely=0.5, anchor="e")
# button2 = tk.Button(root,text="Button2")
# button2.pack(side=tk.LEFT)
# tk.mainloop()

# # 27
# import tkinter as tk
# root = tk.Tk()
# button1 = tk.Button(root, text="Button1")
# button1.configure(command=lambda:print("button clicked"))
# button1.pack()
# tk.mainloop()

# # 28
# import tkinter as tk
# root = tk.Tk()
# mystr = tk.StringVar()
# mystr.set("This is a label")
# label = tk.Label(root,textvariable=mystr)
# label.pack()
# button = tk.Button(root,text="button",command=lambda:mystr.set("Clicked Button"))
# button.pack()
# tk.mainloop()

# # 29
# import tkinter as tk
# root = tk.Tk()
# textbox = tk.Text(root, height=1, width=20)
# textbox.pack()
# button = tk.Button(root, text="click me",command=lambda:print(textbox.get(1.0,"end-1c")))
# button.pack()
# tk.mainloop()

# # 30 - two different approaches
# import tkinter as tk
# root = tk.Tk()
# mystr = tk.StringVar()
# entry  = tk.Entry(root,textvariable=mystr)
# entry.pack()
# button = tk.Button(root, text="click me",command=lambda:print(mystr.get()))
# button2 = tk.Button(root, text="a different approach", command=lambda:print(entry.get()))
# button.pack()
# button2.pack()
# tk.mainloop()
