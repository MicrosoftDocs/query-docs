---
title: "Value.As | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 976d2e2e-ceaf-4920-9a59-f52834198c1c
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Value.As
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Value.As is the function corresponding to the as operator in the formula language. The expression  value as type  asserts that the value of a value argument is compatible with type as per the is operator. If it is not compatible, an error is raised.  
  
```  
Value.As(value as any, type as type) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|The value as.|  
|type|Asserts that the value of a value argument is compatible with type.|  
  
