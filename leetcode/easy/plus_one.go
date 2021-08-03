func plusOne(digits []int) []int {
    var result int
    
    pointer := len(digits) - 1
    
    stop := false
    for (!stop) {
        result = digits[pointer] + 1
        
        if (result < 10) || (pointer == 0) {
            stop = true
        }
        
        digits[pointer] = result % 10
        pointer--
    }
    
    if (result >= 10) {
        output := make([]int, len(digits) + 1)
        
        output[0] = 1
        
        for i := 1; i < len(output); i++ {
            output[i] = 0
        }
        
        return output
    }
    
    return digits
}