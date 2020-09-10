module SumKelipatanX where

--DEFINISI DAN SPESIFIKASI
  sumKelipatanX :: Int -> Int -> Int -> Int

--REALISASI
  sumKelipatanX m n x
    | n < m = 0
    | (mod n x) == 0 = n + sumKelipatanX m (n-1) x
    | otherwise = sumKelipatanX m (n-1) x