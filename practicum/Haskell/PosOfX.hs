isMember1 :: Char -> [Char] -> Bool
-- REALIASI
isMember1 x l = if (isEmpty l) then False -- Basis
                else if (head l) == x then True
                     else (isMember1 x (tail l)) -- Rekurens

isEmpty :: [Char] -> Bool
-- REALISASI
isEmpty li = null li

posOfX :: Char -> [Char] -> Int
{- posOfX(e,lc) menghasilkan sebuah bilangan integer yang
menyatakan posisi e pada list of character lc. Jika e
bukan elemen dari lc, fungsi akan menghasilkan 0.
Prekondisi: lc memiliki elemen unik -}

--REALISASI
posOfX e lc
  | (isEmpty lc) = 0
  | not(isMember1 e lc) = 0
  | (head lc) == e = 1
  | otherwise = 1 + posOfX e (tail lc)