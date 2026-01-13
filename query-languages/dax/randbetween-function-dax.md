---
description: "Learn more about: RANDBETWEEN"
title: "RANDBETWEEN function (DAX)"
ms.topic: reference
---
# RANDBETWEEN

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns a random number in the range between two numbers you specify.

## Syntax

```dax
RANDBETWEEN(<bottom>,<top>)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`Bottom`|The smallest integer the function will return.|
|`Top`|The largest integer the function will return.|

## Return value

A whole number.

## Remarks

[!INCLUDE [function-not-supported-in-directquery-mode](includes/function-not-supported-in-directquery-mode.md)]

## Example

The following formula returns a random number between 1 and 10.

```dax
= RANDBETWEEN(1,10)
```

## Related content

[Math and Trig functions](math-and-trig-functions-dax.md)
[Statistical functions](statistical-functions-dax.md)
