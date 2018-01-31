---
title: "DateTimeZone.From | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 57219c2a-0a23-4170-807d-70a2bc0d2011
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# DateTimeZone.From

  
## About  
Returns a datetimezone value from a value.  
  
```  
DateTimeZone.From(value as any, optional culture as nullable text) as nullable datetimezone  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to convert.|  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](http://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
  
### Type to convert  
  
|**Type**|**Description**|  
|------------|-------------------|  
|text|Returns a datetimezone value from a text value. For more details, see DateTimeZone.FromText.|  
|date|A datetimezone with value as the date component, 12:0:00 AM as the time component and the offset corresponding the local time zone.|  
|datetime|A datetimezone with value as the datetime and the offset corresponding the local time zone.|  
|time|A datetimezone with the date equivalent of the OLE Automation Date of 0 as the date component, value as the time component and the offset corresponding the local time zone.|  
|number|A datetimezone with the datetime equivalent the OLE Automation Date expressed by value and the offset corresponding the local time zone.|  
|any other type|An Expression.Error is thrown.|  
  
## <a name="__toc360789077"></a>Remarks  
  
-   If a value is null, DateTimeZone.From returns null.  
  
-   If a value is  datetimezone , the same value is returned.  
  
## Example  
`DateTimeZone.From("2020-10-30T01:30:00-08:00") equals #datetimezone(2020, 10, 30, 01, 30, 00, -8, 00)`  
  
