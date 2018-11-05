---
title: "Number.Round | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Number.Round

  
## About  
Returns a nullable number (n) if value is an integer.  
  
## Syntax

<pre>
Number.Round(value as nullable number, digits as nullable number,  roundingMode as nullable number) as nullable number  
</pre> 
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Integer value to round.|  
|digits|Fractional part is rounded by digits.|  
|roundingMode|Specifies rounding direction when there is a tie between the possible numbers to round to. For Example, when the last digit of the number being rounded is 5 such as. 1.5 or 2.345.|  
  
## <a name="__toc360788733"></a>Settings  
  
|Rounding mode|Description|  
|-----------------|---------------|  
|RoundingMode.Up = 0|Adds 5e-n to the number being rounded, where n is the number of fractional digits in the number.|  
|RoundingMode.Down = 1|Subtracts 5e-n from the number being rounded, where n is the number of fractional digits in the number.|  
|RoundingMode.AwayFromZero = 2|The same as **RoundingMode.Up** when the number being rounded is positive; otherwise, the same as<br /><br />**RoundingMode.Down**.|  
|RoundingMode.TowardZero = 3|The same as **RoundingMode.Down** when the number being rounded is positive; otherwise, the same as **RoundingMode.Up**.|  
|RoundingMode.ToEven = 4|Applies **RoundingMode.Up** or<br /><br />**RoundingMode.Down** to round the last digit to even.|  
  
## Remarks  
  
-   If **value** &gt;= 0, returns n with the fractional part rounded by **digits** using **roundingMode.**  
  
-   if **value** &lt; 0, it returns the integral part of n rounded to m-n decimal digits, using **roundingMode**, where m is the number of digits of n.  
  
-   If **roundingMode** is not specified, **RoundingMode.ToEven** is used.  
  
## Examples  
  
```powerquery-m
Number.Round(-1.249, 2) equals -1.25  
```  
  
```powerquery-m
Number.Round(-1.245, 2) equals -1.24  
```  
  
```powerquery-m
Number.Round(1.245, 2, RoundingMode.Up) equals 1.25  
```  
  
```powerquery-m
Number.Round(1.245, 2, RoundingMode.Down) equals 1.24  
```  
  
```powerquery-m
Number.Round(1.245, 2, RoundingMode.AwayFromZero) equals 1.25  
```  
  
```powerquery-m
Number.Round(1.245, 2, RoundingMode.TowardZero) equals 1.24  
```  
  
```powerquery-m
Number.Round(1.245, 2, RoundingMode.ToEven) equals 1.24  
```  
  
```powerquery-m
Number.Round(-1.245, 2, RoundingMode.ToEven) equals -1.24  
```  
