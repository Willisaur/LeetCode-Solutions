class Solution {
public:
    bool canPlaceFlowers(vector<int>& flowerbed, int n) {
        while (flowerbed.size() > 1){
            auto start = flowerbed.begin();
            if (flowerbed[0] == 0 && flowerbed[1] == 0){
                flowerbed.erase(start, start + 2);
                --n;
            } else if (flowerbed[0] == 1){
                flowerbed.erase(start, start + 2);
            } else {
                if (flowerbed.size() > 2){
                    flowerbed.erase(start, start + 3);
                }
                else{
                    flowerbed.erase(start, start + 2);
                }
            }
        }
        if (flowerbed.size() == 1){
            if (!flowerbed[0]){
                --n;
            }
        }
        return n <= 0;
    }
};