---
description: "Learn more about: ATAN"
title: "ATAN function (DAX)"
---
# ATAN

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the arctangent, or inverse tangent, of a number. The arctangent is the angle whose tangent is `number`. The returned angle is given in radians in the range -pi/2 to pi/2.

## Syntax

```dax
ATAN(number)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`number`|The tangent of the angle you want.|

## Return value

Returns the inverse tangent of a number.

## Remarks

To express the arctangent in degrees, multiply the result by 180/PI( ) or use the DEGREES function.

## Example

|Formula|Description|Result|
|-----------|---------------|----------|
|`= ATAN(1)`|Arctangent of 1 in radians, pi/4|0.785398163|
|`= ATAN(1)*180/PI()`|Arctangent of 1 in degrees|45|
