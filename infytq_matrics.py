matrics=[[3,2,2,2,2,0],
         [3,2,3,4,5,6],
         [1,2,4,3,5,6],
         [1,0,4,5,5,6],
         [1,1,0,1,5,6],
         [1,0,5,0,5,5],
         [0,3,4,5,0,6]]
find_four =[99] #a dummy insertion to check only for minimum then this
count_of_lookup=1
def track_horizontal( lookup, this_column, one_dim_array ):
    # to do something
    global count_of_lookup
    if count_of_lookup == 4 :
        print(lookup,'track_horizotal --> track-->if')
        count_of_lookup=1
        return lookup
    elif one_dim_array[this_column+1] == lookup:
        count_of_lookup+=1
        print(lookup,'track_horizotal --> track-->elif (1)' ,count_of_lookup)
        return track_horizontal( lookup, this_column+1, one_dim_array)
    else:
        print(lookup,'track_horizotal --> track-->last else --> return False')
        count_of_lookup=1
        return False

# to track in vertical direction 
def track_vertical(lookup , this_row, this_column, matrics):
    global count_of_lookup
    print('track_vertical')
    if count_of_lookup ==4:
        print('track_vertical -->if')
        count_of_lookup =1
        return lookup
    elif matrics[this_row+1][this_column] == lookup:
        count_of_lookup +=1
        print(lookup,'track_vertical --> else(1)' , count_of_lookup)
        return track_vertical(lookup , this_row+1, this_column ,matrics)
    else:
        print(lookup ,'track_vertical --> last else --> return False')
        count_of_lookup=1
        return False

def track_diagonal(lookup , this_row, this_column , matrics):
    #plese write ur logic here
    pass

def main():
    for i in range(0,len(matrics)):
        for j in range(len(matrics[i])):
            pick = matrics[i][j]
            if pick not in find_four and pick < min(find_four): # check presence of find_four 
                if len(matrics[i]) -j >=4: # for horizontal traversal check horizontal direction me atleast me 4 element h ?
                    variable = track_horizontal(pick, j, matrics[i]) 
                    if variable !=False:
                        find_four.append(pick)
                    else:
                        if len(matrics) - i >=4: # for vertical traversal check vertical direction
                                # has atleast 4 element
                            variable = track_vertical(pick, i , j, matrics)
                            if variable !=False:
                                find_four.append(pick)
                            else:
                                variable = track_diagonal( pick, i, j, matrics)



    print('min of find_four' , min(find_four))
    
main()