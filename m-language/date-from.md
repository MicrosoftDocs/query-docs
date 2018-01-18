---
title: "Date.From | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b0814c07-c738-407b-8478-8a52bd3ea099
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Date.From
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
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
