---
description: "Learn more about: Record.Combine"
title: "Record.Combine"
ms.subservice: m-source
---
# Record.Combine

## Syntax

<pre>
Record.Combine(<b>records</b> as list) as record
</pre>
  
## About

Combines the records in the given `records`. If the `records` contains non-record values, an error is returned.

## Example 1

Create a combined record from the records.

**Usage**

```powerquery-m
Record.Combine({
    [CustomerID = 1, Name = "Bob"],
    [Phone = "123-4567"]
})
```

**Output**

`[CustomerID = 1, Name = "Bob", Phone = "123-4567"]`
