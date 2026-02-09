---
description: "Learn more about: INFO.VIEW.MEASURES"
title: "INFO.VIEW.MEASURES function (DAX)"
ms.topic: reference
author: DataZoeMS
---
# INFO.VIEW.MEASURES

[!INCLUDE[applies-to-measures-columns-tables-visual-calculations](includes/applies-to-measures-columns-tables-visual-calculations.md)]

Returns a table with information about each measure in the semantic model, such as name, description, and DAX formula. This information helps you understand the model and to self-document the model when used in calculated tables. 

## Syntax

```dax
INFO.VIEW.MEASURES()
```

## Return value

A table with the following columns:

| Column | Description |
|---|---|
| [ID] | The unique ID for each measure in this semantic model as an integer. |
| [Name] | The name of each measure in this semantic model as a string. |
| [Table] | The home table of each measure in this semantic model as a string. |
| [Description] | The description of each measure in this semantic model as a string. |
| [DataType] | The data type of each measure in this semantic model as a string. Measures are usually variant data type. |
| [Expression] | The DAX formula of each measure in this semantic model. |
| [FormatString] | The format string of each measure in this semantic model as a string. |
| [IsHidden] | The hidden state of each measure in this semantic model as True or False. |
| [State] | The state (such as valid or error) of each measure in this semantic model as a string. |
| [KPIID] | The KPI ID of each measure in this semantic model as an integer. |
| [IsSimpleMeasure] | The simple measure flag of each measure in this semantic model as True of False. |
| [DisplayFolder] | The display folder of each measure in this semantic model as a string. Nested folders shown with / and multiple folders separated by ;. |
| [DetailRowsDefinition] | The details rows definition  of each measure in this semantic model. |
| [DataCategory] | The data category  of each measure in this semantic model as a string. |
| [FormatStringDefinition] | The dynamic format string  of each measure in this semantic model. |
| [LineageTag] | The lineage tag  of each measure in this semantic model as a string. |

## Remarks

Only shows the `Expression`, `DetailRowsDefinition`, `FormatStringDefinition` values when ran by users with write permission on the semantic model and not when live connected to the semantic model in Power BI Desktop.
Unlike [INFO.MEASURES](), this function can be used in calculated tables, columns, and measures of a semantic model, including as part of a model refresh.

## Example 1 - DAX query

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.VIEW.MEASURES()
```

This DAX query returns a table with all of the columns of this DAX function.

:::image type="content" source="media/info-view-measures-function-dax/dax-query-example-1.png" alt-text="Screenshot showing the output of INFO.VIEW.MEASURES() in DAX query view." lightbox="media/info-view-measures-function-dax/dax-query-example-1.png":::

## Example 2 - DAX query with SELECTCOLUMNS

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view): 

```dax
EVALUATE
	SELECTCOLUMNS(
		INFO.VIEW.MEASURES(),
		"Home table", [Table],
		"Measure", [Name],
		[Description],
		"DAX formula", [Expression],
		[State]
	)
```

This DAX query returns a table with only the specified columns.

:::image type="content" source="media/info-view-measures-function-dax/dax-query-example-2.png" alt-text="Screenshot showing the output of INFO.VIEW.MEASURES() with selected columns in DAX query view." lightbox="media/info-view-measures-function-dax/dax-query-example-2.png":::

## Example 3 - calculated table with SELECTCOLUMNS

Either of the above examples work in a calculated table when the EVALUATE keyword is removed and a table name added. Here is example 2 in a calculated table:

```dax
Measures in this semantic model = 
SELECTCOLUMNS(
		INFO.VIEW.MEASURES(),
		"Home table", [Table],
		"Measure", [Name],
		[Description],
		"DAX formula", [Expression],
		[State]
	)
```
This calculated table shows the same information as the DAX query in example 2 in a table in the model itself.

## Example 4 - measure

The following measure can be added to count the number of text columns in a semantic model:

```dax
Number of measures = 
COUNTROWS( INFO.VIEW.MEASURES() )
```
This will show a scalar value with the number of measures in my model.

This can be shown in a visual:

:::image type="content" source="media/info-view-measures-function-dax/measure-example-4-visuals.png" alt-text="Screenshot showing the output of INFO.VIEW.MEASURES() with a measure then used in report visuals." lightbox="media/info-view-measures-function-dax/measure-example-4-visuals.png":::

Or a DAX query in [DAX query view](/power-bi/transform-model/dax-query-view): 

```dax
DEFINE
    MEASURE 'Measures in this semantic model'[Number of measures] = COUNTROWS( INFO.VIEW.MEASURES() )

EVALUATE
    SUMMARIZECOLUMNS(
        "Number of measures", [Number of measures]
    )
```

:::image type="content" source="media/info-view-measures-function-dax/measure-example-4-dax-query.png" alt-text="Screenshot showing the output of INFO.VIEW.MEASURES() with a measure then used in a DAX query in DAX query view." lightbox="media/info-view-measures-function-dax/measure-example-4-dax-query.png":::

## See also

- [INFO.VIEW.TABLES](info-view-tables-function-dax.md)
- [INFO.VIEW.COLUMNS](info-view-columns-function-dax.md)
- [INFO.VIEW.RELATIONSHIPS](info-view-relationships-function-dax.md)
- [INFO.MEASURES](info-measures-function-dax.md)
- [INFO.TABLES](info-tables-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
