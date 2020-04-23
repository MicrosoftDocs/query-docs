---
title: "Table.ReplaceErrorValues | Microsoft Docs"
ms.date: 4/23/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.ReplaceErrorValues

## Syntax

<pre>
Table.ReplaceErrorValues(<b>table</b> as table, <b>errorReplacement</b> as list) as table
</pre>
  
## About  
Replaces the error values in the specified columns of the `table` with the new values in the `errorReplacement` list. The format of the list is {{column1, value1}, …}. There may only be one replacement value per column, specifying the column more than once will result in an error.

## Example 1
Replace the error value with the text "world" in the table.

```powerquery-m
Table.ReplaceErrorValues(
    Table.FromRows({{1, "hello"}, {3, ...}}, {"A", "B"}), 
    {"B", "world"}
)
```

<table> <tr> <th>A</th> <th>B</th> </tr> <tr> <td>1</td> <td>hello</td> </tr> <tr> <td>3</td> <td>world</td> </tr> </table>

## Example 2
Replace the error value in column A with the text "hello" and in column B with the text "world" in the table.

```powerquery-m
Table.ReplaceErrorValues(
    Table.FromRows({{..., ...}, {1, 2}}, {"A", "B"}), 
    {{"A", "hello"}, {"B", "world"}}
)
```

<table> <tr> <th>A</th> <th>B</th> </tr> <tr> <td>hello</td> <td>world</td> </tr> <tr> <td>1</td> <td>2</td> </tr> </table>
