# @param {Integer[]} nums
# @return {Boolean}
def contains_duplicate(nums)
    num_hash = Hash.new
    
    nums.each do |num|
        if num_hash[num]
            return true
        else
            num_hash[num] = true
        end
    end
    
    return false
end