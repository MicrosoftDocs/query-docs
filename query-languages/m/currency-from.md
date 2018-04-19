---
title: "Currency.From | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Currency.From

  
## About  
Returns a currency value from the given value.  
  
```  
Currency.From(value as any, optional culture as nullable text, optional roundingMode as nullable number) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to convert.|  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](http://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
|optional roundingMode|Specifies rounding direction when there is a tie between the possible numbers to round to.|  
  
## Remarks  
If a value is null, Currency.From returns null.  If a value is a number within range of currency, the fractional part of the value is rounded to 4 decimal digits and returned. The valid range for currency is -922,337,203,685,477.5808 to 922,337,203,685,477.5807. If value is of any other type or out of the range, an error is returned. See Number.FromText for converting it to a number value, then convert from a number to a 64-bit integer. See Number.Round for the available rounding modes, the default is RoundingMode.ToEven.  
  
## Examples  
  
```  
Currency.From("1.23455") equals 1.2346  
```  
  
```  
Currency.From("1.23455", "en-Us", RoundingMode.Down) equals 1.2345  
```  
