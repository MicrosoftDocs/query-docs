---
title: "Record.Combine | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.Combine

  
## About  
Combines the records in a list.  
  
## Syntax

<pre>
Record.Combine(list as list) as record  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The list of records to combine.|  
  
## <a name="__toc360789157"></a>Remarks  
If the list contains non-record values, an error is returned.  
  
## <a name="__goback"></a>Example  
  
```powerquery-m
Record.Combine({ [CustomerID =1], [Name ="Bob"] , [Phone =  "123-4567"] })  
```  
  
```powerquery-m 
equals [CustomerID=1, Name="Bob", Phone="123-4567"]  
```  
  
|||  
|-|-|  
|CustomerID|1|  
|Name|Bob|  
|Phone|123-4567|  
  
