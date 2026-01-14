---
description: "Learn more about: Record.FieldCount"
title: "Record.FieldCount"
ms.subservice: m-source
ms.topic: reference
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
