module ListOfInteger where

isEmpty :: [Int] -> Bool
-- isEmpty(li) true jika list of integer li kosong
-- REALISASI
isEmpty li = null li

countIf :: [Int] -> (Int -> Bool) -> Int

--REALISASI
countIf l f
  | (isEmpty l) = 0 -- basis
  | (f (head l)) = 1 + (countIf (tail l) f) --recc
  | otherwise = (countIf (tail l) f) --recc