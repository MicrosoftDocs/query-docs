---
author: jeroenterheerdt
ms.author: Jeroen ter Heerdt
ms.date: 03/17/2025
ms.topic: include
ms.service: powerbi
ms.subservice: dax
---
### ObjectState

|Value|Name|Description|
|---|---|---|
|1|Ready|Object is refreshed, contains up-to-date data, and is queryable.|
|3|NoData|Object is queryable but contains no data. Refresh it to bring in data. Applies to non-calculated objects, such as DataColumns, partitions, and Tables.|
|4|CalculationNeeded|Object is not queryable and contains no data. It needs to be refreshed to become functional. Applies only to calculated objects, such as calculated columns, hierarchies, and calculated tables.|
|5|SemanticError|Object is in an error state because of an invalid expression. It is not queryable.|
|6|EvaluationError|Object is in an error state because an error occurred during expression evaluation. It is not queryable.|
|7|DependencyError|Object is in an error state because some of its calculation dependencies are in an error state. It is not queryable.|
|8|Incomplete|Some parts of the object have no data. Refresh the object to add the rest of the data. The object is queryable. Applies to non-calculated objects, such as DataColumns, partitions, and tables.|
|10|ForceCalculationNeeded|The data is possibly outdated, but is in a queryable state. Applies only for CalculatedTable.|

This table is based on the [official documentation](/dotnet/api/microsoft.analysisservices.tabular.objectstate).

To join with INFO functions use this DAX query.

```dax
EVALUATE
	DATATABLE(
	"State",INTEGER,
	"StateName",STRING,
	{
    	{1,"Ready"},
    	{3,"NoData"},
    	{4,"CalculationNeeded"},
    	{5,"SemanticError"},
    	{6,"EvaluationError"},
    	{7,"DependencyError"},
    	{8,"Incomplete"},
    	{10,"ForceCalculationNeeded"}
	}
	)
```
