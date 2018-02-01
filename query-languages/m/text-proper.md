---
title: "Text.Proper | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: b286f483-2610-4ba3-b45f-7c805f98c13b
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Text.Proper

  
## About  
Returns a text value with first letters of all words converted to uppercase.  
  
```  
Text.Proper(string as nullable text) as nullable text  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|string|The string to transform.|  
  
## Example  
  
```  
Text.Proper("this is an apple") equals "This Is An Apple"  
```  
