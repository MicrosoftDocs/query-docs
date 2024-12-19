---
description: "Learn more about: SIN"
title: "SIN function (DAX)"
---
# SIN

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns the sine of the given angle.

## Syntax

```dax
SIN(number)
```

### Parameters

|Term|Definition|
|--------|--------------|
|`number`|Required. The angle in radians for which you want the sine.|

## Return value

Returns the sine of the given angle.

## Remarks

If an argument is in degrees, multiply it by `PI()/180` or use the RADIANS function to convert it to radians.

## Example

|Formula|Description|Result|
|-----------|---------------|----------|
|`= SIN(PI())`|Sine of pi radians (0, approximately).|0.0|
|`= SIN(PI()/2)`|Sine of pi/2 radians.|1.0|
|`= SIN(30*PI()/180)`|Sine of 30 degrees.|0.5|
|`= SIN(RADIANS(30))`|Sine of 30 degrees.|0.5|
