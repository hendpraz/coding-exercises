# @param {Integer[]} nums1
# @param {Integer[]} nums2
# @return {Integer[]}
def intersect(nums1, nums2)
    # sorted array inputs
    
    nums1 = nums1.sort_by { |num| num }
    nums2 = nums2.sort_by { |num| num }
    
    pointer1 = 0
    pointer2 = 0
    
    intersections = []
    
    while pointer1 < nums1.size && pointer2 < nums2.size
        num1 = nums1[pointer1]
        num2 = nums2[pointer2]
        
        if num1 == num2
            intersections.append(num1)

            pointer1 += 1
            pointer2 += 1
        elsif num1 < num2
            pointer1 += 1
        else # num1 > num2
            pointer2 += 1
        end
    end
    
    return intersections
end