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
    string visit(TreeNode* current, bool side){
        if (!current){
            return ".";
        }
        return visit(side ? current->left: current->right, side) + visit(side ? current->right : current->left, side) + to_string(current->val);
    }
    bool isSymmetric(TreeNode* root) {
        return visit(root->left, 0) == visit(root->right, 1);
    }
};