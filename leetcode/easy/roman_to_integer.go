func romanToInt(s string) int {
    var el, double string
    romanMap := map[string]int {
        "I": 1,
        "IV": 4,
        "V": 5,
        "IX": 9,
        "X": 10,
        "XL": 40,
        "L": 50,
        "XC": 90,
        "C": 100,
        "CD": 400,
        "D": 500,
        "CM": 900,
        "M": 1000,
    }
    
    total := 0
    for i := 0; i < len(s); i++ {
        el = string(s[i])
        
        if i < len(s) - 1 {
            double = string(s[i]) + string(s[i+1])
            
            value, isExist := romanMap[double]
            
            if (isExist) {
                total += value
                i++
            } else {
                total += romanMap[el]
            }
        } else {
            total += romanMap[el]
        }
    }
    
    return total
}