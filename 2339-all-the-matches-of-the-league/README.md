<h2><a href="https://leetcode.com/problems/all-the-matches-of-the-league/">2339. All the Matches of the League</a></h2><h3>Easy</h3><hr><div class="sql-schema-wrapper__3VBi"><a class="sql-schema-link__3cEg">SQL Schema<svg viewBox="0 0 24 24" width="1em" height="1em" class="icon__1Md2"><path fill-rule="evenodd" d="M10 6L8.59 7.41 13.17 12l-4.58 4.59L10 18l6-6z"></path></svg></a></div><div><p>Table: <code>Teams</code></p>

<pre>+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| team_name   | varchar |
+-------------+---------+
team_name is the primary key of this table.
Each row of this table shows the name of a team.
</pre>

<p>&nbsp;</p>

<p>Write an SQL query that reports all the possible matches of the league. Note that every two teams play two matches with each other, with one team being the <code>home_team</code> once and the other time being the <code>away_team</code>.</p>

<p>Return the result table in <strong>any order</strong>.</p>

<p>The query result format is in the following example.</p>

<p>&nbsp;</p>
<p><strong class="example">Example 1:</strong></p>

<pre><strong>Input:</strong> 
Teams table:
+-------------+
| team_name   |
+-------------+
| Leetcode FC |
| Ahly SC     |
| Real Madrid |
+-------------+
<strong>Output:</strong> 
+-------------+-------------+
| home_team   | away_team   |
+-------------+-------------+
| Real Madrid | Leetcode FC |
| Real Madrid | Ahly SC     |
| Leetcode FC | Real Madrid |
| Leetcode FC | Ahly SC     |
| Ahly SC     | Real Madrid |
| Ahly SC     | Leetcode FC |
+-------------+-------------+
<strong>Explanation:</strong> All the matches of the league are shown in the table.
</pre>
</div>