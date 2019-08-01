---
title: "Table.ToList | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ToList

## Syntax

<pre> 
Table.ToList(<b>table</b> as table, optional <b>combiner</b> as nullable function) as list
</pre>
  
## About  
Converts a table into a list by applying the specified combining function to each row of values in the table.

## Example 1
Combine the text of each row with a comma.

```powerquery-m
Table.ToList(Table.FromRows({{Number.ToText(1),"Bob", "123-4567" }, {Number.ToText(2), "Jim", "987-6543" }, {Number.ToText(3), "Paul", "543-7890" }}), Combiner.CombineTextByDelimiter(","))
```

<table> <tr><td>1,Bob,123-4567</td></tr> <tr><td>2,Jim,987-6543</td></tr> <tr><td>3,Paul,543-7890</td></tr> </table>

