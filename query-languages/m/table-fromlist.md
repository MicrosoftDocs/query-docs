---
title: "Table.FromList | Microsoft Docs"
ms.date: 4/23/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Table.FromList

## Syntax

<pre>
Table.FromList(<b>list</b> as list, optional <b>splitter</b> as nullable function, optional <b>columns</b> as any, optional <b>default</b> as any, optional <b>extraValues</b> as nullable number) as table 
</pre>
  
## About  
Converts a list, `list` into a table by applying the optional splitting function, `splitter`, to each item in the list. By default, the list is assumed to be a list of text values that is split by commas. Optional `columns` may be the number of columns, a list of columns or a TableType. Optional `default` and `extraValues` may also be specified.

## Example 1
Create a table from the list with the column named "Letters" using the default splitter.

```powerquery-m
Table.FromList({"a", "b", "c", "d"}, null, {"Letters"})
```

<table> <tr> <th>Letters</th> </tr> <tr> <td>a</td> </tr> <tr> <td>b</td> </tr> <tr> <td>c</td> </tr> <tr> <td>d</td> </tr> </table>

## Example 2
Create a table from the list using the Record.FieldValues splitter with the resulting table having "CustomerID" and "Name" as column names.

```powerquery-m
Table.FromList(
    {
        [CustomerID = 1, Name = "Bob"],
        [CustomerID = 2, Name = "Jim"]
    },
    Record.FieldValues,
    {"CustomerID", "Name"}
)
```

<table> <tr> <th>CustomerID</th> <th>Name</th> </tr> <tr> <td>1</td> <td>Bob</td> </tr> <tr> <td>2</td> <td>Jim</td> </tr> </table>
