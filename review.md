# Test 3 Review

## Dictionaries and Sets

1. What does the following line of code print out?

    ```python
    mystery = {}
    print(type(mystery))
    ```
    - a:
    ```python
    <class 'dict'>
    ```
    - b:
    ```python
    <class 'set'>
    ```
    - c: 
    ```python
    # the code errors out
    ```
2. Select all of the valid ways to create an empty dictionary
    - a:
    ```python
    mydict = dict()
    ```
    - b:
    ```python
    mydict = {}
    ```
    - c:
    ```python
    mydict = dict.fromkeys(())
    ```
    
3. Select all of the valid ways to remove a key-value pair from a dictionary given the following set up:

    ```python
    mydict = {"key":"value", "other":"stuff"}
    ```
    - a: 
    ```python
    mydict.remove("key")
    ```
    - b:
    ```python
    mydict.pop("key")
    ```
    - c:
    ```python
    mydict.popitem()
    ```
    - d:
    ```python
    del mydict["key"]
    ```
4. Select all the valid ways to insert a key-value pair in the dictionary REGARDLESS of the contents of the dictionary.
    ```python
    mydict = {"key", "value"}
    ```
    - a:
    ```python
    mydict["key"] = "value2"
    ```
    - b:
    ```python
    mydict.set("key", "value3")
    ```
    - c:
     ```python
    mydict.setdefault("key", "value3")
    ```
5. Select all the valid ways to retrieve a key-value pair from the dictionary in a manner guaranteed not to raise an exception.

    - a:
    ```python
    value = mydict[key]
    ```
    - b:
    ```python
    if key in mydict:
        value = mydict[key]
    else:
        value = None
    ```
    - c:
    ```python
    value = mydict.get(key)
    ```
    - d:
    ```python
    value = mydict.get(key,None)
    ```
6. You have a dictionary where the values are the counts of the keys [This is a very common pattern]. How do you update the dictionary given a key that may or may not be new?
    ```python
    mydict = dict()
    ```
    - a:
    ```python
    mydict["key1"] = mydict["key1"] + 1
    ```
    - b:
    ```python
    mydict["key1"] = mydict.get("key1", 0) + 1
    ```
    - c:
    ```python
    if "key1" in mydict:
        mydict["key1"] = mydict["key1"] + 1
    else: 
        mydict["key1"] = 1
    ```
7. True or False: Sets are immutable?

    ```python
    True
    ```
    ```python
    False
    ```
8. What will the following print out?
    ```python
    myset = set()
    print(set)
    ```

    - a:
    ```python
    {}
    ```
    - b:
    ```python
    {()}
    ```
    - c:
    ```python
    set()
    ```
9. Which of the following converts a  dictionary to a set such that the key value pairs are now tuples?
    ```python
    mydict = {"key1":"value1","key2":"value2"}
    ```
    - a:
    ```python
    myset = set(mydict)
    ```
    - b:
    ```python
    myset = set(mydict.items())
    ```
    - c:
    ```python
    myset = set().update(mydict)
    ```
    - d:
    ```python
    myset = set()
    myset.update(mydict.items())
    ```
    - e:
    ```python
    myset = {(key, value) for key, value in mydict.items()}
    ```
10. What will the following code do:
    ```python
    myset = set([1,2,3])
    myset.remove(4)
    ```
    - a:
    ```python
    # do nothing
    ```
    - b:
    ```python
    # throw an error
    ```


11. How do you find all values in set a but not in set b?
    ```python
    a = {1,2,3,4,5}
    b = {4,5,6,7,8,9,10}
    ```
    - a:
    ```python
    ans = a.difference(b)
    ```
    - b:
    ```python
    ans = a.difference_update(b)
    ```
    - c:
    ```python
    ans = a - b
    ```
12. Reference time!
    - a: Union: set of all elements in either set a OR set b
    ```python
    ans = a | b
    ans = a.union(b)
    a.update(b) # not a.union_update(b)! updates a with all values in b
    ```
    - b: Intersection: the set of all elements in set a AND set set b
    ```python
    ans = a & b
    ans = a.intersection(b)
    a.intersection_update(b)#updates a such that a contains only the values previously in both a and b.
    ```
    - c: Symmetric difference: the set of all elements that are not in the intersection of A and B. i.e. the set of all elements that are either in A OR B but NOT BOTH.
    ```python
    ans = a ^ b
    ans = a.symmetric_difference(b)
    a.symmetric_difference(b) # sets a to be the symmetric_difference of the original a and b
    ```
    - d: other good to know methods
    ```python
    a.isdisjoint(b) # do a and b contain unique values
    a.issubset(b) # are all values in a also in b
    a.issuperset(b)# are all values in b also in a
    element = a.pop()# removes a "random" element from the set. Random meaning order defined by hash order (outside the scope of this class).
    a.discard(element) # removes the given element from the set. If the element is not present. It does not throw an error.
    ```
### The following is substantially the same for both dictionaries and sets
13. What will  the following output?
    ```python
    mylist1 = [1,2,3]
    mylist2 = [4,5,6]
    mydict1 = {"key1":mylist1, "key2":mylist2}
    mydict2 = mydict1.copy()
    mylist1.append(4)
    mylist2 = []
    mydict2["key2"] += [7]
    print(mydict1)
    print(mydict2)
    ```
    - a:
    ```python
    {'key1': [1, 2, 3], 'key2': [4, 5, 6]}
    {'key1': [1, 2, 3], 'key2': [4, 5, 6, 7]}
    ```
    - b:
    ```python
    {'key1': [1, 2, 3, 4], 'key2': [4, 5, 6]}
    {'key1': [1, 2, 3], 'key2': [4, 5, 6, 7]}
    ```
     - c:
    ```python
    {'key1': [1, 2, 3, 4], 'key2': [7]}
    {'key1': [1, 2, 3, 4], 'key2': [7]}
    ```
    - d:
    ```python
    {'key1': [1, 2, 3, 4], 'key2': [4, 5, 6, 7]}
    {'key1': [1, 2, 3, 4], 'key2': [4, 5, 6, 7]}
    ```
    - e:
    ```python
    # The code errors out
    ```

14. What will the following output?
    ```python
    myset = set([1,2,3,4,5])
    myset.clear()
    print(myset)
    ```
    - a:
    ```python
    set()
    ```
    - b:
    ```python
    {1, 2, 3, 4, 5}
    ```
    - c:
    ```python
    # The code throws an error
    ```
## Tkinter/GUIs

15. The following is the minimal code needed to create a window using tkinter.
    ```python
    import tkinter as tk
    root = tk.Tk()
    tk.mainloop()
    ```
    - a:
    ```python
    True
    ```
    - b:
    ```python
    False
    ```
16. An introduction to pack(). What will the result be?
    ```python
    import tkinter as tk
    root = tk.Tk()
    button1 = tk.Button(root, text="Button 1")
    button1.pack()
    button2 = tk.Button(root, text="Button 2")
    button2.pack()
    button3 = tk.Button(root, text="Button 3")
    button3.pack()
    tk.mainloop()
    ```
    - a:
    ```python
    # Buttons arranged top to bottom. On expansion, they stay vertically and horizontally centered.
    ```
    - b:
    ```python
    # Buttons arranged top to bottom. On expansion, they stay vertically centered but do not adjust horizontally.
    ```
    - c:
    ```python
    # Buttons arranged top to bottom. On expansion, they stay horizontally centered but do not adjust vertically.
    ```
    - d:
    ```python
    #Buttons arranged top to bottom. On expansion, they do not adjust at all.
    ```
17. What will the result be?
    ```python
    import tkinter as tk
    root = tk.Tk()
    button1 = tk.Button(root, text="Button 1")
    button1.pack(expand=tk.YES)
    button2 = tk.Button(root, text="Button 2")
    button2.pack(expand=tk.YES)
    button3 = tk.Button(root, text="Button 3")
    button3.pack(expand=tk.YES)
    tk.mainloop()
    ```
    - a:
    ```python
    #The buttons now cover the entire window space.
    ```
    - b:
    ```python
    #The buttons now adjust both vertically and horizontally when the window expands.
    ```

18. What will the result be?
    ```python
    import tkinter as tk
    root = tk.Tk()
    button1 = tk.Button(root, text="Button 1")
    button1.pack(fill=tk.BOTH)
    button2 = tk.Button(root, text="Button 2")
    button2.pack(fill=tk.BOTH)
    button3 = tk.Button(root, text="Button 3")
    button3.pack(fill=tk.BOTH)
    tk.mainloop()
    ```
    - a:
    ```python
    #The buttons now cover the entire window space.
    ```
    ```python
    #The buttons now stretch to cover the width of the horizontal space, but they do not stretch to cover the width of the vertical space.
    ```
19. What will the result be?
    ```python
    import tkinter as tk
    root = tk.Tk()
    button1 = tk.Button(root, text="Button 1")
    button1.pack(expand=tk.YES, fill=tk.BOTH)
    button2 = tk.Button(root, text="Button 2")
    button2.pack(expand=tk.YES, fill=tk.BOTH)
    button3 = tk.Button(root, text="Button 3")
    button3.pack(expand=tk.YES, fill=tk.BOTH)
    tk.mainloop()
    ```
    - a:
    ```python
     #The buttons now cover the entire window space.
    ```
    - b:
    ```python
    #The code errors: You cannot have both expand and fill set.
    ```
20. Let's get crazy!
    ```python
    import tkinter as tk
    root = tk.Tk()
    button1 = tk.Button(root, text="Button 1")
    button1.pack(side=tk.BOTTOM expand=tk.YES)
    button2 = tk.Button(root, text="Button 2")
    button2.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)
    button3 = tk.Button(root, text="Button 3")
    button3.pack(side=tk.right)
    tk.mainloop()
    ```

    - a:
    ```python
    #button 1 stays the same size but adjusts location. Button 2 grows both vertically and horizontally when the window size increases. Button 3 remains the same size at all times.
    ```
    - b:
    ```python
    # button 1 is "greedy" and claims most of the space even though it does not fill it. Thus it stays the same size but adjusts location. Since button 2 is on a different axis it doesn't fight button1 for vertical space and  thus only expands horizontally. Button 3 remains the same size at all times.
    ```
21. Moving on to grid!
    


        




