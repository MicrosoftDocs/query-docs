---
title: "Int32.From | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Int32.From

  
## About  
Returns a 32-bit integer number value from the given value  
  
```  
Int32.From(value as any, optional culture as nullable text, optional roundingMode as nullable number) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to convert.|  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](http://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
|optional roundingMode|Specifies rounding direction when there is a tie between the possible numbers to round to.|  
  
## Remarks  
If the given value is null, Int32.From returns null. If the given value is number within the range of 32-bit integer without a fractional part, value is returned. If it has fractional part, then the number is rounded with the rounding mode specified. The default rounding mode is RoundingMode.ToEven. If the given value is of any other type, see Number.FromText for converting it to number value, then the previous statement about converting number value to 32-bit integer number value applies. See Number.Round for the available rounding modes.  
  
## Examples  
  
```  
Int32.From("4") equals 4  
```  
  
```  
Int32.From("4.5", null, RoundingMode.AwayFromZero) equals 5  
```  
