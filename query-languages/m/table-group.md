---
title: "Table.Group | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.Group

## Syntax

<pre>
Table.Group(<b>table</b> as table, <b>key</b> as any, <b>aggregatedColumns</b> as list, optional <b>groupKind</b> as nullable number, optional <b>comparer</b> as nullable function) as table 
</pre>
  
## About  
Groups the rows of `table` by the values in the specified column,`key`, for each row. For each group, a record is constructed containing the key columns (and their values) along with any aggregated columns specified by `aggregatedColumns`. Note if multiple keys match the comparer, different keys may be returned. This function cannot guarantee to return a fixed order of rows. Optionally, `groupKind` and `comparer` may also be specifed. 

## Example 1
Group the table adding an aggregate column [total] which contains the sum of prices ("each List.Sum([price])").

```powerquery-m
Table.Group( 
    Table.FromRecords({ 
        [CustomerID = 1, price = 20], 
        [CustomerID = 2, price = 10], 
        [CustomerID = 2, price = 20], 
        [CustomerID = 1, price = 10], 
        [CustomerID = 3, price = 20], 
        [CustomerID = 3, price = 5]
    }), 
    "CustomerID", 
    {"total", each List.Sum([price])} 
)
```

<table> <tr> <th>CustomerID</th> <th>total</th> </tr> <tr> <td>1</td> <td>30</td> </tr> <tr> <td>2</td> <td>30</td> </tr> <tr> <td>3</td> <td>25</td> </tr> </table>
