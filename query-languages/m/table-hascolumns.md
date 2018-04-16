---
title: "Table.HasColumns | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.HasColumns

  
## About  
Returns true if a table has the specified column or columns.  
  
```  
Table.HasColumns(table as table, columns as any) as logical  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to check.|  
|columns|The columns to check for as a text value or a list of text values.|  
  
## <a name="__toc360793125"></a>Remarks  
  
-   **Table.HasColumns** is similar to **Record.HasFields** but requires a table as input.  
  
## Examples  
  
```  
Table.HasColumns(Table.FromRecords(  
  
{  
  
      [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"],  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"],  
  
      [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
),"Name")  
  
equals true  
```  
