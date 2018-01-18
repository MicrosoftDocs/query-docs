---
title: "Value.FromText | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 41ef9826-7a99-4e14-b70e-4761d732d55a
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Value.FromText
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Decodes a value from a textual representation, value, and interprets it as a value with an appropriate type. Value.FromText takes a text value and returns a number, a logical value, a null value, a DateTime value, a Duration value, or a text value. The empty text value is interpreted as a null value.  
  
```  
Value.FromText(value as text, optional culture as nullable text)  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|The value to transform.|  
|optional culture|A text value corresponding to the culture values supported on your version of Windows, such as "en-US". If the culture is not specified, the current user culture is used. For a list of culture names, see [National Language Support (NLS) API Reference](http://msdn.microsoft.com/en-us/goglobal/bb896001.aspx).|  
  
## Examples  
  
```  
Value.FromText("1") equals 1  
```  
  
```  
Value.FromText("2012/5/16") equals #date(2012,5,16)  
```  
  
```  
Value.FromText("null") equals null  
```  
  
```  
Value.FromText("somevalue") equals "somevalue"  
```  
