---
title: "Double.From | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: aa780f53-9cbc-4ebc-af27-c63d371cf2e1
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Double.From

  
## About  
Returns a Double number value from the given value.  
  
```  
Double.From(value as any, optional culture as nullable text)  as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to convert.|  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](http://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
  
## Remarks  
If the given value is null, Double.From returns null. If the given value is number within the range of Double, value is returned, otherwise an error is returned. If the given value is of any other type, see Number.FromText for converting it to number value, then the previous statement about converting number value to Double number value applies.  
  
## Examples  
  
```  
Double.From("4.5") equals 4.5  
```  
