def binary_search1(a_list,item):
    ''' assumption is the a_list is sorted '''

    first = 0
    last = len(a_list) - 1

    while first <= last :
        mid = (first + last) // 2
        #print(mid)
        if a_list[mid] == item:
            return True
        elif  item  < a_list[mid]:
            last = mid - 1
        else:
            first = mid + 1
    return False




def binary_search2(a_list,item):
    ''' assumption is the a_list is sorted '''
    ''' recursive version '''

    if len(a_list) == 0:
        return False
    else:
        mid = len(a_list) // 2
        #print(mid)
        if a_list[mid] == item:
            return True
        elif  item  < a_list[mid]:
            return binary_search2(a_list[:mid],item)
        else:
            return binary_search2(a_list[mid + 1:],item)
            #return binary_search(a_list[mid + 1:],item)

def binary_search(start,end,item):
  alist = range(start,end)
  if len(alist) == 0 :
    #print(alist,start,end)
    return False
  else:
      mid =  (end - start)  // 2
      #print('total : %d - Start : %d, end : %d, Mid : %d'%(len(alist),start, end, mid))
      if item == alist[mid]:
          return True
      elif item < alist[mid]:
          return binary_search(start,mid+ start,item)
      else:
          return binary_search(start+mid,end,item)
