class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        // you only need to look at the first two elements since they're the edge
        // if elements 1 and 2 are 0, you can plant a flower
        // if element 1 is 1, you cannot plant a flower in the current two spots
        // if element 2 is 1, you cannot plant a flower in the current 2 + 1 spots
        // if one element is left over and it's a zero, you can plant a flower
        auto start  = flowerbed.begin();
        while (flowerbed.size() > 1){
            if (flowerbed[0] == 0 && flowerbed[1] == 0){
                flowerbed.erase(start, start + 2);
                --n;
            } else if (flowerbed[0] == 1){
                flowerbed.erase(start, start + 2);
            } else {
                flowerbed.erase(start, start + (flowerbed.size() > 2 ? 3 : 2));
            }
            start = flowerbed.begin();
        }
        if (flowerbed.size() == 1 && !flowerbed[0]){
            --n;
        }
        return n <= 0;
    }
};