---
title: "Record.Field | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: gepopell
ms.topic: reference
author: dougklopfenstein
ms.author: v-douklo

---
# Record.Field

## Syntax

<pre>
Record.Field(<b>record</b> as record, <b>field</b> as text) as any
</pre> 
  
## About  
Returns the value of the specified `field` in the `record`. If the field is not found, an exception is thrown.

## Example 1
Find the value of field "CustomerID" in the record.

```powerquery-m
Record.Field([CustomerID = 1, Name = "Bob", Phone = "123-4567"], "CustomerID")
```

`1`
