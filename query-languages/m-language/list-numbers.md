---
title: "List.Numbers | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 4f89a4ac-acf9-4c8c-918b-36705798cc02
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.Numbers

  
## About  
Returns a list of numbers from size count starting at initial, and adds an increment.  The increment defaults to 1.  
  
```  
List.Numbers(start as number, count as number, optional increment as nullable number) as { Number }  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|start|The first number in the sequence.|  
|count|How many numbers to return.|  
|optional increment|The number to increment each number.|  
  
## Examples  
  
```  
List.Numbers(1, 5) equals {1, 2, 3, 4, 5}  
```  
  
```  
List.Numbers(1, 8, 3) equals {1, 4, 7, 10, 13, 16, 19, 22}  
```  
