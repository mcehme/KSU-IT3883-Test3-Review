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
# # mydict.remove("key")
# # mydict.pop("key")
# # mydict.popitem()
# # del mydict["key"]

# print(mydict)

# #4
# mydict = {"key", "value"}
# # mydict["key"] = "value2"
# # mydict.set("key", "value3")
# # mydict.setdefault("key", "value3")
# print(mydict)

# #5
# key = "key"
# mydict = dict()

# # value = mydict[key]

# # if key in mydict:
# #     value = mydict[key]
# # else:
# #     value = None

# # value = mydict.get(key)

# # value = mydict.get(key,None)

# #6
# mydict = dict()

# # mydict["key1"] = mydict["key1"] + 1

# # mydict["key1"] = mydict.get("key1", 0) + 1

# # if "key1" in mydict:
# #     mydict["key1"] = mydict["key1"] + 1
# # else: 
# #     mydict["key1"] = 1

# #7
# myset = {"value1"}
# myset.add("value2")
# print(myset)

# #8
# myset = set()
# print(set)

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

