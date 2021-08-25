func twoSum(nums []int, target int) []int {
    var indexMap map[int]int
    var i, num, solutionValue int
    
    indexMap = make(map[int]int)
    
    for i = 0; i < len(nums); i++ {
        num = nums[i]
        solutionValue = target - num
        
        solutionIndex, isExist := indexMap[solutionValue]
        
        if (isExist) {
            return []int{solutionIndex, i}
        } else {
            indexMap[num] = i
        }
    }
    
    return []int{0,0}
}