---
title: "Table.TransformRows | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.TransformRows

## Syntax

<pre>
Table.TransformRows(<b>table</b> as table, <b>transform</b> as function) as list
</pre>
  
  
## About  
Creates a table from <code>table</code> by applying the <code>transform</code> operation to the rows. If the return type of the <code>transform</code> function is specified, then the result will be a table with that row type. In all other cases, the result of this function will be a list with an item type of the return type of the transform function.
 
  
## Example 1  

Transform the rows into a list of numbers from the table <code>({[A = 1], [A = 2], [A = 3], [A = 4], [A = 5]})</code>.

```powerquery-m
Table.TransformRows(
    Table.FromRecords({
        [a = 1], 
        [a = 2], 
        [a = 3], 
        [a = 4], 
        [a = 5]
    }),
    each [a]
)
```

<table> <tr><td>1</td></tr> <tr><td>2</td></tr> <tr><td>3</td></tr> <tr><td>4</td></tr> <tr><td>5</td></tr> </table>

## Example 2

Transform the rows in column [A] into text values in a column [B] from the table <code>({[A = 1], [A = 2], [A = 3], [A = 4], [A = 5])</code>.

```powerquery-m
Table.TransformRows(
    Table.FromRecords({
        [a = 1], 
        [a = 2], 
        [a = 3], 
        [a = 4], 
        [a = 5]
    }), 
    (row) as record => [B = Number.ToText(row[a])]
)
```

<table> <tr><td>[Record]</td></tr> <tr><td>[Record]</td></tr> <tr><td>[Record]</td></tr> <tr><td>[Record]</td></tr> <tr><td>[Record]</td></tr> </table>

  
