---
description: "Learn more about: Number functions"
title: "Number functions | Microsoft Docs"
ms.date: 5/5/2022
ms.service: powerquery

ms.reviewer: ehvonleh
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan

---
# Number functions

These functions create and manipulate number values.

## Number

### Information

|Function|Description|  
|------------|---------------|  
|[Number.IsEven](number-iseven.md)|Returns true if a value is an even number.|
|[Number.IsNaN](number-isnan.md)|Returns true if a value is Number.NaN.|  
|[Number.IsOdd](number-isodd.md)|Returns true if a value is an odd number.|  

### Conversion and formatting  

|Function|Description|
|------------|---------------|
|[Byte.From](byte-from.md)|Returns a 8-bit integer number value from the given value.|
|[Currency.From](currency-from.md)|Returns a currency value from the given value.|
|[Decimal.From](decimal-from.md)|Returns a decimal number value from the given value.|
|[Double.From](double-from.md)|Returns a Double number value from the given value.|
|[Int8.From](int8-from.md)|Returns a signed 8-bit integer number value from the given value.|
|[Int16.From](int16-from.md)|Returns a 16-bit integer number value from the given value.|
|[Int32.From](int32-from.md)|Returns a 32-bit integer number value from the given value.|
|[Int64.From](int64-from.md)|Returns a 64-bit integer number value from the given value.|
|[Number.From](number-from.md)|Returns a number value from a value.|
|[Number.FromText](number-fromtext.md)|Returns a number value from a text value.|
|[Number.ToText](number-totext.md)|Returns a text value from a number value.|
|[Percentage.From](percentage-from.md)|Returns a percentage value from the given value.|
|[Single.From](single-from.md)|Returns a Single number value from the given value.|

### Rounding

|Function|Description|
|------------|---------------|
|[Number.Round](number-round.md)|Returns a nullable number (n) if value is an integer.|
|[Number.RoundAwayFromZero](number-roundawayfromzero.md)|Returns Number.RoundUp(value) when value &gt;= 0 and Number.RoundDown(value) when value &lt; 0.|
|[Number.RoundDown](number-rounddown.md)|Returns the largest integer less than or equal to a number value.|
|[Number.RoundTowardZero](number-roundtowardzero.md)|Returns Number.RoundDown(x) when x &gt;= 0 and Number.RoundUp(x) when x &lt; 0.|
|[Number.RoundUp](number-roundup.md)|Returns the larger integer greater than or equal to a number value.|  

### Operations

|Function|Description|
|------------|---------------|
|[Number.Abs](number-abs.md)|Returns the absolute value of a number.|
|[Number.Combinations](number-combinations.md)|Returns the number of combinations of a given number of items for the optional combination size.|
|[Number.Exp](number-exp.md)|Returns a number representing *e* raised to a power.|
|[Number.Factorial](number-factorial.md)|Returns the factorial of a number.|
|[Number.IntegerDivide](number-integerdivide.md)|Divides two numbers and returns the whole part of the resulting number.|
|[Number.Ln](number-ln.md)|Returns the natural logarithm of a number.|
|[Number.Log](number-log.md)|Returns the logarithm of a number to the base.|
|[Number.Log10](number-log10.md)|Returns the base-10 logarithm of a number.|
|[Number.Mod](number-mod.md)|Divides two numbers and returns the remainder of the resulting number.|
|[Number.Permutations](number-permutations.md)|Returns the number of total permutations of a given number of items for the optional permutation size.|
|[Number.Power](number-power.md)|Returns a number raised by a power.|
|[Number.Sign](number-sign.md)|Returns 1 for positive numbers, -1 for negative numbers or 0 for zero.|
|[Number.Sqrt](number-sqrt.md)|Returns the square root of a number.|

### Random

|Function|Description|
|------------|---------------|
|[Number.Random](number-random.md)|Returns a random fractional number between 0 and 1.|
|[Number.RandomBetween](number-randombetween.md)|Returns a random number between the two given number values.|

### Trigonometry

|Function|Description|
|------------|---------------|
|[Number.Acos](number-acos.md)|Returns the arccosine of a number.|
|[Number.Asin](number-asin.md)|Returns the arcsine of a number.|
|[Number.Atan](number-atan.md)|Returns the arctangent of a number.|
|[Number.Atan2](number-atan2.md)|Returns the arctangent of the division of two numbers.|
|[Number.Cos](number-cos.md)|Returns the cosine of a number.|
|[Number.Cosh](number-cosh.md)|Returns the hyperbolic cosine of a number.|
|[Number.Sin](number-sin.md)|Returns the sine of a number.|
|[Number.Sinh](number-sinh.md)|Returns the hyperbolic sine of a number.|
|[Number.Tan](number-tan.md)|Returns the tangent of a number.|
|[Number.Tanh](number-tanh.md)|Returns the hyperbolic tangent of a number.|

### Bytes

|Function|Description|
|------------|---------------|
|[Number.BitwiseAnd](number-bitwiseand.md)|Returns the result of a bitwise AND operation on the provided operands.|
|[Number.BitwiseNot](number-bitwisenot.md)|Returns the result of a bitwise NOT operation on the provided operands.|
|[Number.BitwiseOr](number-bitwiseor.md)|Returns the result of a bitwise OR operation on the provided operands.|
|[Number.BitwiseShiftLeft](number-bitwiseshiftleft.md)|Returns the result of a bitwise shift left operation on the operands.|
|[Number.BitwiseShiftRight](number-bitwiseshiftright.md)|Returns the result of a bitwise shift right operation on the operands.|
|[Number.BitwiseXor](number-bitwisexor.md)|Returns the result of a bitwise XOR operation on the provided operands.|

## See also

[Number constants](number-constants.md)
[Number enumerations](number-enumerations.md)
