---
title: "Type.ForFunction | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 7b835253-e2d3-4907-96e1-921cbdf96ff4
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Type.ForFunction
This topic applies to the Power Query Formula Language which can be used with [Power Query](https://support.office.com/article/Introduction-to-Microsoft-Power-Query-for-Excel-6E92E2F4-2079-4E1F-BAD5-89F6269CD605) and [Power BI Desktop](http://go.microsoft.com/fwlink/p/?LinkId=618607) to build queries that mashup data. See the list of [function categories](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## About  
Creates a function type from the given Arguments.  
  
```  
Type.ForFunction(signature as record,  min as number) as type  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|signature|A Record value that contains fields for ReturnType and Parameters. Parameters is itself a record with all the parameter values assigned to their expected types.|  
|min|The minimum number of Arguments required to invoke the function.|  
  
## Example  
  
```  
Type.ForFunction([ReturnType = number, Parameters = [X = number]], 1)  
```  
