---
description: "Learn more about: Record.Field"
title: "Record.Field | Microsoft Docs"
ms.date: 3/14/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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

**Usage**

```powerquery-m
Record.Field([CustomerID = 1, Name = "Bob", Phone = "123-4567"], "CustomerID")
```

**Output**

`1`
