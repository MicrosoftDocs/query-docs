---
description: "Learn more about: Record.ReorderFields"
title: "Record.ReorderFields"
ms.subservice: m-source
ms.topic: reference
---
# Record.ReorderFields

## Syntax

<pre>
Record.ReorderFields(
    <b>record</b> as record,
    <b>fieldOrder</b> as list,
    optional <b>missingField</b> as nullable number
) as record
</pre>
  
## About

Reorders the fields of a record to match the order of a list of field names.

* `record`: The record containing the fields to reorder.
* `fieldOrder`: A list containing the new order of the fields to apply to the record. Field values are maintained and fields not listed in this parameter are left in their original positions.
* `missingField`: Specifies the expected action for missing values in a row that contains fewer fields than expected. The following values are valid:
  * `MissingField.Error`: (Default) Indicates that missing fields should result in an error. If no value is entered for the `missingField` parameter, this value is used.
  * `MissingField.Ignore`: Indicates that missing fields should be ignored.
  * `MissingField.UseNull`: Indicates that missing fields should be included as `null` values.

## Example 1

Reorder some of the fields in the record.

**Usage**

```powerquery-m
Record.ReorderFields(
    [CustomerID = 1, OrderID = 1, Item = "Fishing rod", Price = 100.0],
    {"OrderID", "CustomerID"}
)
```

**Output**

`[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0]`

## Example 2

Reorder some of the fields in the record and include `null` for any missing fields.

**Usage**

```powerquery-m
let
    Source = [CustomerID = 3, First Name = "Paul", Phone = "543-7890", Purchase = "Fishing Rod"],
    reorderedRecord = Record.ReorderFields(
        Source, 
        {"Purchase", "Last Name", "First Name"}, 
        MissingField.UseNull
    )
in
    reorderedRecord
```

**Output**

`[CustomerID = 3, Purchase = "Fishing Rod", Phone = "543-7890", Last Name = null, First Name = "Paul"]`
