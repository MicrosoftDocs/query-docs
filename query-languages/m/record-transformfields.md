---
description: "Learn more about: Record.TransformFields"
title: "Record.TransformFields | Microsoft Docs"
ms.date: 5/19/2022
ms.service: powerquery

ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Record.TransformFields

## Syntax

<pre>
Record.TransformFields(<b>record</b> as record, <b>transformOperations</b> as list, optional <b>missingField</b> as nullable number) as record
</pre>

## About

Returns a record after applying transformations specified in list `transformOperations` to `record`. One or more fields may be transformed at a given time.

In the case of a single field being transformed, `transformOperations` is expected to be a list with two items. The first item in `transformOperations` specifies a field name, and the second item in `transformOperations` specifies the function to be used for transformation. For example, `{"Quantity", Number.FromText}`

In the case of a multiple fields being transformed, `transformOperations` is expected to be a list of lists, where each inner list is a pair of field name and transformation operation. For example, `{{"Quantity",Number.FromText},{"UnitPrice", Number.FromText}}`

## Example 1

Convert "Price" field to number.

**Usage**

```powerquery-m
Record.TransformFields(
    [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = "100.0"],
    {"Price", Number.FromText}
)
```

**Output**

`[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100]`

## Example 2

Convert "OrderID" and "Price" fields to numbers.

**Usage**

```powerquery-m
Record.TransformFields(
    [OrderID = "1", CustomerID = 1, Item = "Fishing rod", Price = "100.0"],
    {{"OrderID", Number.FromText}, {"Price", Number.FromText}}
)
```

**Output**

`[OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100]`
