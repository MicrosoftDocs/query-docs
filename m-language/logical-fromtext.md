---
title: "Logical.FromText | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 8d32f2ac-5c58-411f-90ab-055c7c5c5baf
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
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
