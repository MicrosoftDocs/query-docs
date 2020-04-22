---
title: "Table.Repeat | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.Repeat

## Syntax

<pre>
Table.Repeat(<b>table</b> as table, <b>count</b> as number) as table  
</pre>
  
## About  
Returns a table with the rows from the input `table` repeated the specified `count` times.

## Example 1
Repeat the rows in the table two times.

```powerquery-m
Table.Repeat(
    Table.FromRecords({
        [a = 1, b = "hello"], 
        [a = 3, b = "world"]
    }), 
    2
)
```

<table> <tr> <th>a</th> <th>b</th> </tr> <tr> <td>1</td> <td>hello</td> </tr> <tr> <td>3</td> <td>world</td> </tr> <tr> <td>1</td> <td>hello</td> </tr> <tr> <td>3</td> <td>world</td> </tr> </table>
