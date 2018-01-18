---
title: "Number.FromText | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 478c0ada-2f38-4076-9327-9d595637f5cd
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Number.FromText
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a number value from a text value.  
  
```  
Number.FromText(text as nullable text, optional culture as nullable text) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|Text value to convert to a number. If **text** does not represent a valid number, **Expression.Error** is thrown.|  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](http://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
  
## Examples  
  
```  
Number.FromText("1") equals 1  
```  
  
```  
Number.FromText("a") equals error  
```  
