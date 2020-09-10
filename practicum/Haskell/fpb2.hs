-- Mencari nilai FPB dari dua buah integer dengan pendekatan kedua

-- DEFINISI DAN SPESIFIKASI
 fpb :: Int -> Int -> Int
 cari :: Int -> Int -> Int -> Int
 min2 :: Int -> Int -> Int
 -- Mencari FPB dari dua buah integer m dan n dengan fungsi antara.

-- REALISASI
 min2 a b = (a+b-abs(a-b))
 cari m n x | ((mod m x) == 0) && ((mod n x) == 0) = x
            | otherwise = cari m n (x-1)
 fpb m n = cari m n (min2 m n)

-- APLIKASI 
-- fpb 24 18