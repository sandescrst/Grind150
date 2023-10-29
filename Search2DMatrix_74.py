def searchMatrix(target, matrix):
     row, col = len(matrix), len(matrix[0])

     left, right = 0, row - 1
    #  print(right)

     while left <= right:
          mid = (left + right)//2
          if target > matrix[mid][-1]:
               left = mid+1
            #    print(left)
          elif target < matrix[mid][0]:
               right = mid -1
            #    print(right)
          else:
               break
     print(left, right)
     if not (left <= right):
          return False
     print(left, right)
     right_matrix = (left+right)//2
     l,r = 0,len(matrix[right_matrix])-1
     print(r, "hello")
     while l< r:
          mid = (l+r)//2
          if target > matrix[right_matrix][mid]:
               l = mid+1
          elif target < matrix[right_matrix][mid]:
               r = mid -1
          else:
               return True
     return False
print(searchMatrix(3,[[1,3,5,7],[10,11,16,20],[23,30,34,60]]))