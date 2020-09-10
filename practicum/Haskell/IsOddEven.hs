-- Deskripsi : Fungsi rekursi untuk mengecek ganjil genapnya sebuah integer

-- DEFINISI DAN SPESIFIKASI
 isOdd :: Int -> Bool
 isEven :: Int -> Bool

-- REALISASI
 isOdd a
   | a == 1 = True
   | otherwise = isEven(a-1)
 isEven a
   | a == 1 = False
   | otherwise = isOdd(a-1)

-- APLIKASI
-- isEven 4 atau isOdd 12