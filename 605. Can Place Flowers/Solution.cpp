class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        // you only need to look at the first two elements since they're the edge
        // if elements 1 and 2 are 0, you can plant a flower
        // if element 1 is 1, you cannot plant a flower in the current two spots
        // if element 2 is 1, you cannot plant a flower in the current 2 + 1 spots
        // if one element is left over and it's a zero, you can plant a flower
        int i = 0;
        int first, second;
        int size = flowerbed.size();
        while (i+1 < size){
            first = flowerbed[i];
            second = flowerbed[i+1];

            if (!first && !second){
                --n;
            } else if (!first){
                if (i < size){
                    ++i;
                }
            }
            i += 2;
        }
        if (i < size && !flowerbed[size-1]){
            --n;
        }
        return n<=0;
    }
};