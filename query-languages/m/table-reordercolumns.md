---
title: "Table.ReorderColumns | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerquery

ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ReorderColumns

  
## About  
Returns a table with specific columns in an order relative to one another, without changing the order of the columns that aren’t specified.  
  
## Syntax

<pre>
Table.ReorderColumns(table as table, columnOrder as list, optional missingField as nullable number) as table  
</pre> 
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|columnOrder|The list of columns to arrange in the specific order.|  
|optional missingField|The default value of missingField is **MissingField.Error**. For more information, see Parameter Values.|  
  
## <a name="__toc360789576"></a>Remarks  
  
-   Table.ReorderColumns is similar to Record.ReorderFields applied to every row in a table.  
  
-   Columns that are not specified will remain in the same location and the specified columns will be ordered around them.  
  
## Examples  
  
```powerquery-m
Table.ReorderColumns(Table.FromRecords({[CustomerID=1, Phone = "123-4567", Name ="Bob"] }), {"Name","Phone"})  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
|CustomerID|Name|Phone|  
|1|Bob|123-4567|  

```powerquery-m 
Table.ReorderColumns(Table.FromRecords({  
  
    [CustomerID=1, Name = "Bob", Phone = "123-4567"]  
  
}), {"Address1", "Address2"}, MissingField.UseNull)  
  
Table.ReorderColumns(Table.FromRecords({  
  
    [CustomerID=1, Name = "Bob", Phone = "123-4567"]  
  
}), {"Address1", "Address2"}, MissingField.UseNull)  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|ddress1|Address2|  
|1|Bob|123-4567|null|null|  
  
