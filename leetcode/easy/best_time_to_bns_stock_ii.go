func maxProfit(prices []int) int {
    isUp := false
    
    total := 0
    currentLowest := 0
    
    prev := prices[0]
    
    for i := 1; i < len(prices); i++ {
        if prices[i] > prev {
            if (!isUp) {
                isUp = true
                currentLowest = prev
            }
        } else if(isUp) {
            isUp = false
            total += prev - currentLowest
        }
        
        prev = prices[i]
    }
    
    if (isUp) {
        total += (prev - currentLowest)
    }
    
    return total
}