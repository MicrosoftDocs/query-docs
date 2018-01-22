---
title: "Byte.From | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 1574d887-e610-4372-83cc-99a3d7579f10
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Byte.From

  
## About  
Returns a 8-bit integer number value from the given value.  
  
```  
Byte.From(value as any, optional culture as nullable text, optional roundingMode as nullable number) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to convert.|  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](http://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
|optional roundingMode|Specifies rounding direction when there is a tie between the possible numbers to round to.|  
  
## Remarks  
If the given value is null, Byte.From returns null. If the given value is number within the range of 8-bit integer without a fractional part, value is returned. If it has fractional part, then the number is rounded with the rounding mode specified. The default rounding mode is RoundingMode.ToEven. If the given value is of any other type, see Number.FromText for converting it to number value, then the previous statement about converting number value to 8-bit integer number value applies. See Number.Round for the available rounding modes.  
  
## Examples  
  
```  
Byte.From("4") equals 4  
```  
  
```  
Byte.From("4.5", null, RoundingMode.AwayFromZero) equals 5  
```  
