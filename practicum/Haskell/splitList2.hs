isEmpty :: [Int] -> Bool
-- isEmpty(li) true jika list of integer li kosong
-- REALISASI
isEmpty li = null li

isOneElmt :: [Int] -> Bool
isOneElmt li = (length li) == 1

splitList :: [Int] -> ([Int],[Int])

splitList li =
  if (isEmpty li) then ([],[])
  else if (isOneElmt x) then (x,[])
  else
  	let
  	  temp1 = tail x
  	  temp2 = init temp1
  	  (m,n) = splitList(tmp2)
  	  in
  	    (konso (head x) m, konsdot n (last x))