---
description: "Learn more about: Record.FieldCount"
title: "Record.FieldCount | Microsoft Docs"
ms.date: 3/14/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

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

**Usage**

```powerquery-m
Record.FieldCount([CustomerID = 1, Name = "Bob"])
```

**Output**

`2`
