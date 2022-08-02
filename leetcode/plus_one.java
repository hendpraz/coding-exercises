class Solution {
    public int[] plusOne(int[] digits) {
        // special case: all 9
        
        boolean allNine = true;
        for (int i = 0; i < digits.length; i++) {
            if (digits[i] != 9) {
                allNine = false;
                break;
            }
        }
        
        if (allNine) {
            int[] result = new int[digits.length + 1];
            
            result[0] = 1;
            
            for (int i = 1; i < result.length; i++) {
                result[i] = 0;
            }
            
            return result;
        } else {
            int[] result = new int[digits.length];
            
            boolean plusOne = true;
            for (int i = result.length - 1; i >= 0; i--) {
                int addedOne = digits[i] + 1;

                if (plusOne) {
                    result[i] = addedOne % 10;
                } else {
                    result[i] = digits[i];
                }

                if (addedOne < 10) {
                    plusOne = false;
                }
            }
            
            return result;
        }
    }
}