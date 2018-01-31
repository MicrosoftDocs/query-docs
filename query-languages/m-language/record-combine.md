---
title: "Record.Combine | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: cb2b0fb3-e172-4c52-a8d3-1620030851a8
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Record.Combine

  
## About  
Combines the records in a list.  
  
```  
Record.Combine(list as list) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The list of records to combine.|  
  
## <a name="__toc360789157"></a>Remarks  
If the list contains non-record values, an error is returned.  
  
## <a name="__goback"></a>Example  
  
```  
Record.Combine({ [CustomerID =1], [Name ="Bob"] , [Phone =  "123-4567"] })  
```  
  
```  
equals [CustomerID=1, Name="Bob", Phone="123-4567"]  
```  
  
|||  
|-|-|  
|CustomerID|1|  
|Name|Bob|  
|Phone|123-4567|  
  
