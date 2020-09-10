module NbKelipatanX where

--DEFINISI DAN SPESIFIKASI
  nbKelipatanX :: Int -> Int -> Int -> Int

--REALISASI
  nbKelipatanX m n x
    | n < m = 0
    | (mod n x) == 0 = 1 + nbKelipatanX m (n-1) x
    | otherwise = nbKelipatanX m (n-1) x