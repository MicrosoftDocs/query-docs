---
description: "Learn more about: CONVERT"
title: "CONVERT function (DAX)"
ms.custom: ExampleTypeAW2020
---
# CONVERT

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Converts an expression of one data type to another.

## Syntax

```dax
CONVERT(<Expression>, <Datatype>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`Expression`|Any valid expression.|
|`Datatype`|An enumeration that includes: BOOLEAN, CURRENCY, DATETIME, DECIMAL, DOUBLE, INT64, INTEGER, LOGICAL, STRING, TEXT.|

## Return value

Returns the value of `Expression`, translated to `Datatype`.

## Remarks

- The function returns an error when a value cannot be converted to the specified data type.

- DAX calculated columns must be of a single data type. Since MEDIAN and MEDIANX functions over an integer column return mixed data types, either integer or double, the following calculated column expression will return an error as a result: 
    ```dax
    MedianOrderQuantity = MEDIAN ( [Order Quantity] )
    ```

- To avoid mixed data types, change the expression to always return the double data type, for example:
    ```dax
    MedianOrderQuantity = MEDIANX('Sales', CONVERT([Order Quantity], DOUBLE))
    ```

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

DAX query

```dax
EVALUATE { CONVERT(DATE(1900, 1, 1), INTEGER) }
```

Returns

|[Value]  |
|---------|
|2     |
