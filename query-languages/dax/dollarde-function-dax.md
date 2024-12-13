---
description: "Learn more about: DOLLARDE"
title: "DOLLARDE function (DAX)"
author: jajin7
---

# DOLLARDE

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Converts a dollar price expressed as an integer part and a fraction part, such as 1.02, into a dollar price expressed as a decimal number. Fractional dollar numbers are sometimes used for security prices.

## Syntax

```dax
DOLLARDE(<fractional_dollar>, <fraction>)
```

### Parameters

|Term|Definition|  
|--------|--------------|  
|`fractional_dollar`|A number expressed as an integer part and a fraction part, separated by a decimal symbol.|
|`fraction`|The integer to use in the denominator of the fraction.|

## Return Value

The decimal value of `fractional_dollar`.

## Remarks

- The fraction part of the value is divided by an integer that you specify. For example, if you want your price to be expressed to a precision of 1/16 of a dollar, you divide the fraction part by 16. In this case, 1.02 represents \\$1.125 (\\$1 + 2/16 = \\$1.125).

- fraction is rounded to the nearest integer.

- An error is returned if:
  - fraction < 1.

- [!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following DAX query:

```dax
EVALUATE
{
  DOLLARDE(1.02, 16)
}
```

Returns 1.125, the decimal price of the original fractional price, 1.02, read as 1 and 2/16. Since the fraction value is 16, the price has a precision of 1/16 of a dollar.
