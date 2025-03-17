---
description: "Learn more about: INFO.CALCDEPENDENCY"
title: "INFO.CALCDEPENDENCY function (DAX)"
author: DataZoeMS
---
# INFO.CALCDEPENDENCY

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each calculation dependency in the semantic model. This information helps you understand the model.

## Syntax

```dax
INFO.CALCDEPENDENCY([<Restriction name>, <Restriction value>], ...)
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Description |
|---|---|
| [DATABASE_NAME] | The name of the semantic model. |
| [OBJECT_TYPE] | The type of object. |
| [TABLE] | The object's table name. |
| [OBJECT] | The name of the object. |
| [EXPRESSION] | The DAX formula of the object. |
| [REFERENCED_OBJECT_TYPE] | The type of object this object references. The "Object" is dependent on this object. |
| [REFERENCED_TABLE] | The referenced object's table name. |
| [REFERENCED_OBJECT] | The referenced object's name. | 
| [REFERENCED_EXPRESSION] | The refrenced object's DAX formula. |
| [QUERY] | The query, if specified as a restriction. |

## Remarks

Can only be ran by users with write permission on the semantic model and not when live connected to the semantic model in Power BI Desktop. This function can be used in [DAX queries](dax-queries), and can't be used in calculations.

You can also call this DAX function with INFO.DEPENDENCIES.

## Example 1 - DAX query

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.CALCDEPENDENCY()
```

This DAX query returns a table with all of the columns of this DAX function.

## Example 2 - DAX query with restriction

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view): 

```dax
EVALUATE
	INFO.CALCDEPENDENCY("Query", "EVALUATE { [Orders] }")
```

This DAX query returns a table showing the objects in the semantic model needed to run this specified DAX query. The restriction name of "query" is used with the value of a DAX query. This DAX query is getting the output of the measure named Orders. 

If a query has double-quotes they can be escaped with another double-quote and you can optionally use a VAR to hold the value.

```dax
EVALUATE
	VAR _query =
		"EVALUATE
		SELECTCOLUMNS(
			'Date',
			""Date"", [Date]
		)"
	RETURN
		INFO.CALCDEPENDENCY(
			"Query",
			_query
		)
```
