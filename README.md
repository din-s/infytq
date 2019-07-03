# infytq
june 21
the one of the two question asked was:
Accept input length of list say m
then each next m lines contains a list containing n integers 

thus after taking these input we have a m * n matrix 
where number of rows = m and 
number of columns = n (may be fixed they didn't mentioned explicitly about 'n')

for eg : when m = 7 
 say matrics =[[3,2,2,2,2,0],
               [3,2,3,4,5,6],
               [1,2,4,3,5,6],
               [1,0,4,5,5,6],
               [1,1,0,1,5,6],
               [1,0,5,0,5,5],
               [0,3,4,5,0,6]]

thus our task is to find the minimum number which is repeated consecutively either in row , column or diagonal
here we have 1,5 and 6 which are repeated in vertical line for consecutively 4 times , 2 is repeated in horizontal sense and 0 is repeated in diagonal sense.

thus we have to return / print the element which is minimum amongst {0, 1, 2, 5, 6} here answer =0
if no such element exist which repeats for 4 consecutive times then return / print answer = -1

And we had to code from scratch in Infyq examination right from taking input to delivering correct answer unfotunately I was not able to do in given time there.
So I tried for traversing in horizontal and vertical direction and I am working to search element in diagonal direction as well, so to keep this version safe I had used this repository!!!

peek in code if you want the answer so far (horizontal + vertical)!
