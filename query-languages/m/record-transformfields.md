---
title: "Record.TransformFields | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Record.TransformFields

  
## About  
Transforms fields by applying **transformOperations**. For more more information about  values supported by **transformOperations**, see Parameter Values.  
  
## Syntax

<pre>
Record.TransformFields(record as record,  transformOperations as list,  optional missingField as nullable number) as record  
</pre>
  
## Arguments  
  
|Argument|Description|  
|------------|---------------|  
|record|The Record to modify.|  
|transformOperations|The list of transformations to make.|  
|optional missingField|A **MissingField** enum value to handle missing fields. The default value is MissingField.Error.|  
  
### MissingField enum  
  
-   `MissingField.Error = 0;`  
  
-   `MissingField.Ignore = 1;`  
  
-   `MissingField.UseNull = 2;`  
  
## Examples  
  
```powerquery-m
Record.TransformFields([OrderID = 1, CustomerID= 1, Item = "Fishing rod", Price = "100.0"], {"Price", Number.FromText})  
```  

```powerquery-m 
equals [OrderID =1, CustomerID  =1, Item = "Fishing rod", Price=100 ]  
```  
  
|||  
|-|-|  
|OrderID|1|  
|CustomerID|1|  
|Item|Fishing rod|  
|Price|100|  
  
```powerquery-m
Record.TransformFields(  
```  
  
```powerquery-m
[OrderID ="1", CustomerID= 1, Item = "Fishing rod", Price = "100.0"],  
```  
  
```powerquery-m
{{"OrderID", Number.FromText}, {"Price",Number.FromText}})  
```  
  
```powerquery-m
equals [OrderID =1, CustomerID  =1, Item = "Fishing rod", Price=100 ]  
```  
  
|||  
|-|-|  
|OrderID|1|  
|CustomerID|1|  
|Item|Fishing rod|  
|Price|100|  
  
