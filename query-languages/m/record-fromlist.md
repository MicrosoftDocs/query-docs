---
title: "Record.FromList | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.FromList

  
## About  
Returns a record from a list of field values and a set of field names.  
  
## Syntax

<pre>
Record.FromList(list as list, fields as any) as record  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The list of values in the record to check.|  
|fields|The set of fields corresponding to the values. The fields can be specific either by a list of text values or a record type.|  
  
## <a name="__toc360789944"></a>Remarks  
  
-   An Expression.Error is thrown if the fields are not unique.  
  
## Examples  
  
```powerquery-m
Record.FromList  
  
(  
  
    {1, "Bob", "123-4567"},  
  
    type [CustomerID = number, Name = text, Phone = number]  
  
)  
  
equals [CustomerID = 1, Name = "Bob", Phone = "123-4567"]  
```  
  
|||  
|-|-|  
|OrderID|1|  
|Name|Bob|  
|Phone|123-4567|  
  
