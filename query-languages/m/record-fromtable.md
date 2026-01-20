---
description: "Learn more about: Record.FromTable"
title: "Record.FromTable"
ms.subservice: m-source
ms.topic: reference
---
# Record.FromTable

## Syntax

<pre>
Record.FromTable(<b>table</b> as table) as record  
</pre>
  
## About

Returns a record from a table of records `table` containing field names and value names `{[Name = name, Value = value]}`. An error is raised if the field names are not unique.

## Example 1

Create a record from the table of the form Table.FromRecords({[Name = "CustomerID", Value = 1], [Name = "Name", Value = "Bob"], [Name = "Phone", Value = "123-4567"]}).

**Usage**

```powerquery-m
Record.FromTable(
    Table.FromRecords({
        [Name = "CustomerID", Value = 1],
        [Name = "Name", Value = "Bob"],
        [Name = "Phone", Value = "123-4567"]
    })
)
```

**Output**

`[CustomerID = 1, Name = "Bob", Phone = "123-4567"]`
