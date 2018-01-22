---
title: "Record.FromTable | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 58064c8d-8097-4e01-a12c-76e2d559f907
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Record.FromTable

  
## About  
Returns a record from a table of records containing field names and values.  
  
```  
Record.FromTable(list as table) as record  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|list|The Table to check.|  
  
## <a name="__toc360789195"></a>Remarks  
  
-   An Expression.Error is thrown if the fields are not unique.  
  
## <a name="__goback"></a>Example  
  
```  
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
  
