---
title: "List.Contains | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 92fdacc7-ebdc-4941-83fc-8583b98ee843
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.Contains

  
## About  
Returns true if a value is found in a list.  
  
```  
List.Contains(list as list, value as any, optional equationCriteria as any) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
|value|The value to check for.|  
|optional equationCriteria|An optional equation criteria value to control equality testing.|  
  
## Examples  
  
```  
List.Contains({1, 2, 3}, 2) equals true  
```  
  
```  
List.Contains({1, 2, 3}, 4) equals false  
```  
