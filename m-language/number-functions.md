---
title: "Number functions | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "index-page "
ms.assetid: e67be63f-7970-49e2-85f7-01178102d1b5
caps.latest.revision: 13
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Number functions
The Power Query Formula Language is a mashup language for transforming data. It's a functional, case sensitive language similar to F\#. Power Query Formula Language is used in a number of Microsoft products such as Power BI Desktop, Excel, and Analysis Services. To learn more about the language, see [PowerQueryName reference](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## Number  
  
### <a name="__toc360788690"></a>Constants  
  
|Function|Description|  
|------------|---------------|  
|[Number.E](../PowerQuery/number-e.md)|Returns 2.7182818284590451, the value of e up to 16 decimal digits.|
|[Number.Epsilon](../PowerQuery/number-epsilon.md)|Returns the smallest possible number.|
|[Number.NaN](../PowerQuery/number-nan.md)|Represents 0/0.|  
|[Number.NegativeInfinity](../PowerQuery/number-negativeinfinity.md)|Represents -1/0.|  
|[Number.PI](../PowerQuery/number-pi.md)|Returns 3.1415926535897931, the value for Pi up to 16 decimal digits.|
|[Number.PositiveInfinity](../PowerQuery/number-positiveinfinity.md)|Represents 1/0.|  
  
  
### Information  
  
|Function|Description|  
|------------|---------------|  
|[Number.IsEven](../PowerQuery/number-iseven.md)|Returns true if a value is an even number.|
|[Number.IsNaN](../PowerQuery/number-isnan.md)|Returns true if a value is Number.NaN.|  
|[Number.IsOdd](../PowerQuery/number-isodd.md)|Returns true if a value is an odd number.|  
  
### <a name="__toc360788707"></a>Conversion and formatting  
  
|Function|Description|  
|------------|---------------|  
|[Byte.From](../PowerQuery/byte-from.md)|Returns a 8-bit integer number value from the given value.|
|[Currency.From](../PowerQuery/currency-from.md)|Returns a currency value from the given value.|
|[Decimal.From](../PowerQuery/decimal-from.md)|Returns a decimal number value from the given value.|
|[Double.From](../PowerQuery/double-from.md)|Returns a Double number value from the given value.|
|[Int8.From](../PowerQuery/int8-from.md)|Returns a signed 8-bit integer number value from the given value.|  
|[Int16.From](../PowerQuery/int16-from.md)|Returns a 16-bit integer number value from the given value.|  
|[Int32.From](../PowerQuery/int32-from.md)|Returns a 32-bit integer number value from the given value.|  
|[Int64.From](../PowerQuery/int64-from.md)|Returns a 64-bit integer number value from the given value.|
|[Number.From](../PowerQuery/number-from.md)|Returns a number value from a value.|
|[Number.FromText](../PowerQuery/number-fromtext.md)|Returns a number value from a text value.|  
|[Number.ToText](../PowerQuery/number-totext.md)|Returns a text value from a number value.|  
|[Percentage.From](../PowerQuery/percentage-from.md)|Returns a percentage value from the given value.|
|[Single.From](../PowerQuery/single-from.md)|Returns a Single number value from the given value.|  
  
  
### Rounding  
  
|Function|Description|  
|------------|---------------|  
|[Number.Round](../PowerQuery/number-round.md)|Returns a nullable number (n) if value is an integer.|
|[Number.RoundAwayFromZero](../PowerQuery/number-roundawayfromzero.md)|Returns Number.RoundUp(value) when value &gt;= 0 and Number.RoundDown(value) when value &lt; 0.|
|[Number.RoundDown](../PowerQuery/number-rounddown.md)|Returns the largest integer less than or equal to a number value.|
|[Number.RoundTowardZero](../PowerQuery/number-roundtowardzero.md)|Returns Number.RoundDown(x) when x &gt;= 0 and Number.RoundUp(x) when x &lt; 0.|
|[Number.RoundUp](../PowerQuery/number-roundup.md)|Returns the larger integer greater than or equal to a number value.|  
  
  
  
### Operations  
  
|Function|Description|  
|------------|---------------|  
|[Number.Abs](../PowerQuery/number-abs.md)|Returns the absolute value of a number.|  
|[Number.Combinations](../PowerQuery/number-combinations.md)|Returns the number of combinations of a given number of items for the optional combination size.|
|[Number.Exp](../PowerQuery/number-exp.md)|Returns a number representing *e* raised to a power.|
|[Number.Factorial](../PowerQuery/number-factorial.md)|Returns the factorial of a number.|
|[Number.IntegerDivide](../PowerQuery/number-integerdivide.md)|Divides two numbers and returns the whole part of the resulting number.|
|[Number.Ln](../PowerQuery/number-ln.md)|Returns the natural logarithm of a number.|  
|[Number.Log](../PowerQuery/number-log.md)|Returns the logarithm of a number to the base.|  
|[Number.Log10](../PowerQuery/number-log10.md)|Returns the base-10 logarithm of a number.|
|[Number.Mod](../PowerQuery/number-mod.md)|Divides two numbers and returns the remainder of the resulting number.|
|[Number.Permutations](../PowerQuery/number-permutations.md)|Returns the number of total permutatons of a given number of items for the optional permutation size.|
|[Number.Power](../PowerQuery/number-power.md)|Returns a number raised by a power.|
|[Number.Sign](../PowerQuery/number-sign.md)|Returns 1 for positive numbers, -1 for negative numbers or 0 for zero.|  
|[Number.Sqrt](../PowerQuery/number-sqrt.md)|Returns the square root of a number.|  
  
### Random  
  
|Function|Description|  
|------------|---------------|  
|[Number.Random](../PowerQuery/number-random.md)|Returns a random fractional number between 0 and 1.|  
|[Number.RandomBetween](../PowerQuery/number-randombetween.md)|Returns a random number between the two given number values.|  
  
### Trigonometry  
  
|Function|Description|  
|------------|---------------|  
|[Number.Acos](../PowerQuery/number-acos.md)|Returns the arccosine of a number.|  
|[Number.Asin](../PowerQuery/number-asin.md)|Returns the arcsine of a number.|  
|[Number.Atan](../PowerQuery/number-atan.md)|Returns the arctangent of a number.|  
|[Number.Atan2](../PowerQuery/number-atan2.md)|Returns the arctangent of the division of two numbers.|  
|[Number.Cos](../PowerQuery/number-cos.md)|Returns the cosine of a number.|  
|[Number.Cosh](../PowerQuery/number-cosh.md)|Returns the hyperbolic cosine of a number.|  
|[Number.Sin](../PowerQuery/number-sin.md)|Returns the sine of a number.|  
|[Number.Sinh](../PowerQuery/number-sinh.md)|Returns the hyperbolic sine of a number.|  
|[Number.Tan](../PowerQuery/number-tan.md)|Returns the tangent of a number.|  
|[Number.Tanh](../PowerQuery/number-tanh.md)|Returns the hyperbolic tangent of a number.|  
  
### Bytes  
  
|Function|Description|  
|------------|---------------|  
|[Number.BitwiseAnd](../PowerQuery/number-bitwiseand.md)|Returns the result of a bitwise AND operation on the provided operands.|  
|[Number.BitwiseNot](../PowerQuery/number-bitwisenot.md)|Returns the result of a bitwise NOT operation on the provided operands.|  
|[Number.BitwiseOr](../PowerQuery/number-bitwiseor.md)|Returns the result of a bitwise OR operation on the provided operands.|  
|[Number.BitwiseShiftLeft](../PowerQuery/number-bitwiseshiftleft.md)|Returns the result of a bitwise shift left operation on the operands.|  
|[Number.BitwiseShiftRight](../PowerQuery/number-bitwiseshiftright.md)|Returns the result of a bitwise shift right operation on the operands.|  
|[Number.BitwiseXor](../PowerQuery/number-bitwisexor.md)|Returns the result of a bitwise XOR operation on the provided operands.|  

Parameter values | Description
---------------- | -----------
[RoundingMode.AwayFromZero](../PowerQuery/roundingmode-awayfromzero.md) | RoundingMode.AwayFromZero
[RoundingMode.Down](../PowerQuery/roundingmode-down.md) | RoundingMode.Down
[RoundingMode.ToEven](../PowerQuery/roundingmode-toeven.md) | RoundingMode.ToEven
[RoundingMode.TowardZero](../PowerQuery/roundingmode-towardzero.md) | RoundingMode.TowardZero
[RoundingMode.Up](../PowerQuery/roundingmode-up.md) | RoundingMode.Up 
