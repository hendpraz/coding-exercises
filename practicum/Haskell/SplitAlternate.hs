isEmpty :: [Char] -> Bool
-- REALISASI
isEmpty li = null li

-- DEFINISI DAN SPESIFIKASI KONSTRUKTOR
konso :: Char -> [Char] -> [Char]
-- konso(e,li) menghasilkan sebuah list dari e (sebuah
-- integer) dan li (list of integer),
-- dengan e sebagai elemen pertama: e o li -> li'
-- REALISASI
konso e li = [e] ++ li

splitAlternate :: [Char] -> ([Char],[Char])
{- splitAlternate(l) menghasilkan dua buah list, misalnya
l1 dan l2. l1 berisi semua elemen l pada posisi
ganjil, l2 berisi semua elemen l pada posisi genap -}
ambilElemen :: Int -> [Char] -> [Char]

--REALISASI
ambilElemen n l
  | (isEmpty l) = []
  | (mod n 2) == 0 = ambilElemen (n+1) (tail l)
  | otherwise = konso (head l) (ambilElemen (n+1) (tail l))

splitAlternate l = (ambilElemen 1 l,ambilElemen 1 (tail l))