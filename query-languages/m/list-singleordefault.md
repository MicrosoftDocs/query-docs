---
title: "List.SingleOrDefault | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 846fa33f-2a7b-4630-8674-9e2b2fc0aa8f
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# List.SingleOrDefault

  
## About  
Returns a single item from a list.  
  
```  
List.SingleOrDefault(list as list, optional default as any) as any  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|List|The List to check.|  
|optional default|Specifies a default value to be returned.|  
  
## <a name="__toc360789261"></a>Remarks  
  
-   If list is empty, a default value is returned instead.  
  
-   If default is not specified, the default value of null is assumed.  
  
-   If list has more than one item, an error is returned.  
  
## Examples  
  
```  
List.SingleOrDefault({1}) equals 1  
```  
  
```  
List.SingleOrDefault({1, 2, 3}) equals error  
```  
  
```  
List.SingleOrDefault({}, 0) equals 0  
```  
