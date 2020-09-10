module ListOfInteger where

isMember :: [Int] -> Int -> Bool

isMember li x
  | (null li) = False
  | (head li) == x = True
  | otherwise = isMember (tail li) x