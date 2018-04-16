---
title: "DateTime.From | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# DateTime.From

  
## About  
Returns a datetime value from a value.  
  
```  
DateTime.From(value as any, optional culture as nullable text) as nullable datetime  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to convert.|  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](http://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
  
### Type to convert  
  
|**Type**|**Description**|  
|------------|-------------------|  
|text|Returns a datetime value from a text value. For more details, see DateTime.FromText.|  
|date|A datetime with value as the date component and 12:0:00 AM as the time component.|  
|datetimezone|The local date and time equivalent of value.|  
|time|A datetime with the date equivalent to the OLE Automation Date of 0 as the date component and value as the time component.|  
|number|A datetime equivalent the OLE Automation Date expressed by value.|  
|any other type|An Expression.Error is thrown.|  
  
## <a name="__toc360789049"></a>Remarks  
  
-   If a value is null, DateTime.From returns null.  
  
-   If a value is datetime, the same value is returned.  
  
## Examples  
  
```  
DateTime.From(#time(06, 45, 12)) equals #datetime(1899, 12, 30, 06, 45, 12)  
```  
  
```  
DateTime.From(#date(1975, 4, 4)) equals #datetime(1975, 4, 4, 0, 0, 0)  
```  
