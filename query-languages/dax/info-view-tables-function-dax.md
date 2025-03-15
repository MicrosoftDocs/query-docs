---
description: "Learn more about: INFO.VIEW.TABLES"
title: "INFO.VIEW.TABLES function (DAX)"
author: DataZoeMS
---
# INFO.VIEW.TABLES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns a table with information about each table in the semantic model, such as table name, description, and storage mode. This information helps you understand the model and to self-document the model when used in calculated tables. 

## Syntax

```dax
INFO.VIEW.TABLES()
```

## Return value

A table with the following columns:

| Column | Description |
|---|---|
| [ID] | The unique ID for each table in this semantic model as an integer. |
| [Name] | The name of each table in this semantic model as a string. |
| [Model] | The ID of the table's semantic model as a GUID. |
| [DataCategory] | The data category of each tablein this semantic model  as a string. |
| [Description] | The description of each tablein this semantic model  as a string. |
| [IsHidden] | The hidden state of each table in this semantic model as TRUE or FALSE. |
| [StorageMode] | The storage mode of each table in this semantic model as a string. |
| [TableStorage] | The name and unique ID of each table in this semantic model as a string. |
| [Expression] | The DAX formula of each table in this semantic model as a string. Only applies to calculated tables. |
| [ShowAsVariationOnly] | The show as variation only state of each table in this semantic model as TRUE or FALSE. |
| [IsPrivate] | The private state of each table in this semantic model as TRUE or FALSE. |
| [CalculationGroupPrecedence] | The calculation group precedence of each table in this semantic model as an integer. Only applies to calculation groups. |
| [LineageTag] | The lineage tag of each table in this semantic model  as a string. |

## Remarks

Can only be ran by users with write permission on the semantic model and not when live connected to the semantic model in Power BI Desktop. This function can be used in calculated tables, columns, and measures of a semantic model and will update when the model is refreshed.

## Example 1 - DAX query

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.VIEW.TABLES()
```

This DAX query returns a table with all of the columns of this DAX function.

:::image type="content" source="media/info-view-tables-function-dax/dax-query-example-1.png" alt-text="Screenshot showing the output of INFO.VIEW.TABLES() DAX function in DAX query view." lightbox="media/info-view-tables-function-dax/dax-query-example-1.png":::

## Example 2 - DAX query with SELECTCOLUMNS and ADDCOLUMNS

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view): 

```dax
EVALUATE
	ADDCOLUMNS(
		SELECTCOLUMNS(
			INFO.VIEW.TABLES(),
			"Table", [Name],
			[Description],
			"Storage mode", [StorageMode],
			"Calc table DAX formula", [Expression],
			"Calc group precedence", [CalculationGroupPrecedence],
			[DataCategory]
		),
		"Table type", SWITCH(
			TRUE(),
			NOT (ISBLANK([Calc group precedence])), "Calculation group",
			NOT (ISBLANK([Calc table DAX formula])), "Calculated (DAX) table",
			[DataCategory] = "Time", "Date table",
			[DataCategory]
		)
	)
```

This DAX query returns a table with only the specified columns and a new column to categorize the tables with a DAX formula.

:::image type="content" source="media/info-view-tables-function-dax/dax-query-example-2.png" alt-text="Screenshot showing the output of INFO.VIEW.TABLES() with selected columns in DAX query view." lightbox="media/info-view-tables-function-dax/dax-query-example-2.png":::

## Example 3 - calculated table with SELECTCOLUMNS and ADDCOLUMNS

Either of the above examples work in a calculated table when the EVALUATE keyword is removed and a table name added. Here is example 2 in a calculated table:

```dax
xTables2 = 
	ADDCOLUMNS(
		SELECTCOLUMNS(
			INFO.VIEW.TABLES(),
			"Table", [Name],
			[Description],
			"Storage mode", [StorageMode],
			"Calc table DAX formula", [Expression],
			"Calc group precedence", [CalculationGroupPrecedence],
			[DataCategory]
		),
		"Table type", SWITCH(
			TRUE(),
			NOT (ISBLANK([Calc group precedence])), "Calculation group",
			NOT (ISBLANK([Calc table DAX formula])), "Calculated (DAX) table",
			[DataCategory] = "Time", "Date table",
			[DataCategory]
		)
	)
```
This calculated table shows the same information as the DAX query in example 2 in a table in the model itself.

:::image type="content" source="media/info-view-tables-function-dax/calculated-table-example-3.png" alt-text="Screenshot showing the output of INFO.VIEW.TABLES() with selected columns in DAX query view." lightbox="media/info-view-tables-function-dax/calculated-table-example-3.png":::

## Example 4 - measure

The following measure can be added to count the number of calculated columns in a semantic model:

```dax
Number of calculated tables = 
COUNTROWS(
    FILTER(
		INFO.VIEW.TABLES(),
    		NOT ( ISBLANK( [Expression] ) )
	)
)
```
This will show a scalar value with the number of calculated tables in my model.

This can be shown in a visual:

:::image type="content" source="media/info-view-tables-function-dax/measure-example-4-visuals.png" alt-text="Screenshot showing the output of INFO.VIEW.TABLES() with a measure then used in report visuals." lightbox="media/info-view-tables-function-dax/measure-example-4-visuals.png":::

Or a DAX query in [DAX query view](/power-bi/transform-model/dax-query-view): 

```dax
DEFINE
    MEASURE 'xTables'[Number of calculated tables] = 
		COUNTROWS(
			FILTER(
				INFO.VIEW.TABLES(),
					NOT ( ISBLANK( [Expression] ) )
			)
		)

EVALUATE
    SUMMARIZECOLUMNS(
        "Number of calculated tables", [Number of calculated tables]
    )
```

:::image type="content" source="media/info-view-tables-function-dax/measure-example-4-dax-query.png" alt-text="Screenshot showing the output of INFO.VIEW.TABLES() with a measure then used in a DAX query in DAX query view." lightbox="media/info-view-tables-function-dax/measure-example-4-dax-query.png":::
