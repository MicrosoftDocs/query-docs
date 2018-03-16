---
title: "Table.ContainsAll | Microsoft Docs"
ms.custom: ""
ms.date: "01/19/2018"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "language-reference"
ms.assetid: 71615c4e-5e3b-49d5-8cd9-4f96adacc202
caps.latest.revision: 7
author: "Minewiskan"
ms.author: "owend"
manager: "kfile"
---
# Table.ContainsAll

  
## About  
Determines whether all of the specified records appear as rows in the table.  
  
```  
Table.ContainsAll(table as table, rows as list, optional equationCriteria as any) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|rows|The List of rows to check for.|  
|optional equationCriteria|An optional value that specifies how to control comparison between the rows of the table.|  
  
## <a name="__toc360789669"></a>Remarks  
  
-   Table.ContainsAll is similar to List.ContainsAll but requires a table as input.  
  
## <a name="__goback"></a>Example  
  
```  
Table.ContainsAll(  
  
  Table.FromRecords(  
  
{  
  
    [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
    [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
    [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
    [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
),  
  
    {[CustomerID=1, Name="Bill"],[CustomerID=2, Name="Fred"]},  
  
    "CustomerID")  
  
equals true  
```  
