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

offsetList :: [Int] -> (Int -> Int) -> [Int]

--REALISASI
offsetList l offset 
  | (isEmpty l) = []
  | otherwise = konso (offset (head l)) (offsetList (tail l) offset)