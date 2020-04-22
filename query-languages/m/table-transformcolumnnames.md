---
title: "Table.TransformColumnNames | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.TransformColumnNames

## Syntax

<pre>
Table.TransformColumnNames(<b>table</b> as table, <b>nameGenerator</b> as function, optional <b>options</b> as nullable record) as table
</pre>
  
## About  
Transforms column names by using the given `nameGenerator` function. Valid options: <div> `MaxLength` specifies the maximum length of new column names. If the given function results with a longer column name, the long name will be trimmed. </div> <div> `Comparer` is used to control the comparison while generating new column names. Comparers can be used to provide case insensitive or culture and locale aware comparisons. </div> <div> The following built in comparers are available in the formula language: </div> <ul> <li><code>Comparer.Ordinal</code>: Used to perform an exact ordinal comparison</li> <li><code>Comparer.OrdinalIgnoreCase</code>: Used to perform an exact ordinal case-insensitive comparison</li> <li> <code>Comparer.FromCulture</code>: Used to perform a culture aware comparison</li> </ul> 

## Example 1
Remove the `#(tab)` character from column names

```powerquery-m
Table.TransformColumnNames(Table.FromRecords({[#"Col#(tab)umn" = 1]}), Text.Clean)
```

<table> <tr> <th>Column</th> </tr> <tr> <td>1</td> </tr> </table>

## Example 2
Transform column names to generate case-insensitive names of length 6.

```powerquery-m
Table.TransformColumnNames(
    Table.FromRecords({[ColumnNum = 1, cOlumnnum = 2, coLumnNUM = 3]}), 
    Text.Clean, 
    [MaxLength = 6, Comparer = Comparer.OrdinalIgnoreCase]
)
```

<table> <tr> <th>Column</th> <th>cOlum1</th> <th>coLum2</th> </tr> <tr> <td>1</td> <td>2</td> <td>3</td> </tr> </table>
