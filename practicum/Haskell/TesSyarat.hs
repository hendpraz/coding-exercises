module TesSyarat where

tesSyarat :: Float -> Float -> Int

tesSyarat ip pot
  | (ip >= 3.5) = 4
  | (pot < 1) && (ip < 3.5) = 1
  | (pot >= 1) && (pot < 5) && (ip < 2) = 2
  | (pot >= 1) && (pot < 5) && (ip >= 2) && (ip < 3.5) = 3
  | otherwise = 0