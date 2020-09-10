module TesKategori where

-- DEFINISI DAN SPESIFIKASI
 tesKategori :: Int -> Int -> Int -> Bool

-- REALISASI
 tesKategori h w k | (h > 100) && (w <= 150) && (k > 1) && (k <= 4) = True
 				   | (h <= 100) && (w <= 150) && (k == 1) = True
 				   | (h <= 100) && (w <= 150) && (w > 30) && (k == 2) = True
 			 	   | (w > 150) && (h <= 100) && (k == 2) = True
 			 	   | (w > 150) && (h > 100) && (h <= 200) && ((k == 3) || (k == 2)) = True
 				   | (h > 200) && (w > 150) && (k == 0) = True
 				   | otherwise = False

-- APLIKASI
-- tesKategori 120 80 1