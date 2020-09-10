isOneElmt :: [Char] -> Bool
-- isOneElmt(li) true jika list of char lc hanya
-- mempunyai satu elemen
-- REALISASI
isOneElmt lc = (length lc) == 1

isUnique :: [Char] -> Bool
{- isUnique(lc) menghasilkan true jika lc adalah list
dengan elemen unik, yaitu tidak ada elemen pada lc
yang muncul lebih dari 1 kali -}

cekChar :: Char -> [Char] -> Bool

--REALISASI
cekChar x lc
  | x == (head lc) = True
  | isOneElmt lc = False
  | otherwise = cekChar x (tail lc)


isUnique lc
  | isOneElmt lc = True
  | (cekChar (head lc) (tail lc)) = False
  | otherwise = isUnique (tail lc)