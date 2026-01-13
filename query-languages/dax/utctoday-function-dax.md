---
description: "Learn more about: UTCTODAY"
title: "UTCTODAY function (DAX)"
ms.topic: reference
---
# UTCTODAY

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the current UTC date.

## Syntax

```dax
UTCTODAY()
```

## Return value

A date.

## Remarks

- UTCTODAY returns the time value 12:00:00 PM for all dates.

- The UTCNOW function is similar but returns the exact time and date.

## Example

The following:

```dax
EVALUATE { FORMAT(UTCTODAY(), "General Date") }
```

Returns:

|[Value]  |
|---------|
|2/2/2018    |

## Related content

[NOW function](now-function-dax.md)
[UTCNOW function](utcnow-function-dax.md)
