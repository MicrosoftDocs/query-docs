---
title: "Table.ReplaceErrorValues | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.ReplaceErrorValues

  
## About  
Replaces the error values in the specified columns with the corresponding specified value.  
  
```  
Table.ReplaceErrorValues(table as table, errorReplacement as list) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|errorReplacement|The list of columns and the value to replace the errors with. The form of the list is {{column1, value1},…}|  
  
## <a name="__toc360789538"></a>Remarks  
  
-   There may be only one replacement value per column, specifying the column more than one will result in an error  
  
## Example  
  
```  
Table.ReplaceErrorValues(  
  
    Table.FromRows({{1,"hello"},{3,...}}, {"Column1","Column2"}),  
  
    {"Column2", "world"})  
```  
  
|Column1|Column2|  
|-----------|-----------|  
|1|hello|  
|2|world|  
  
