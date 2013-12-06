# list      : [(200, 111), (101, 123), (130, 234), (299, 9)  ]
# if sort by tuple(0): x=0
# after sort: [(101, 123), (130, 234), (200, 111), (299, 9)  ]
# if sort by tuple(1): x=1
# after sort: [(299, 9)  , (200, 111), (101, 123), (130, 234)]
def sort( aList, x ):
  RADIX = 10
  maxLength = False
  tmp , placement = -1, 1
  
  while not maxLength:
    maxLength = True
    # declare and initialize buckets
    buckets = [list() for _ in range( RADIX )]
 
    # split aList between lists
    for i in aList:
      tmp = i[x] / placement
      buckets[tmp % RADIX].append( i )
      if maxLength and tmp > 0:
        maxLength = False
 
    # empty lists into aList array
    a = 0
    for b in range( RADIX ):
      buck = buckets[b]
      for i in buck:
        aList[a] = i
        a += 1
 
    # move to next digit
    placement *= RADIX
    
  return aList
