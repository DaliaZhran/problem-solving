
# my sol
class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        baskets = {}
        start, end = 0, 0
        count = 0
        while end < len(tree):
            if tree[end] not in baskets:
                baskets[tree[end]] = 0
            baskets[tree[end]] += 1
            
            while len(baskets) > 2:
                baskets[tree[start]] -= 1
                if baskets[tree[start]] == 0:
                    del baskets[tree[start]] 
                start += 1
            
            count = max(count, end - start + 1)
            end += 1
        return count


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