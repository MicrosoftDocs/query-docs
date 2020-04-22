---
title: "Table.ToRecords | Microsoft Docs"
ms.date: 4/21/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.ToRecords


## Syntax

<pre>
Table.ToRecords(<b>table</b> as table) as list  
</pre>
  

## About  
Converts a table, <code>table</code>, to a list of records.

  
## Example  
  
Convert the table to a list of records.

```powerquery-m
Table.ToRecords(
    Table.FromRows(
        {
            {1, "Bob", "123-4567"} , 
            {2, "Jim", "987-6543"}, 
            {3, "Paul", "543-7890"} 
        },
        {"CustomerID", "Name", "Phone"}
    )
)
```

<table> <tr><td>[Record]</td></tr> <tr><td>[Record]</td></tr> <tr><td>[Record]</td></tr> </table>
