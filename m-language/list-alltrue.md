---
title: "List.AllTrue | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 0cd82c8a-85ad-4360-a479-42dee9cd6a73
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.AllTrue

  
## About  
Returns true if all expressions in a list are true  
  
```  
List.AllTrue(list as list) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## Example  
  
```  
List.AllTrue({true, 2=2}) equals true  
```  
