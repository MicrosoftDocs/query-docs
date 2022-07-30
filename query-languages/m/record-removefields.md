---
description: "Learn more about: Record.RemoveFields"
title: "Record.RemoveFields"
ms.date: 3/9/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Record.RemoveFields

## Syntax

<pre>
Record.RemoveFields(<b>record</b> as record, <b>fields</b> as any, optional <b>missingField</b> as nullable number) as record
</pre>
  
## About

Returns a record that removes all the fields specified in list `fields` from the input `record`. If the field specified does not exist, an exception is thrown.

## Example 1

Remove the field "Price" from the record.

**Usage**

```powerquery-m
Record.RemoveFields([CustomerID = 1, Item = "Fishing rod", Price = 18.00], "Price")
```

**Output**

`[CustomerID = 1, Item = "Fishing rod"]`

## Example 2

Remove the fields "Price" and "Item" from the record.

**Usage**

```powerquery-m
Record.RemoveFields([CustomerID = 1, Item = "Fishing rod", Price = 18.00], {"Price", "Item"})
```

**Output**

`[CustomerID = 1]`
