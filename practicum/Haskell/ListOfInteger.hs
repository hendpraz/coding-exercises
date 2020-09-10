module ListOfInteger where

isEmpty :: [Int] -> Bool
-- isEmpty(li) true jika list of integer li kosong
-- REALISASI
isEmpty li = null li

-- DEFINISI DAN SPESIFIKASI KONSTRUKTOR
konso :: Int -> [Int] -> [Int]
{- konso e li menghasilkan sebuah list of integer dari e (sebuah integer) dan li 
   (list of integer), dengan e sebagai elemen pertama: e o li -> li' -}
-- REALISASI
konso e li = [e] ++ li

deleteIf :: [Int] -> (Int -> Bool) -> [Int]

--REALISASI
deleteIf l f
  | (isEmpty l) = [] --basis
  | (f (head l)) = (deleteIf (tail l) f) --recc
  | otherwise = konso (head l) (deleteIf (tail l) f) --recc