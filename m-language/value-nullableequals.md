---
title: "Value.NullableEquals | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: c41d93f1-fc55-4c77-9815-d83ad648d6ec
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Value.NullableEquals
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns a logical value or null based on two values .  
  
```  
Value.NullableEquals(value1 as any, value2 as any) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value1|The right value to compare.|  
|value2|The left value to compare.|  
  
## <a name="__toc360789738"></a>Remarks  
  
-   If either of the argument is null, it applies a nullable equality rules; otherwise, the same result as Value.Equals.  
  
## Example  
  
```  
Value.NullableEquals(1, null) equals null  
```  
