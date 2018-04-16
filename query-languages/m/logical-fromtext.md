---
title: "Logical.FromText | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Logical.FromText

  
## About  
Returns a logical value of true or false from a text value.  
  
```  
Logical.FromText(text as nullable text) as nullable logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|text|The text to evaluate.|  
  
## Examples  
  
```  
Logical.FromText("true") equals true  
```  
  
```  
Logical.FromText("a") equals error  
```  
