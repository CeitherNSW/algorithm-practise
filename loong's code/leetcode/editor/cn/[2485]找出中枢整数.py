"""
<p>给你一个正整数 <code>n</code> ，找出满足下述条件的<strong> 中枢整数</strong> <code>x</code> ：</p>

<ul> 
 <li><code>1</code> 和 <code>x</code> 之间的所有元素之和等于 <code>x</code> 和 <code>n</code> 之间所有元素之和。</li> 
</ul>

<p>返回中枢整数<em> </em><code>x</code> 。如果不存在中枢整数，则返回 <code>-1</code> 。题目保证对于给定的输入，至多存在一个中枢整数。</p>

<p>&nbsp;</p>

<p><strong class="example">示例 1：</strong></p>

<pre>
<strong>输入：</strong>n = 8
<strong>输出：</strong>6
<strong>解释：</strong>6 是中枢整数，因为 1 + 2 + 3 + 4 + 5 + 6 = 6 + 7 + 8 = 21 。
</pre>

<p><strong class="example">示例 2：</strong></p>

<pre>
<strong>输入：</strong>n = 1
<strong>输出：</strong>1
<strong>解释：</strong>1 是中枢整数，因为 1 = 1 。
</pre>

<p><strong class="example">示例 3：</strong></p>

<pre>
<strong>输入：</strong>n = 4
<strong>输出：</strong>-1
<strong>解释：</strong>可以证明不存在满足题目要求的整数。</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul> 
 <li><code>1 &lt;= n &lt;= 1000</code></li> 
</ul>

<div><div>Related Topics</div><div><li>数学</li><li>前缀和</li></div></div><br><div><li>👍 40</li><li>👎 0</li></div>
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def pivotInteger(self, n: int) -> int:
        前缀和 = []
        for i in range(1, n+1):
            前缀和.append(sum(range(1, n+1)[:i+1]))
        return 前缀和

# leetcode submit region end(Prohibit modification and deletion)
print(Solution().pivotInteger(8))