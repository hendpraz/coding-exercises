# @param {Integer[]} prices
# @return {Integer}
def max_profit(prices)
    is_going_up = false
    
    total = 0
    current_lowest = 0
    
    prev = prices[0]
    
    prices.each do |price|
        if is_going_up
            if price <= prev
                is_going_up = false
                total += prev - current_lowest
            end
        elsif price > prev
            is_going_up = true
            current_lowest = prev
        end
        
        prev = price
    end
    
    if is_going_up
        total += prev - current_lowest
    end
    
    return total
end