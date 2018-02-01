---
title: "Function.Invoke | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 32840f82-cff0-4a39-9ebb-d6dc3346cdbd
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Function.Invoke

  
## About  
Invokes the given function using the specified Arguments and returns the result.  
  
```  
Function.Invoke(function as function, args as list) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|function|The function to invoke.|  
|args|The list of required Arguments.|  
  
## Example  
  
```  
Function.Invoke(Record.FieldNames, {[A=1,B=2]}) equals {"A", "B"}  
```  
