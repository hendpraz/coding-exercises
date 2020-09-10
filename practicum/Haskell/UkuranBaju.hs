module UkuranBaju where

-- DEFINISI DAN SPESIFIKASI
 ukuranBaju :: Int -> Int -> Int

-- REALISASI
 ukuranBaju h w | (h <= 150) = 1
 				| (h > 150) && (h <= 170) && (w <= 80) = 2
 				| (h > 170) && (w <= 60) = 2
 				| (h > 150) && (h <= 170) && (w > 80) = 3
 				| (h > 170) && (w > 60) && (w <= 80) = 3
 				| otherwise = 4

-- APLIKASI
-- ukuranBaju 160 75