---
description: "Learn more about: INFO.KPIS"
title: "INFO.KPIS function (DAX)"
author: jeroenterheerdt
---
# INFO.KPIS

[!INCLUDE[applies-to-query-only](includes/applies-to-query-only.md)]

Returns a table with information about each KPI in the semantic model. This function provides metadata about Key Performance Indicators defined in the model.

## Syntax

```dax
INFO.KPIS ( [<Restriction name>, <Restriction value>], ... )
```

[!INCLUDE[parameters-for-info-dax-functions](includes/parameters-for-info-dax-functions.md)]

## Return value

A table with the following columns:

| Column | Description |
|--------|-------------|
| [ID] | Unique identifier for the KPI |
| [MeasureID] | Identifier of the measure associated with the KPI |
| [Description] | Description of the KPI |
| [TargetDescription] | Description of the KPI target |
| [TargetExpression] | DAX expression defining the KPI target value |
| [TargetFormatString] | Format string for displaying the target value |
| [StatusGraphic] | Graphic used to display the KPI status |
| [StatusDescription] | Description of the KPI status |
| [StatusExpression] | DAX expression defining the KPI status |
| [TrendGraphic] | Graphic used to display the KPI trend |
| [TrendDescription] | Description of the KPI trend |
| [TrendExpression] | DAX expression defining the KPI trend |
| [ModifiedTime] | Timestamp of when the KPI was last modified |

## Remarks

- Typically used in DAX queries to inspect and document model metadata.
- Permissions required depend on the host. Querying full metadata may require model admin permissions.

## Example

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	INFO.KPIS()
```

## Example 2 - DAX query with joins

The following DAX query can be run in [DAX query view](/power-bi/transform-model/dax-query-view):

```dax
EVALUATE
	VAR _KPIs =
		SELECTCOLUMNS(
			INFO.KPIS(),
			"KPIID", [ID],
			"MeasureID", [MeasureID],
			"KPI Description", [Description],
			"TargetExpression", [TargetExpression]
		)
	VAR _Measures = 
		SELECTCOLUMNS(
			INFO.MEASURES(),
			"MeasureID", [ID],
			"Measure Name", [Name]
		)
	VAR _CombinedTable =
		NATURALLEFTOUTERJOIN(
			_KPIs,
			_Measures
		)
	RETURN
		SELECTCOLUMNS(
			_CombinedTable,
			"Measure Name", [Measure Name],
			"KPI Description", [KPI Description],
			"Target Expression", [TargetExpression]
		)
	ORDER BY [Measure Name]
```

## See also

- [INFO.CALCULATIONGROUPS](info-calculationgroups-function-dax.md)
- [INFO.CALCULATIONITEMS](info-calculationitems-function-dax.md)
- [INFO.MEASURES](info-measures-function-dax.md)
- [INFO.TABLES](info-tables-function-dax.md)
- [INFO.COLUMNS](info-columns-function-dax.md)
