---
title: "Table.SelectColumns | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.SelectColumns

  
## About  
Returns a table that contains only specific columns.  
  
## Syntax

<pre>
Table.SelectColumns(table as table, columns as any, optional missingField as any) as table  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|columns|The list of columns to copy.|  
|optional missingField|The default value of missingField is **MissingField.Error**. For more information, see Parameter Values.|  
  
## <a name="__toc360789584"></a>Remarks  
  
-   Table.SelectColumns is similar to Record.SelectFields applied to every row in a table.  
  
## Examples  

```powerquery-m
Table.SelectColumns(Table.FromRecords(  
  
{  
  
      [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
      [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
      [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
      [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
}  
  
), "Name")  
```  
  
|Name|  
|--------|  
|Bob|  
|Jim|  
|Paul|  
|Ringo|  
  
```  
Table.SelectColumns(Table.FromRecords({  
  
    [CustomerID=1, Name="Bob", Phone = "123-4567"]}), {"CustomerID", "Name"})  
```  
  
|CustomerID|Name|  
|--------------|--------|  
|1|Bob|  
  
```  
Table.SelectColumns(Table.FromRecords({  
  
    [CustomerID=1, Name = "Bob", Phone = "123-4567" ]}), {"CustomerID", "NewColumn"}, MissingField.UseNull)  
```  
  
|CustomerID|NewColumn|  
|--------------|-------------|  
|1|null|  
  
