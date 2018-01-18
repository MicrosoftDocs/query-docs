---
title: "Value.Metadata | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: d4278eee-b70a-4ae6-9d2a-abd3c7e22bf3
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Value.Metadata
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a record containing the input?s metadata.  
  
```  
Value.Metadata(value as any) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|The value to retrieve metadata for.|  
  
## Example  
  
```  
Value.Metadata(1 meta [meta = 1]) equals [ meta = 1]  
```  
