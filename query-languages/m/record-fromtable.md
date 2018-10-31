---
title: "Record.FromTable | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.FromTable

  
## About  
Returns a record from a table of records containing field names and values.  
  
## Syntax

<pre>
Record.FromTable(list as table) as record  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The Table to check.|  
  
## <a name="__toc360789195"></a>Remarks  
  
-   An Expression.Error is thrown if the fields are not unique.  
  
## <a name="__goback"></a>Example  
  
```powerquery-m
let  
  
    input = Table.FromRows({{"OrderID",1} , {"CustomerID", 1}, {"Item", "Fishing rod"}, {"Price" , 100.00}}, {"Name", "Value"})  
  
in  
  
    Record.FromTable(input)  
  
equals [OrderID = 1, CustomerID = 1, Item = "Fishing rod", Price = 100.0]  
```  
  
|||  
|-|-|  
|OrderID|1|  
|CustomerID|1|  
|Item|Fishing rod|  
|Price|100|  
  
