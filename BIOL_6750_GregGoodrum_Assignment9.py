# Author: Greg Goodrum
# Course: BIOL 6750 with Dr. Will Pearse
# Section: 9 - Sorting Alogrithms
# Exercise 9
# ----------------


# ---- Bubblesort ----
testlist = [5,7,2,10,4,7,9,1]
value_bottom=testlist[0]
value_top=testlist[-1]
index_top = len(testlist)-1
index_bottom = testlist[0]


# Layout
# 1. Cycle through pairs of numbers, starting with the lowest indexed two
# 2. Swap such that greatest of the two numbers is on top
# 3. Repeat moving up the list until you have compared every pair of numbers once
# 4. This represents on pass
# 5. On second pass, repeat for every number that is not the top of the list
# 6. Repeat until there are no pairs left to sort


testlist = [5,7,2,10,4,7,9,1]
def bubblesort(list):
    # For every value in the list
    for i in range(len(list)-1):
        # Compare each value from previous clause to each remaining value in the list.
        for j in range(len(list)-1-i):
            # If the current value is greater than the next value
            if list[j] > list[j+1]:
                # Swap the values
                list[j], list[j+1] = list[j+1], list[j]
            print(list)
    #Once all individual items have been compared, return the result
    print("Finished Bubblesort")
    return list


print(bubblesort([5,7,2,10,4,7,9,1]))



# ---- QuickSort ----
# determine syntax to define each input (list, bottom, top)
testlist = [5,7,2,10,4,7,9,1,6]
value_bottom = testlist[0]
value_top=testlist[-1]
index_top = len(list)-1
index_bottom = 0


# For every pass, the pivot is going to segment the list into what has been sorted and what hasn't
# Partition returns a single value, the index in the list of the sorted pivot point
# Then, when quicksort calls itself, it uses the returned pivot point to split the list into sections
def PARTITION(list, bottom, top):
    # Set pivot as the value of the last element in the list
    pivot = list[top]
    # Set bottom as the first index position in the list
    x = bottom
    # For ever index position from beginning to the last position before the pivot (len(list)-2)
    for i in range(bottom, top):
        # If the current value is less than or equal to the pivot
        if list[i] <= pivot:
            # Swap the current value to the bottom position
            list[i], list[x] = list[x], list[i]
            # Once the swap occurs, change the bottom position one index to the right so the value is locked in the less than section
            x = x+1
        # Next Step: Once everything has been sorted, switch the pivot to the bottom+1 position
        # end if
    # end for
    # Swap the pivot value from the end position the the value to the right of the last minimum value (list[x])
    list[top], list[x] = list[x], list[top]
    #Print index and alterations to list to verify results
    print(x)
    print(list)
    # Return x as the index of the pivot point in the re-ordered list.
    return x
#end function
testlist = [5,7,2,10,4,7,9,1,6]
PARTITION(testlist, 0, len(testlist)-1)


def QuickSort(list, bottom, top):
    # I will add the PARTITION function defined above once I have figured out the edge condition here
    # If index of bottom < index of top (i.e. if the list is larger than one value)
    if bottom < top:
        # Assign Pivot the index value returned in the PARTITION function
        pivot = PARTITION(list, bottom, top)
        # Call Quicksort on the section of list between the bottom value and the pivot
        QuickSort(list, bottom, pivot-1)
        # Call Quicksort on the section of list between the pivot and the top value
        QuickSort(list, pivot+1, top)
    # Define edge condition
    elif bottom >= top:
        return(list)
    #end if
#end function
import random
testlist = random.sample(range(1,100), 15)
QuickSort(testlist, 0, len(testlist)-1)


# ---- ALL MATERIAL BELOW THIS POINT IS FOR AUTHOR REFERENCE ONLY ----


# ---- Conditions from Source Material ----
def quicksortfunction(list, bottom, top):
    # Edge condition?
    if bottom < top:
        pivot = PARTITION(list,bottom,top)
        quicksortfunction(list, bottom, pivot-1)
        quicksort(list, pivot+1, top)
    end if
end function


def PARTITION(list, bottom, top):
    pivot = list[top]
    x = bottom
    for i in bottom-(top-1):
        if list[i] < pivot:
            SWAP(list[i], list[x])
            x = x+1
        end if
    end for
    return x
end function
# ---- END Source Material ----


# ---- PARTITION function reference ----


def PARTITION(list, bottom, top):
    # Set pivot as the value of the last element in the list
    pivot = list[top]
    # Set bottom as the first index position in the list
    x = bottom
    # For ever index position from beginning to the last position before the pivot (len(list)-2)
    for i in range(len(list)-1):
        # If the current value is less than or equal to the pivot
        if list[i] <= pivot:
            # Swap the current value to the bottom position
            list[i], list[x] = list[x], list[i]
            # Once the swap occurs, change the bottom position one index to the right so the value is locked in the less than section
            x = x+1
        # Next Step: Once everything has been sorted, switch the pivot to the bottom+1 position
        # end if
    # end for
    # Swap the pivot value from the end position the the value to the right of the last minimum value (list[x])
    list[len(list)-1], list[x] = list[x], list[len(list)-1]
    #Print index and alterations to list to verify results
    print(x)
    print(list)
    # Return x as the index of the pivot point in the re-ordered list.
    return x
#end function
testlist = [5,7,2,10,4,7,9,1,6]
PARTITION(testlist, 0, len(testlist)-1)




# ---- START PARTITION function with only list input ----
# This was my first functional version of partition, but
# I didn't realize how the bottom and top values interacted
# with the QuickSort function, so the complete version is
# above.

def PARTITION(list):
    # Set pivot as the value of the last element in the list
    pivot = list[-1]
    # Set bottom as the first index position in the list
    x = 0
    # For ever index position from beginning to the last position before the pivot (len(list)-2)
    for i in range(len(list)-1):
        # If the current value is less than or equal to the pivot
        if list[i] <= pivot:
            # Swap the current value to the bottom position
            list[i], list[x] = list[x], list[i]
            # Once the swap occurs, change the bottom position one index to the right so the value is locked in the less than section
            x = x+1
        # Next Step: Once everything has been sorted, switch the pivot to the bottom+1 position
        # end if
    # end for
    # Swap the pivot value from the end position the the value to the right of the last minimum value (list[x])
    list[len(list)-1], list[x] = list[x], list[len(list)-1]
    #Print index and alterations to list to verify results
    print(x)
    print(list)
    # Return x as the index of the pivot point in the re-ordered list.
    return x
#end function
PARTITION([5,7,2,10,4,7,9,1,6])
