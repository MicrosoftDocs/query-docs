---
title: "Record.TransformFields | Microsoft Docs"
ms.date: 8/1/2019
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.TransformFields

## Syntax

<pre>
Record.TransformFields(<b>record</b> as record, <b>transformOperations</b> as list, optional <b>missingField</b> as nullable number) as record
</pre>

## About
Returns a record after applying transformations specified in list `transformOperations` to `record`. One or more fields may be transformed at a given time. <div>In the case of a single field being transformed, `transformOperations` is expected to be a list with two items. The first item in `transformOperations` specifies a field name, and the second item in `transformOperations` specifies the function to be used for transformation. For example, `{"Quantity", Number.FromText}`</div> <div>In the case of a multiple fields being transformed, `transformOperations` is expected to be a list of lists, where each inner list is a pair of field name and transformation operation. For example, `{{"Quantity",Number.FromText},{"UnitPrice", Number.FromText}}`</div>

## Example 1
Convert "Price" field to number.

```powerquery-m
Record.TransformFields([OrderID = 1, CustomerID= 1, Item = "Fishing rod", Price = "100.0"], {"Price", Number.FromText})
```

<table> <tr> <th>OrderID</th> <td>1</td> </tr> <tr> <th>CustomerID</th> <td>1</td> </tr> <tr> <th>Item</th> <td>Fishing rod</td> </tr> <tr> <th>Price</th> <td>100</td> </tr> </table>

## Example 2
Convert "OrderID" and "Price" fields to numbers.

```powerquery-m
Record.TransformFields( [OrderID ="1", CustomerID= 1, Item = "Fishing rod", Price = "100.0"], {{"OrderID", Number.FromText}, {"Price",Number.FromText}})
```

<table> <tr> <th>OrderID</th> <td>1</td> </tr> <tr> <th>CustomerID</th> <td>1</td> </tr> <tr> <th>Item</th> <td>Fishing rod</td> </tr> <tr> <th>Price</th> <td>100</td> </tr> </table>
