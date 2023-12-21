/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    bool visit(TreeNode* leftHalf, TreeNode* rightHalf){
        if (!leftHalf && !rightHalf) return true;
        if (!leftHalf || !rightHalf) return false;
        if (leftHalf->val != rightHalf->val) return false;

        return visit(leftHalf->left, rightHalf->right) && visit(leftHalf->right, rightHalf->left);
    }
    bool isSymmetric(TreeNode* root) {
        return visit(root->left, root->right);
    }
};