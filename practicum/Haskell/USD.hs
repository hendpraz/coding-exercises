-- DEFINISI DAN SPESIFIKASI
 usd :: Int -> Int -> Int -> Int -> (Int , Int)

-- REALISASI
 usd q d n p = 
   let x = (q * 25) + (d * 10) + (n * 5) + p
   in
   ( div x 100,
     mod x 100 )

-- APLIKASI
-- usd 8 20 30 77