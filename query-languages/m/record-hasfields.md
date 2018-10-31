---
title: "Record.HasFields | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.HasFields

  
## About  
Returns true if the field name or field names are present in a record.  
  
## Syntax

<pre>
Record.HasFields(record as record, fields as any) as logical  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The Record to check against.|  
|fields|A text value or a list of text values.|  
  
## <a name="__toc360789150"></a>Examples:  
  
```powerquery-m
Record.HasFields([CustomerID = 1, Name = "Bob", Phone = "123-4567"],"CustomerID") equals true  
```  
  
```powerquery-m
Record.HasFields([CustomerID = 1, Name = "Bob", Phone = "123-4567"],{"CustomerID", "Address"}) equals false  
```  
