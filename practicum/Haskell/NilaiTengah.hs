-- DEFINISI DAN SPESIFIKASI
 nilaiTengah :: Int -> Int -> Int -> Int
 max2 :: Int -> Int -> Int
 min2 :: Int -> Int -> Int
 max3 :: Int -> Int -> Int -> Int
 min3 :: Int -> Int -> Int -> Int

-- REALISASI
 max2 a b = div (a+b+abs(a-b)) 2
 min2 a b = div (a+b-abs(a-b)) 2
 max3 a b c = max2 c (max2 a b)
 min3 a b c = min2 c (min2 a b)
 nilaiTengah a b c = (a + b + c) - (max3 a b c) - (min3 a b c)

-- APLIKASI
-- nilaiTengah 5 3 7