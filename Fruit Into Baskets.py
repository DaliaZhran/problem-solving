# https://leetcode.com/problems/fruit-into-baskets/


# Time: O(N)
# Space: O(1)
class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        fruits = defaultdict(int)
        start, end = 0, 0
        
        max_amount = 0
        while end < len(tree):
            fruits[tree[end]] += 1
            while len(fruits) > 2:
                fruits[tree[start]] -= 1
                if fruits[tree[start]] == 0:
                    del fruits[tree[start]]
                start += 1
            max_amount = max(max_amount, end - start + 1)
            end += 1
        
        return max_amount


# c++ sol but good too ( constant space - linear time)
class Solution {
    public int totalFruit(int[] tree) {
        // track last two fruits seen
        int lastFruit = -1;
        int secondLastFruit = -1;
        int lastFruitCount = 0;
        int currMax = 0;
        int max = 0;
        
        for (int fruit : tree) {
            if (fruit == lastFruit || fruit == secondLastFruit)
                currMax++;
            else
                currMax = lastFruitCount + 1; // last fruit + new fruit
            
            if (fruit == lastFruit)
                lastFruitCount++;
            else
                lastFruitCount = 1; 
            
            if (fruit != lastFruit) {
                secondLastFruit = lastFruit;
                lastFruit = fruit;
            }
            
            max = Math.max(max, currMax);
        }
        
        return max;
    }
}
