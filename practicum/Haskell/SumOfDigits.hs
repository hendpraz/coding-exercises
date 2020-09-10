module SumOfDigits where

--DEFINISI DAN SPESIFIKASI
  sumOfDigits :: Int -> Int

--REALISASI
  sumOfDigits x | (div x 10) == 0 = x
                | otherwise = (mod x 10) + sumOfDigits (div x 10)