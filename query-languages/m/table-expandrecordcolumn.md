---
title: "Table.ExpandRecordColumn | Microsoft Docs"
ms.date: 4/20/2020
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Table.ExpandRecordColumn

## Syntax

<pre>
Table.ExpandRecordColumn(<b>table</b> as table, <b>column</b> as text, <b>fieldNames</b> as list, optional <b>newColumnNames</b> as nullable list) as table 
</pre>
  
## About  
Given the `column` of records in the input `table`, creates a table with a column for each field in the record. Optionally, `newColumnNames` may be specified to ensure unique names for the columns in the new table. <ul> <li><code>table</code>: The original table with the record column to expand. </li> <li><code>column</code>: The column to expand.</li> <li><code>fieldNames</code>: The list of fields to expand into columns in the table.</li> <li><code>newColumnNames</code>: The list of column names to give the new columns. The new column names cannot duplicate any column in the new table.</li> </ul>

## Example 1
Expand column [a] in the table `({[a = [aa = 1, bb = 2, cc = 3], b = 2]})` into 3 columns "aa", "bb" and "cc".

```powerquery-m
Table.ExpandRecordColumn( 
    Table.FromRecords({ 
        [ 
            a = [aa = 1, bb = 2, cc = 3], 
            b = 2 
        ] 
    }), 
    "a", 
    {"aa", "bb", "cc"} 
)
```

<table> <tr> <th>aa</th> <th>bb</th> <th>cc</th> <th>b</th> </tr> <tr> <td>1</td> <td>2</td> <td>3</td> <td>2</td> </tr> </table>
