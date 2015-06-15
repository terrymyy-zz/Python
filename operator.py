# even_numbers = [2,4,6,8]
# odd_numbers = [1,3,5,7]
# all_numbers = odd_numbers + even_numbers
# print all_numbers
# print [1,2,3] * 3

##    x_list = [1,2,3,4,5,6,7,8,9,0]
##    y_list = [0,9,8,7,6,5,4,3,2,1]
##    big_list = x_list *10 + y_list*10
##    print big_list

# variables
x = object()
y = object()

# TODO: change this code
x_list = [x] * 10
y_list = [y] * 10
big_list = x_list + y_list

print "x_list contains %d objects" % len(x_list)
print "y_list contains %d objects" % len(y_list)
print "big_list contains %d objects" % len(big_list)

# testing code
if x_list.count(x) == 10 and y_list.count(y) == 10:
    print "Almost there..."
if big_list.count(x) == 10 and big_list.count(y) == 10:
    print "Great!"
