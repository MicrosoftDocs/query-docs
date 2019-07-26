---
title: "Table.AddJoinColumn | Microsoft Docs"
ms.date: 7/26/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.AddJoinColumn

## Syntax

<pre>
Table.AddJoinColumn(table1 as table, key1 as any, table2 as function, key2 as any, newColumnName as text) as table  
</pre>
  
## About  


Joins the rows of <code>table1</code> with the rows of <code>table2</code> based on the equality of the values of the key columns selected by <code>key1</code> (for <code>table1</code>) and <code>key2</code> (for <code>table2</code>). The results are entered into the column named <code>newColumnName</code>. This function behaves similarly to Table.Join with a JoinKind of LeftOuter except that the join results are presented in a nested rather than flattened fashion.

## Example 1
Add a join column to ({[saleID = 1, item = "Shirt"], [saleID = 2, item = "Hat"]}) named "price/stock" from the table ({[saleID = 1, price = 20], [saleID = 2, price = 10]}) joined on [saleID].

```powerquery-m
Table.AddJoinColumn(Table.FromRecords({[saleID = 1, item = "Shirt"], [saleID = 2, item = "Hat"]}), "saleID", () => Table.FromRecords({[saleID = 1, price = 20, stock = 1234], [saleID = 2, price = 10, stock = 5643]}), "saleID", "price")
```

<table> <tr> <th>saleID</th> <th>item</th> <th>price</th> </tr> <tr> <td>1</td> <td>Shirt</td> <td>[Table]</td> </tr> <tr> <td>2</td> <td>Hat</td> <td>[Table]</td> </tr> </table>