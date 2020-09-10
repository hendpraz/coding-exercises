module LuasTrapesium where

-- DEFINISI DAN SPESIFIKASI
 luasTrapesium :: Float -> Float -> Float -> Float

-- REALISASI
 luasTrapesium t s1 s2 = (t * (s1 + s2)) / 2

-- APLIKASI
-- luasTrapesium 2 4 3