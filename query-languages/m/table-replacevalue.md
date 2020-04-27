---
title: "Table.ReplaceValue | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.ReplaceValue

## Syntax

<pre>
Table.ReplaceValue(<b>table</b> as table, <b>oldValue</b> as any, <b>newValue</b> as any, <b>replacer</b> as function, <b>columnsToSearch</b> as list) as table
</pre>
  
## About  
Replaces `oldValue` with `newValue` in the specified columns of the `table`.

## Example 1
Replace the text "goodbye" with the text "world" in the table.

```powerquery-m
Table.ReplaceValue(
    Table.FromRecords({
        [a = 1, b = "hello"],
        [a = 3, b = "goodbye"]
    }),
    "goodbye",
    "world",
    Replacer.ReplaceText,
    {"b"}
)
```

<table> <tr> <th>a</th> <th>b</th> </tr> <tr> <td>1</td> <td>hello</td> </tr> <tr> <td>3</td> <td>world</td> </tr> </table>

## Example 2
Replace the text "ur" with the text "or" in the table.

```powerquery-m
Table.ReplaceValue(
    Table.FromRecords({
        [a = 1, b = "hello"],
        [a = 3, b = "wurld"]
    }),
    "ur",
    "or",
    Replacer.ReplaceText,
    {"b"}
)
```

<table> <tr> <th>a</th> <th>b</th> </tr> <tr> <td>1</td> <td>hello</td> </tr> <tr> <td>3</td> <td>world</td> </tr> </table>
