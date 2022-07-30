---
description: "Learn more about: Comments"
title: "Comments"
ms.date: 12/12/2018
ms.service: powerquery
ms.topic: reference
author: dougklopfenstein
ms.author: dougklo

---
# Comments
You can add comments to your code with single-line comments `//` or multi-line comments that begin with `/*` and end with `*/`.  
  
**Example - Single-line comment**  
  
```powerquery-m  
let  
   //Convert to proper case.  
    Source = Text.Proper("hello world")  
in  
    Source  
```  
**Example - Multi-line comment**  
  
```powerquery-m  
/* Capitalize each word in the Item column in the Orders table. Text.Proper  
is evaluated for each Item in each table row. */  
let  
    Orders = Table.FromRecords({  
        [OrderID = 1, CustomerID = 1, Item = "fishing rod", Price = 100.0],  
          [OrderID = 2, CustomerID = 1, Item = "1 lb. worms", Price = 5.0],  
          [OrderID = 3, CustomerID = 2, Item = "fishing net", Price = 25.0]}),  
        #"Capitalized Each Word" = Table.TransformColumns(Orders, {"Item", Text.Proper})  
in  
        #"Capitalized Each Word"  
```  
