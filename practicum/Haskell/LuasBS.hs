module LuasBS where

-- DEFINISI DAN SPESIFIKASI
 luasBS :: Int -> Int
 jumlahkan :: Int -> Int -> Int

-- REALISASI
 jumlahkan a b
   | b == 0 = 0
   | otherwise = a + (jumlahkan a (b-1))

 luasBS s 
   | s == 1 = 1
   | otherwise = jumlahkan s s