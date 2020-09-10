-- DEFINISI DAN SPESIFIKASI KONSTRUKTOR
konso :: Int -> [Int] -> [Int]
-- konso(e,li) menghasilkan sebuah list dari e (sebuah
-- integer) dan li (list of integer),
-- dengan e sebagai elemen pertama: e o li -> li'
-- REALISASI
konso e li = [e] ++ li

isEmpty :: [Int] -> Bool
-- isEmpty(li) true jika list of integer li kosong
-- REALISASI
isEmpty li = null li

--DEFINISI DAN SPESIFIKASI
splitList :: [Int] -> ([Int],[Int])
{- splitList(li) menghasilkan 2 list of integer, list
   pertama memuat bilangan positif dan 0 yang merupakan
   elemen dari li (dengan urutan kemunculan yang tidak
   berubah), sedangkan list kedua memuat bilangan negatif
   elemen li.
   Prekondisi: li mungkin kosong-}
listPos :: [Int] -> [Int]
listNeg :: [Int] -> [Int]

--REALISASI
listPos li
  | isEmpty li = []
  | (head li) >= 0 = konso (head li)  (listPos (tail li))
  | otherwise = listPos (tail li)

listNeg li
  | isEmpty li = []
  | (head li) < 0 = konso (head li)  (listNeg (tail li))
  | otherwise = listNeg (tail li)

splitList li = (listPos li,listNeg li)