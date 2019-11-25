---
title: "Table.FuzzyJoin | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.FuzzyJoin
  
## Syntax

<pre>
Table.FuzzyJoin(<b>table1</b> as table, <b>key1</b> as any, <b>table2</b> as table, <b>key2</b> as any, optional <b>joinKind</b> as nullable number, optional <b>joinOptions</b> as nullable record) as table 
</pre>
  
## About 
  
<p>Joins the rows of `table1` with the rows of `table2` based on a fuzzy matching of the values of the key columns selected by `key1` (for `table1`) and `key2` (for `table2`).</p> <p>Fuzzy matching is a comparison based on similarity of text rather than equality of text.</p> <p>By default, an inner join is performed, however an optional `joinKind` may be included to specify the type of join. Options include: <ul> <li><code>JoinKind.Inner</code></li> <li><code>JoinKind.LeftOuter</code></li> <li><code>JoinKind.RightOuter</code></li> <li><code>JoinKind.FullOuter</code></li> <li><code>JoinKind.LeftAnti</code></li> <li><code>JoinKind.RightAnti</code></li> </ul> </p> <p>An optional set of <code>joinOptions</code> may be included to specify how to compare the key columns. Options include: <ul> <li><code>ConcurrentRequests</code></li> <li><code>Culture</code></li> <li><code>IgnoreCase</code></li> <li><code>IgnoreSpace</code></li> <li><code>NumberOfMatches</code></li> <li><code>Threshold</code></li> <li><code>TransformationTable</code></li> </ul> </p> <p> The following table provides more details about the advanced options. <table> <tr> <th>Advanced Option</th> <th>Default</th> <th>Allowed</th> <th>Description</th> </tr> <tr> <td>ConcurrentRequests</td> <td>1</td> <td>Between 1 and 8</td> <td>The ConcurrentRequests option supports parallelizing the join operation by specifying the number of parallel threads to to use.</td> </tr> <tr> <td>Culture</td> <td>Culture neutral</td> <td>A valid culture name</td> <td>The Culture option allows matching records based on culture-specific rules. <br> For example a Culture option of 'ja-JP' matches records based on the Japanese language.</td> </tr> <tr> <td>IgnoreCase</td> <td>true</td> <td>true or false</td> <td>The IgnoreCase option allows matching records irrespective of the case of the text. <br> For example, 'Grapes' (sentence case) is matched with 'grapes' (lower case) if the IgnoreCase option is set to true.</td> </tr> <tr> <td>IgnoreSpace</td> <td>true</td> <td>true or false</td> <td>The IgnoreSpace option allows combining text parts in order to find matches. <br> For example, 'Micro soft' is matched with both 'Microsoft' and 'Micro soft' if the IgnoreSpace option is set to true.</td> </tr> <tr> <td>NumberOfMatches</td> <td>2147483647</td> <td>Between 0 and 2147483647</td> <td>The NumberOfMatches option specifies the maximum number of matching rows that can be returned.</td> </tr> <tr> <td>Threshold</td> <td>0.80</td> <td>Between 0.00 and 1.00</td> <td>The similarity Threshold option provides the ability to match records above a given similarity score. A threshold of 1.00 is the same as specifying an exact match criteria. <br> For example, 'Grapes' matches with 'Graes' (missing 'p') only if the thresold is set to less than 0.90.</td> </tr> <tr> <td>TransformationTable</td> <td></td> <td>A valid table with at least 2 columns named 'From' and 'To'.</td> <td>The TransformationTable option allows matching records based on custom value mappings. <br> For example, 'Grapes' are matched with 'Raisins' if a transformation table is provided with the 'From' column containing 'Grapes' and the 'To' column containing 'Raisins'.</td> </tr> </table> </p>

## Example

Left inner fuzzy join of two tables based on [FirstName]

```powerquery-m
Table.FuzzyJoin( Table.FromRecords({ [CustomerID = 1, FirstName1 = "Bob", Phone = "555-1234"], [CustomerID = 2, FirstName1 = "Robert", Phone = "555-4567"] }, type table [CustomerID = nullable number, FirstName1 = nullable text, Phone = nullable text]), {"FirstName1"}, Table.FromRecords({ [CustomerStateID = 1, FirstName2 = "Bob", State = "TX"], [CustomerStateID = 2, FirstName2 = "bOB", State = "CA"] }, type table [CustomerStateID = nullable number, FirstName2 = nullable text, State = nullable text]), {"FirstName2"}, JoinKind.LeftOuter, [IgnoreCase = true, IgnoreSpace = false] ) 
```

<table> <tr> <th>CustomerID</th> <th>FirstName1</th> <th>Phone</th> <th>CustomerStateID</th> <th>FirstName2</th> <th>State</th> </tr> <tr> <td>1</td> <td>Bob</td> <td>555-1234</td> <td>1</td> <td>Bob</td> <td>TX</td> </tr> <tr> <td>1</td> <td>Bob</td> <td>555-1234</td> <td>2</td> <td>bOB</td> <td>CA</td> </tr> <tr> <td>2</td> <td>Robert</td> <td>555-4567</td> <td></td> <td></td> <td></td> </tr> </table>
  
