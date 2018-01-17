---
title: "Value.Compare | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 24912d43-e6f8-41b7-b624-7984a9d55632
caps.latest.revision: 6
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Value.Compare
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Returns 1, 0, or -1 based on **value1** being greater than, equal to, or less than the **value2**. An optional comparer function can be provided.  
  
```  
Value.Compare(value1 as any, value2 as any, optional precision as nullable number) as  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|value1|The left value to compare.|  
|value2|The right value to compare.|  
|optional precision|Precision of comparison.|  
  
## <a name="__toc360789742"></a>Arithmetic operations  
The built-in arithmetic operators (+, -, *, /) use Double Precision. The following library functions can be used to request these operations using a specific precision model.  
  
