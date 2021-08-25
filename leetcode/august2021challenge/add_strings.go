func addStrings(num1 string, num2 string) string {
    pointer1 := len(num1) - 1
    pointer2 := len(num2) - 1
    
    otp := ""
    addition := 0
    
    for (pointer1 >= 0 || pointer2 >= 0) {
        dig1 := 0
        dig2 := 0
        
        if pointer1 >= 0 {
            i, err := strconv.Atoi(string(num1[pointer1]))
            
            if err != nil {
                // handle error
                fmt.Println(err)
                os.Exit(2)
            } else {
                dig1 = i
            }
        }
        
        if pointer2 >= 0 {
            j, err := strconv.Atoi(string(num2[pointer2]))
            
            if err != nil {
                // handle error
                fmt.Println(err)
                os.Exit(2)
            } else {
                dig2 = j
            }
        }
        
        res := dig1 + dig2 + addition
        
        addition = res / 10
        remainder := res % 10
        
        otp = strconv.Itoa(remainder) + otp
        
        pointer1--
        pointer2--
    }
    
    if (addition > 0) {
        otp = strconv.Itoa(addition) + otp
    }
    
    return otp
}