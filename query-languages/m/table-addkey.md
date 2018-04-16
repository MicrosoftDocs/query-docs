---
title: "Table.AddKey | Microsoft Docs"
ms.date: 4/16/2018
ms.service: powerbi
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Table.AddKey

  
## About  
Add a key to table.  
  
```  
Table.AddKey(table as table,  columns as list,  isPrimary as logical) as table  
```  
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|table|The Table to modify.|  
|columns|The subset of column names that defines the key.|  
|isPrimary|Specifies whether the key is primary.|  
  
## <a name="__goback"></a>Example  
  
```  
let  
  
        table = Table.FromRecords(  
  
    {  
  
        [CustomerID = 1, Name = "Bob", Phone = "123-4567"],  
  
        [CustomerID = 2, Name = "Jim", Phone = "987-6543"] ,  
  
        [CustomerID = 3, Name = "Paul", Phone = "543-7890"] ,  
  
        [CustomerID = 4, Name = "Ringo", Phone = "232-1550"]  
  
    }  
  
),  
  
        resultTable = Table.AddKey(table, {"CustomerID"}, true)  
  
in  
  
        resultTable  
```  
  
|CustomerID|Name|Phone|  
|--------------|--------|---------|  
|1|Bob|123-4567|  
|2|Jim|987-6543|  
|3|Paul|543-7890|  
|4|Ringo|232-1550|  
  
