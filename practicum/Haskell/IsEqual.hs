module ListOfInteger where

isEmpty :: [Int] -> Bool
-- isEmpty(li) true jika list of integer li kosong
-- REALISASI
isEmpty li = null li

isEqual :: [Int] -> [Int] -> Bool

--REALISASI
isEqual t1 t2 
  | (isEmpty t1) && (isEmpty t2) = True --basis
  | (isEmpty t1) || (isEmpty t2) = False
  | (head t1) /= (head t2) = False
  | otherwise = isEqual (tail t1) (tail t2) --rekurens