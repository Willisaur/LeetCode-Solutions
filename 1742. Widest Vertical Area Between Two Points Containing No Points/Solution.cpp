class Solution {
public:
    int maxWidthOfVerticalArea(vector<vector<int>>& points) {
        sort(points.begin(), points.end());
        int maxWidth = abs(points[0][0] - points[1][0]);

        int width;
        for (int i=2; i<points.size(); ++i){
            width = abs(points[i-1][0] - points[i][0]);
            maxWidth = max(width, maxWidth);
        }
        return maxWidth;
    }
};