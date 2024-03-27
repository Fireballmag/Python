from tkinter import *
import tkinter.messagebox as mb

window = Tk()
window.title("Сортировка")

def mergeSort(nums): # сортировка слиянием 
    if len(nums) == 1:
        return nums
    mid = (len(nums) - 1) // 2
    lst1 = mergeSort(nums[:mid + 1])
    lst2 = mergeSort(nums[mid + 1:])
    result = merge(lst1, lst2)
    return result
    
def merge(lst1, lst2):
    lst = []; i = 0; j = 0
    while(i <= len(lst1) - 1 and j <= len(lst2) - 1):
        if lst1[i] < lst2[j]:
            lst.append(lst1[i])
            i += 1
        else:
            lst.append(lst2[j])
            j += 1
    if i > len(lst1) - 1:
        while(j <= len(lst2) - 1):
            lst.append(lst2[j])
            j += 1
    else:
        while(i <= len(lst1) - 1):
            lst.append(lst1[i])
            i += 1
    return lst

def BinarySearch(lys, val): # бинарный поиск
    first = 0; last = len(lys) - 1; index = - 1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if lys[mid] == val:
            index = mid
        else:
            if val < lys[mid]:
                last = mid - 1
            else:
                first = mid + 1
    return index

def clicked_sort():
    arr = txt1.get()
    arr = mergeSort(arr)
    lbl.configure(text = "Отсартированный список: " + ''.join(arr))
    
def clicked_search():
    search = txt2.get()
    arr = txt1.get(); arr = mergeSort(arr)
    check = BinarySearch(arr, search)
    if(check == -1):
        mb.showinfo("Поиск буквы", "Ничего не найдено!")
    else:
        mb.showinfo("Поиск буквы", "Букавка имеется в строке!")
    


txt1 = Entry(window, width = 20); txt1.grid(row = 1, column = 0)
btn1 = Button(window, text = "Сортировать", command = clicked_sort); btn1.grid(row = 1, column = 1)
lbl = Label(window, text = "Отсартированный список: "); lbl.grid(row = 2, column = 0)
txt2 = Entry(window, width = 20); txt2.grid(row = 3, column = 0)
btn2 = Button(window, text = "Поиск", command = clicked_search); btn2.grid(row = 3, column = 1)
window.mainloop()