"""
<p>给你一个含重复值的二叉搜索树（BST）的根节点 <code>root</code> ，找出并返回 BST 中的所有 <a href="https://baike.baidu.com/item/%E4%BC%97%E6%95%B0/44796" target="_blank">众数</a>（即，出现频率最高的元素）。</p>

<p>如果树中有不止一个众数，可以按 <strong>任意顺序</strong> 返回。</p>

<p>假定 BST 满足如下定义：</p>

<ul> 
 <li>结点左子树中所含节点的值 <strong>小于等于</strong> 当前节点的值</li> 
 <li>结点右子树中所含节点的值 <strong>大于等于</strong> 当前节点的值</li> 
 <li>左子树和右子树都是二叉搜索树</li> 
</ul>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p> 
<img alt="" src="https://assets.leetcode.com/uploads/2021/03/11/mode-tree.jpg" style="width: 142px; height: 222px;" /> 
<pre>
<strong>输入：</strong>root = [1,null,2,2]
<strong>输出：</strong>[2]
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<strong>输入：</strong>root = [0]
<strong>输出：</strong>[0]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li>树中节点的数目在范围 <code>[1, 10<sup>4</sup>]</code> 内</li> 
 <li><code>-10<sup>5</sup> &lt;= Node.val &lt;= 10<sup>5</sup></code></li> 
</ul>

<p>&nbsp;</p>

<p><strong>进阶：</strong>你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）</p>

<div><div>Related Topics</div><div><li>树</li><li>深度优先搜索</li><li>二叉搜索树</li><li>二叉树</li></div></div><br><div><li>👍 640</li><li>👎 0</li></div>
"""
from collections import Counter
from typing import Optional, List


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inOrder(self, root, res):
        if root is None:
            return
        self.inOrder(root.left, res)
        res.append(root.val)
        self.inOrder(root.right, res)
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        lst = []
        self.inOrder(root, lst)
        lst = Counter(lst)
        tup = lst.most_common(len(lst))
        ans = []
        for i, j in tup:
            if j == tup[0][1]:
                ans.append(i)
            else:
                break
        return ans
# leetcode submit region end(Prohibit modification and deletion)
