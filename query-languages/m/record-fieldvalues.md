---
description: "Learn more about: Record.FieldValues"
title: "Record.FieldValues"
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

**Usage**

```powerquery-m
Record.FieldValues([CustomerID = 1, Name = "Bob", Phone = "123-4567"])
```

**Output**

`{1, "Bob", "123-4567"}`
