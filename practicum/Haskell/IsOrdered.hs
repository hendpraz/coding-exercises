-- DEFINISI DAN SPESIFIKASI KONSTRUKTOR
konso :: Int -> [Int] -> [Int]
-- konso(e,li) menghasilkan sebuah list dari e (sebuah
-- integer) dan li (list of integer),
-- dengan e sebagai elemen pertama: e o li -> li'
-- REALISASI
konso e li = [e] ++ li

isOneElmt :: [Int] -> Bool
-- isOneElmt(li) true jika list of integer li hanya
-- mempunyai satu elemen
-- REALISASI
isOneElmt li = (length li) == 1

isOrdered :: [Int] -> Bool
{- isOrdered(l) menghasilkan true jika elemen-elemen pada
l terurut membesar, false jika tidak.
Prekondisi: l tidak kosong -}

--REALISASI
isOrdered l 
  | (isOneElmt l) = True
  | (head l) > (head (tail l)) = False
  | otherwise = isOrdered (tail l)