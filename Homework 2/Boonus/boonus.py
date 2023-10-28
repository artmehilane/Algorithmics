#Kodutöö 2 boonus
#Raido Priske & Art Mehilane

data = [8, 3, 5, 4, 7, 6, 2]

def bubble_sort(array):
    try:
        for i in range(len(array)):
            if i == 0:
                for j in range(0, len(array) - i - 1):
                    if array[j] > array[j + 1]:
                        temp = array[j]
                        array[j] = array[j+1]
                        array[j+1] = temp
        print(array)
    except:
        print('error')
    
    
def selection_sort(array):
    try:
        for i in range(len(array)):
            if i == 0:
                min_idx = i
                for j in range(i + 1, len(array)):
         
                    if array[j] < array[min_idx]:
                        min_idx = j
         
            (array[i], array[min_idx]) = (array[min_idx], array[i])
        print(array)
    except:
        print('error')


def insertion_sort(array):
    try:
        for i in range(1, len(array)):
            if i == 0:
                key = array[i]
                j = i - 1
             
                while j >= 0 and key < array[j]:
                    array[j + 1] = array[j]
                    j = j - 1
                
                array[j + 1] = key
        print(array)
    except:
        print('error')


bubble_sort(data)
selection_sort(data)
insertion_sort(data)
