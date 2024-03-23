#Sangeethan Thevathasan 100867103
#You have to install playsound in order to hear swap noise
from playsound import playsound
def mergesort(array):
    if len(array) > 1:
        middle = len(array)//2
        left = array[:middle]
        right = array[middle:]
        mergesort(left)
        mergesort(right)
        i=j=k=0
        
        while i<len(left) and j <len(right):
            if left[i]<right[j]:
                array[k]=left[i]
                i+=1
            else:
                array[k] = right[j]
                j+=1
                playsound("C:\\Users\\sange\\Desktop\\assign 2\\DSAassign2\\FAST.MP3")
            k+=1
            
        while i<len(left):
            array[k]=left[i]
            i+=1
            k+=1
            
        while j <len(right):
            array[k]=right[j]
            j+=1
            k+=1
        print("current",array)
        
if __name__ == "__main__":
    array = [12,15,12,100,86,54,32,21]
    mergesort(array)
    print(array)
