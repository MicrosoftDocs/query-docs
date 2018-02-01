---
title: "List.NonNullCount | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 4c390b2a-a53d-4448-9543-991795881da7
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.NonNullCount

  
## About  
Returns the number of items in a list excluding null values  
  
```  
List.NonNullCount(list as list) as number  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The List to check.|  
  
## <a name="__goback"></a>Example  
  
```  
List.NonNullCount({1, null}) equals 1  
```  
