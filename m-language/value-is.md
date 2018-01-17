---
title: "Value.Is | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: a535f4fc-cf0e-4e57-8950-0eada7b3385f
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Value.Is
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Value.Is is the function corresponding to the is operator in the formula language. The expression value is type  returns true if the ascribed type of value is compatible with type, and returns false if the ascribed type of value is incompatible with type.  
  
```  
Value.Is(value as any, type as type) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value|The value is.|  
|type|Type of value is compatible with type|  
  
