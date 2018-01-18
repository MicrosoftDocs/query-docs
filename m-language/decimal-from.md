---
title: "Decimal.From | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 862c9753-3dbc-43ab-bb4b-6e93eb712319
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Decimal.From
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a decimal number value from the given value.  
  
```  
Decimal.From(value as any, optional culture as nullable text) as nullable number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|Value to convert.|  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](http://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
  
## Remarks  
Returns a Decimal number value from the given value. If the given value is null, Decimal.From returns null. If the given value is number within the range of Decimal, value is returned, otherwise an error is returned. If the given value is of any other type, see Number.FromText for converting it to number value, then the previous statement about converting number value to Decimal number value applies.  
  
## Examples  
  
```  
Decimal.From("4.5") equals 4.5  
```  
