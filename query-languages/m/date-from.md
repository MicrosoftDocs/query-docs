---
title: "Date.From | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Date.From

  
## About  
Returns a date value from a value.  
  
```  
Date.From(value as any, optional culture as nullable text) as nullable date  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to convert.|  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](http://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
  
Values of the following types can be converted to a date value:  
  
|**Type**|**Description**|  
|------------|-------------------|  
|text|Returns a Date value from a text value. For more details, see Date.FromText.|  
|datetime|The Date component of a value.|  
|datetimezone|The Date component of the local date and time equivalent of a value.|  
|number|The Date component of the datetime equivalent of the OLE Automation Date of  a value.|  
|any other type|An Expression.Error is thrown.|  
  
## <a name="__toc360788945"></a>Remarks  
  
-   If a value is null, Date.From returns null.  
  
-   If a value is date, the same value is returned.  
  
## Examples  
  
```  
Date.From(43910) equals #date(2020,3,20)  
```  
  
```  
Date.From(#datetime(1899, 12, 30, 6, 45, 12)) equals #date(1899,12,30)  
```  
