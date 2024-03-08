/*
Daily challenge in 2024.03.08
3005. Count Elements With Maximum Frequency
Difficulty : Easy
Algorithm : Hash Map
Time complexity : O(N), Space complexity : O(N)
Runtime : 3 ms (31.20%), Memory : 42.10 MB (66.26%)
*/

import java.util.*;

class Solution {
    public int maxFrequencyElements(int[] nums) {
        Map<Integer, Integer> map = new HashMap<>();

        int fre = 1;
        for(int num : nums) {
            if(map.containsKey(num) == true) {
                int val = map.get(num);
                map.replace(num, val+1);
                fre = (val+1 > fre) ? (val+1) : fre;
            }
            else {map.put(num, 1);}
        }

        int cnt = 0;
        for(int num : map.values()) {
            if(fre == num) {cnt += num;}
        }

        return cnt;
    }
}
