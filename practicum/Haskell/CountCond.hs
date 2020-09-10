countCond :: [Int] -> (Int -> Int) -> Int

isEmpty :: [Int] -> Bool
-- isEmpty(li) true jika list of integer li kosong
-- REALISASI
isEmpty li = null li

countCond l f
  | isEmpty l = 0
  | (f (head l)) == 0 = 1 + countCond (tail l) f
  | otherwise = countCond (tail l) f