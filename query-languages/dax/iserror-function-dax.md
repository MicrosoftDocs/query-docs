---
description: "Learn more about: ISERROR"
title: "ISERROR function (DAX)"
---
# ISERROR

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Checks whether a value is an error, and returns `TRUE` or `FALSE`.

## Syntax

```dax
ISERROR(<value>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`value`|The value you want to test.|

## Return value

A Boolean value of `TRUE` if the value is an error; otherwise `FALSE`.

## Remarks

- For best practices when using ISERROR, see [Appropriate use of error functions](best-practices/dax-error-functions.md).

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following example calculates the ratio of total Internet sales to total reseller sales. The ISERROR function is used to check for errors, such as division by zero. If there is an error a blank is returned, otherwise the ratio is returned.

```dax
= IF( ISERROR(
       SUM('ResellerSales_USD'[SalesAmount_USD])
       /SUM('InternetSales_USD'[SalesAmount_USD])
             )
    , BLANK()
    , SUM('ResellerSales_USD'[SalesAmount_USD])
      /SUM('InternetSales_USD'[SalesAmount_USD])
    )
```

## Related content

[Information functions](information-functions-dax.md)
[IFERROR function](iferror-function-dax.md)
[IF function](if-function-dax.md)
