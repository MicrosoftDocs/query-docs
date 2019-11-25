---
title: "Record.FieldCount | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Record.FieldCount

## Syntax

<pre>
Record.FieldCount(<b>record</b> as record) as number 
</pre>
  
## About  
Returns the number of fields in the record `record`.

## Example 1
Find the number of fields in the record.

```powerquery-m
Record.FieldCount([CustomerID = 1, Name = "Bob"])
```

`2`
