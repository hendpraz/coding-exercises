func maxSubArray(nums []int) int {
    var currentMax, i, max, num int
    
    currentMax = nums[0]
    max = nums[0]
    
    for i = 1; i < len(nums); i++ {
        num = nums[i]
        
        if (currentMax + num < num) {
            currentMax = num
        } else {
            currentMax += num
        }
        
        if (currentMax > max) {
            max = currentMax
        }
    }
    
    return max
}