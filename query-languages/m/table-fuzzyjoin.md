---
description: "Learn more about: Table.FuzzyJoin"
title: "Table.FuzzyJoin | Microsoft Docs"
ms.date: 11/23/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.FuzzyJoin
  
## Syntax

<pre>
Table.FuzzyJoin(<b>table1</b> as table, <b>key1</b> as any, <b>table2</b> as table, <b>key2</b> as any, optional <b>joinKind</b> as nullable number, optional <b>joinOptions</b> as nullable record) as table 
</pre>
  
## About 
  
Joins the rows of `table1` with the rows of `table2` based on a fuzzy matching of the values of the key columns selected by `key1` (for `table1`) and `key2` (for `table2`).

Fuzzy matching is a comparison based on similarity of text rather than equality of text.

By default, an inner join is performed, however an optional `joinKind` may be included to specify the type of join. Options include:

* `JoinKind.Inner`
* `JoinKind.LeftOuter`
* `JoinKind.RightOuter`
* `JoinKind.FullOuter`
* `JoinKind.LeftAnti`
* `JoinKind.RightAnti`

An optional set of `joinOptions` may be included to specify how to compare the key columns. Options include:

* `ConcurrentRequests`: A number between 1 and 8 that specifies the number of parallel threads to use for fuzzy matching. The default value is 1.
* `Culture`: Allows matching records based on culture-specific rules. It can be any valid culture name. For example, a Culture option of "ja-JP" matches records based on the Japanese culture. The default value is "", which matches based on the Invariant English culture.
* `IgnoreCase`: A logical (true/false) value that allows case-insensitive key matching. For example, when true, "Grapes" is matched with "grapes". The default value is true.
* `IgnoreSpace`: A logical (true/false) value that allows combining of text parts in order to find matches. For example, when true, "Gra pes" is matched with "Grapes". The default value is true.
* `NumberOfMatches`: A whole number that specifies the maximum number of matching rows that can be returned for every input row. For example, a value of 1 will return at most one matching row for each input row. If this option is not provided, all matching rows are returned.
* `SimilarityColumnName`: A name for the column that shows the similarity between an input value and the representative value for that input. The default value is null, in which case a new column for similarities will not be added.
* `Threshold`: A number between 0.00 and 1.00 that specifies the similarity score at which two values will be matched. For example, "Grapes" and "Graes" (missing "p") are matched only if this option is set to less than 0.90. A threshold of 1.00 is the same as specifying an exact match criteria. The default value is 0.80.
* `TransformationTable`: A table that allows matching records based on custom value mappings. It should contain "From" and "To" columns. For example, "Grapes" is matched with "Raisins" if a transformation table is provided with the "From" column containing "Grapes" and the "To" column containing "Raisins". Note that the transformation will be applied to all occurrences of the text in the transformation table. With the above transformation table, "Grapes are sweet" will also be matched with "Raisins are sweet". 

## Example

Left inner fuzzy join of two tables based on [FirstName]

```powerquery-m
Table.FuzzyJoin(
	  Table.FromRecords(
        {
		        [CustomerID = 1, FirstName1 = "Bob", Phone = "555-1234"], 
		        [CustomerID = 2, FirstName1 = "Robert", Phone = "555-4567"] 
	      },
        type table [CustomerID = nullable number, FirstName1 = nullable text, Phone = nullable text]
    ),
	  {"FirstName1"}, 
	  Table.FromRecords(
        {
		        [CustomerStateID = 1, FirstName2 = "Bob", State = "TX"], 
		        [CustomerStateID = 2, FirstName2 = "bOB", State = "CA"]
	      },
        type table [CustomerStateID = nullable number, FirstName2 = nullable text, State = nullable text]
    ),
	  {"FirstName2"}, 
	  JoinKind.LeftOuter, 
	  [IgnoreCase = true, IgnoreSpace = false] 
) 
```

<table> <tr> <th>CustomerID</th> <th>FirstName1</th> <th>Phone</th> <th>CustomerStateID</th> <th>FirstName2</th> <th>State</th> </tr> <tr> <td>1</td> <td>Bob</td> <td>555-1234</td> <td>1</td> <td>Bob</td> <td>TX</td> </tr> <tr> <td>1</td> <td>Bob</td> <td>555-1234</td> <td>2</td> <td>bOB</td> <td>CA</td> </tr> <tr> <td>2</td> <td>Robert</td> <td>555-4567</td> <td></td> <td></td> <td></td> </tr> </table>
  
