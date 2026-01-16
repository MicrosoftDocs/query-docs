---
description: "Learn more about: Record.Field"
title: "Record.Field"
ms.subservice: m-source
---
# Record.Field

## Syntax

<pre>
Record.Field(<b>record</b> as record, <b>field</b> as text) as any
</pre>
  
## About

Returns the value of the specified `field` in the `record`. If the field is not found, an error is raised.

## Example 1

Find the value of field "CustomerID" in the record.

**Usage**

```powerquery-m
Record.Field([CustomerID = 1, Name = "Bob", Phone = "123-4567"], "CustomerID")
```

**Output**

`1`
