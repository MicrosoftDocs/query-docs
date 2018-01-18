---
title: "Comments | Microsoft Docs"
ms.custom: ""
ms.date: "2015-07-18"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "article"
ms.assetid: 3f725744-8098-41d4-b6af-69a750f2e771
caps.latest.revision: 5
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Comments
You can add comments to your code with single-line comments (//) or multi-line comments that begin with /* and end with \*/.  
  
**Example - Single-line comment**  
  
```  
let  
   \/\/Convert to proper case  
    Source \= Text.Proper("hello world")  
in  
    Source  
```  
**Example - Multi-line comment**  
  
```  
\/\* Capitalize each word in the Item column in the Orders table. Text.Proper  
is evaluated for each Item in each table row. \*\/  
let  
    Orders \= Table.FromRecords({  
        \[OrderID \= 1, CustomerID \= 1, Item \= "fishing rod", Price \= 100.0],  
          \[OrderID \= 2, CustomerID \= 1, Item \= "1 lb. worms", Price \= 5.0],  
          \[OrderID \= 3, CustomerID \= 2, Item \= "fishing net", Price \= 25.0]}),  
        \#"Capitalized Each Word" \= Table.TransformColumns(Orders, {"Item", Text.Proper})  
in  
        \#"Capitalized Each Word"  
```  
