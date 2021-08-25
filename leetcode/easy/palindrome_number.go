// challenge: solve without turning input to a string
func powInt(x, y int) int {
    return int(math.Pow(float64(x), float64(y)))
}

func isPalindrome(x int) bool {
    if x < 0 {
        return false
    } else if x == 0 {
        return true
    } else {
        n := 0    
        temp := x
        
        for temp > 0 {
            temp = temp / 10
            n += 1
        }
        
        front := x
        mid := n / 2
        
        for mid > 0 {
            front = front / 10
            mid -= 1
        }
        
        if n % 2 == 1 {
            front = front / 10
        }
        
        mid = n / 2
        divisor := (powInt(10, mid - 1))

        back := x
        
        for mid > 0 {
            dig1 := front % 10
            dig2 := (back / divisor) % 10
            
            // fmt.Println(front, back, divisor)
            
            if dig1 != dig2 {
                return false
            }
            
            front /= 10
            divisor /= 10
            
            mid -= 1
        }
        
        return true
    }
}