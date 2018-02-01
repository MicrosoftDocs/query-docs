---
title: "Type.ForFunction | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
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
manager: "kfile"
---
# Type.ForFunction

  
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
