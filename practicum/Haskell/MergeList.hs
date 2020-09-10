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

mergeList:: [Int] -> [Int] -> [Int]
{- mergeList(li1,li2) menghasilkan list of integer yang
   merupakan hasil penggabungan li1 dan li2, dan tetap
   terurut membesar.
   Prekondisi: li1 dan li2 adalah list terurut membesar
   dan mungkin kosong -}

--REALISASI
mergeList li1 li2
  | (isEmpty li1) && (isEmpty li2) = [] --basis 1
  | (isEmpty li1) = li2 --basis 2
  | (isEmpty li2) = li1 --basis 3
  | (head li1)<(head li2) = konso (head li1) (mergeList (tail li1) li2)
  | otherwise = konso (head li2) (mergeList li1 (tail li2))