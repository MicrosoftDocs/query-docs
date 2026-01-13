---
description: "Learn more about: ORDERBY"
title: "ORDERBY function (DAX)"
ms.topic: reference
---

# ORDERBY

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Defines the expressions that determine the sort order within each of a window function’s partitions.

## Syntax

```dax
ORDERBY ( [<orderBy_expression>[, <order>[, <orderBy_expression>[, <order>]] …]] )
```

### Parameters

|Term|Definition|
|--------|--------------|
|`orderBy_expression`|(Optional) Any scalar expression that will be used used to sort the data within each of a window function’s partitions.|
|`order`|(Optional) A two-part value of the form "`OrderDirection` [`BlankHandling`]".<br><br> `OrderDirection` specifies how to sort `orderBy_expression` values (i.e. ascending or descending). Valid values include:<br> `DESC`. Alternative value: `0`(zero)/`FALSE`. Sorts in descending order of values of `orderBy_expression`. <br> `ASC`. Alternative value: `1`/`TRUE`. Sorts in ascending order of values of `orderBy_expression`. This is the default value if `order` is omitted.<br><br> `BlankHandling` part is optional. It specifies how blanks are ordered. Valid values include:<br> `BLANKS DEFAULT`. This is the default value. The behavior for numerical values is blank values are ordered between zero and negative values. The behavior for strings is blank values are ordered before all strings, including empty strings. <br> `BLANKS FIRST`. Blanks are always ordered on the beginning, regardless of ascending or descending sorting order. <br> `BLANKS LAST`. Blanks are always ordered on the end, regardless of ascending or descending sorting order.|

## Return value

This function does not return a value.

## Remarks

This function can only be used within a window function expression.

## Example

See [OFFSET](offset-function-dax.md).

## Related content

[Understanding ORDERBY, PARTITIONBY, and MATCHBY functions](../dax/best-practices/dax-understand-orderby.md)
[INDEX](index-function-dax.md)
[OFFSET](offset-function-dax.md)
[PARTITIONBY](partitionby-function-dax.md)
[MATCHBY](matchby-function-dax.md)
[WINDOW](window-function-dax.md)
[RANK](rank-function-dax.md)
[ROWNUMBER](rownumber-function-dax.md)

