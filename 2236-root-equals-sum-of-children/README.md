<h2><a href="https://leetcode.com/problems/root-equals-sum-of-children/">2236. Root Equals Sum of Children</a></h2><h3>Easy</h3><hr><div><p>You are given the <code>root</code> of a <strong><span class="tou-node" id="tou-3.0-71732d82-b322-40e5-9828-0c5abcf40028"></span> tree</strong> that consists of <span class="tou-node" id="tou-4-e4e711c6-981d-499f-aa00-f79b53e8cb20"></span> <code>3</code> nodes: the root, its left child, and its right child.</p>

<p>Return <code>true</code> <em>if the value of the root is equal to the <strong>sum</strong> of the values of its two <span class="tou-node" id="tou-3.2-855a8f17-f0d2-45aa-93d1-2c84c2365dad" lang="de"></span>, or </em><code>false</code><em> otherwise</em>.</p>

<p>&nbsp;</p>
<p><strong class="example"><span class="tou-node" id="tou-0.0-cfe55582-faba-48d7-9f7f-f14f81062a4f" lang="de"></span> 1:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/04/08/graph3drawio.png" style="width: 281px; height: 199px;">
<pre><strong>Input:</strong> root = [10,4,6]
<strong>Output:</strong> true
<strong>Explanation:</strong> The values of the root, its left child, and its right child are 10, 4, and 6, respectively.
10 is equal to 4 + 6, so we return true.
</pre>

<p><strong class="example"><span class="tou-node" id="tou-0.0-5197cf53-bf54-4d3e-9de5-51bb09811811" lang="de"></span> 2:</strong></p>
<img alt="" src="https://assets.leetcode.com/uploads/2022/04/08/graph3drawio-1.png" style="width: 281px; height: 199px;">
<pre><strong>Input:</strong> root = [5,3,1]
<strong>Output:</strong> false
<strong>Explanation:</strong> The values of the root, its left child, and its right child are 5, 3, and 1, respectively.
5 is not equal to 3 + 1, so we return false.
</pre>

<p>&nbsp;</p>
<p><strong>Constraints:</strong></p>

<ul>
	<li>The tree consists only of the root, its left child, and its right child.</li>
	<li><code>-100 &lt;= Node.val &lt;= 100</code></li>
</ul>
</div>