matrics=[[3,4,4,4,4,0],
         [3,2,3,4,5,6],
         [3,1,4,3,5,6],
         [3,0,0,1,5,6],
         [3,1,1,0,5,6],
         [3,1,5,0,0,5],
         [1,3,4,5,0,0]]
find_four =[99] #a dummy insertion to check only for minimum then this
count_of_lookup=1
# track on x-axis
def track_east( lookup, this_column, one_dim_array ):
    global count_of_lookup
    if count_of_lookup == 4 :
        count_of_lookup=1
        return True
    elif one_dim_array[this_column+1] == lookup:
        count_of_lookup+=1
        return track_east( lookup, this_column+1, one_dim_array)
    else:
        count_of_lookup=1
        return False

# to track in vertical direction 
def track_south(lookup , this_row, this_column, matrics):
    global count_of_lookup
    if count_of_lookup ==4:
        count_of_lookup =1
        return True
    elif matrics[this_row+1][this_column] == lookup:
        count_of_lookup +=1
        return track_south(lookup , this_row+1, this_column ,matrics)
    else:
        count_of_lookup=1
        return False

# ^ North west
def track_north_west(lookup, this_row, this_column, matrics):
    # print('debugger NWEST')
    global count_of_lookup
    if count_of_lookup ==4:
        count_of_lookup =1
        return True
    elif matrics[this_row -1][this_column -1] ==lookup:
        count_of_lookup+=1
        return track_north_west(lookup,this_row-1, this_column-1, matrics)
    else:
        count_of_lookup =1
        return False

# ^North east 
def track_north_east(lookup, this_row, this_column, matrics):
    # print('debugger NEST')
    global count_of_lookup
    if count_of_lookup ==4:
        count_of_lookup =1
        return True
    elif matrics[this_row-1][this_column+1] ==lookup:
        count_of_lookup+=1
        return track_north_east(lookup,this_row-1, this_column+1, matrics)
    else:
        count_of_lookup =1
        return False

# South west
def track_south_west(lookup, this_row, this_column, matrics):
    # print('debugger sWEST')
    global count_of_lookup
    if count_of_lookup ==4:
        count_of_lookup =1
        return True
    elif matrics[this_row+1][this_column-1] ==lookup:
        count_of_lookup+=1
        return track_south_west(lookup,this_row+1, this_column-1, matrics)
    else:
        count_of_lookup =1
        return False

# South East
def track_south_east(lookup, this_row, this_column, matrics):
    # print('debugger SEST')
    global count_of_lookup
    if count_of_lookup == 4:
        count_of_lookup = 1
        return True
    elif matrics[this_row+1][this_column+1] ==lookup:
        count_of_lookup+=1
        return track_south_east(lookup,this_row+1, this_column+1, matrics)
    else:
        count_of_lookup =1
        return False

def main():
    for i in range(0,len(matrics)): # rows
        for j in range(len(matrics[i])): # cols
            pick = matrics[i][j]
            flag=True
            if pick not in find_four and pick < min(find_four): # check presence of find_four 
                if flag and len(matrics[i]) -j >=3: # for horizontal traversal check horizontal direction me atleast me 4 element h ?
                    if track_east(pick, j, matrics[i])  !=False :
                        find_four.append(pick)
                        flag = False
                        continue
                if flag and len(matrics) - i >=3: # for vertical traversal check vertical direction
                                # has atleast 4 element
                    if track_south(pick, i , j, matrics) !=False:
                        find_four.append(pick)
                        flag = False
                        continue
                if flag and j >=3 and i >=3:
                    if track_north_west(pick, i, j, matrics) != False:
                        find_four.append(pick)
                        flag = False
                        continue
                if flag and (len(matrics[i]) - j )>=3 and i >=3:
                    if track_north_east(pick, i, j, matrics) !=False:
                        find_four.append(pick)
                        flag =False
                        continue
                if flag and (len(matrics) - i )>= 3 and j >=3 :
                    if track_south_west( pick , i, j,matrics) !=False:
                        find_four.append(pick)
                        flag =False
                        continue
                if flag and ((len(matrics) - i) >= 4 and (len(matrics[i]) - j) >=3) :
                    if track_south_east(pick, i , j, matrics) != False:
                        find_four.append(pick)
                
    
main()

print (min(find_four)) if len(find_four) >1 else print(-1)