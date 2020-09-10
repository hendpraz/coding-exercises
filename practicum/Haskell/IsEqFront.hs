isEmpty :: [Char] -> Bool
-- isEmpty(li) true jika list of integer li kosong
-- REALISASI
isEmpty li = null li

isEqFront :: [Char] -> [Char] -> Bool

--REALISASI
isEqFront t1 t2 
  | (isEmpty t1) = True --basis
  | (head t1) /= (head t2) = False
  | otherwise = isEqFront (tail t1) (tail t2) --rekurens