---
title: "DateTime.From | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 1a07b930-6eab-4505-92e9-621da1131496
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# DateTime.From
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
