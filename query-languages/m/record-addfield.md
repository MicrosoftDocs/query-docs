---
description: "Learn more about: Record.AddField"
title: "Record.AddField"
ms.subservice: m-source
---
# Record.AddField

## Syntax

<pre>
Record.AddField(
    <b>record</b> as record,
    <b>fieldName</b> as text,
    <b>value</b> as any,
    optional <b>delayed</b> as nullable logical
) as record
</pre>
  
## About

Adds a field to a record `record`, given the name of the field `fieldName` and the value `value`.

## Example 1

Add the field Address to the record.

**Usage**

```powerquery-m
Record.AddField([CustomerID = 1, Name = "Bob", Phone = "123-4567"], "Address", "123 Main St.")
```

**Output**

`[CustomerID = 1, Name = "Bob", Phone = "123-4567", Address = "123 Main St."]`
