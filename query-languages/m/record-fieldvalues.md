---
title: "Record.FieldValues | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.FieldValues

## Syntax

<pre>
Record.FieldValues(<b>record</b> as record) as list
</pre>
  
## About  
Returns a list of the field values in record `record`.

## Example 1
Find the field values in the record.

```powerquery-m
Record.FieldValues([CustomerID = 1, Name = "Bob", Phone = "123-4567"])
```

<table> <tr><td>1</td></tr> <tr><td>Bob</td></tr> <tr><td>123-4567</td></tr> </table>
