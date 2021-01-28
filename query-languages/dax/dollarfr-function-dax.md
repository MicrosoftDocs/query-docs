---
description: "Learn more about: DOLLARFR"
title: "DOLLARFR function (DAX) | Microsoft Docs"
ms.service: powerbi
ms.date: 07/02/2020
ms.reviewer: owend
ms.topic: reference
author: jajin7
ms.author: owend

---

# DOLLARFR

Converts a dollar price expressed as a decimal number into a dollar price expressed as an integer part and a fraction part, such as 1.02. Fractional dollar numbers are sometimes used for security prices.

## Syntax

```dax
DOLLARFR(<decimal_dollar>, <fraction>)
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|decimal_dollar|A decimal number.|
|fraction|The integer to use in the denominator of the fraction.|

## Return Value

The fractional value of *decimal_dollar*, expressed as an integer part and a fraction part.

## Remarks

- fraction is rounded to the nearest integer.

- An error is returned if:
  - fraction < 1.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following DAX query:

```dax
EVALUATE
{
  DOLLARFR(1.125, 16)
}
```

Returns 1.02, read as 1 and 2/16, which is the corresponding fraction price of the original decimal price, 1.125. Since the fraction value is 16, the price has a precision of 1/16 of a dollar.
