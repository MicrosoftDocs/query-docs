---
author: DataZoeMS
ms.author: zoedouglas
ms.date: 03/17/2025
ms.topic: include
ms.service: powerbi
ms.subservice: dax
---
### ObjectType

| Number | Value                  |
|-------------|------------------------|
| 0           | Null                   |
| 1           | Model                  |
| 2           | DataSource             |
| 3           | Table                  |
| 4           | Column                 |
| 5           | AttributeHierarchy     |
| 6           | Partition              |
| 7           | Relationship           |
| 8           | Measure                |
| 9           | Hierarchy              |
| 10          | Level                  |
| 11          | Annotation             |
| 12          | KPI                    |
| 13          | Culture                |
| 14          | ObjectTranslation      |
| 15          | LinguisticMetadata     |
| 29          | Perspective            |
| 30          | PerspectiveTable       |
| 31          | PerspectiveColumn      |
| 32          | PerspectiveHierarchy   |
| 33          | PerspectiveMeasure     |
| 34          | Role                   |
| 35          | RoleMembership         |
| 36          | TablePermission        |
| 37          | Variation              |
| 38          | Set                    |
| 39          | PerspectiveSet         |
| 40          | ExtendedProperty       |
| 41          | Expression             |
| 42          | ColumnPermission       |
| 43          | DetailRowsDefinition   |
| 44          | RelatedColumnDetails   |
| 45          | GroupByColumn          |
| 46          | CalculationGroup       |
| 47          | CalculationItem        |
| 48          | AlternateOf            |
| 49          | RefreshPolicy          |
| 50          | FormatStringDefinition |

This table is based on the [official documentation](/dotnet/api/microsoft.analysisservices.tabular.objecttype).

To join with INFO functions use this DAX query.

```dax
EVALUATE
	DATATABLE(
	"ObjectType",INTEGER,
	"Object",STRING,
	{
	{0,"Null"},
	{1,"Model"},
	{2,"DataSource"},
	{3,"Table"},
	{4,"Column"},
	{5,"AttributeHierarchy"},
	{6,"Partition"},
	{7,"Relationship"},
	{8,"Measure"},
	{9,"Hierarchy"},
	{10,"Level"},
	{11,"Annotation"},
	{12,"KPI"},
	{13,"Culture"},
	{14,"ObjectTranslation"},
	{15,"LinguisticMetadata"},
	{29,"Perspective"},
	{30,"PerspectiveTable"},
	{31,"PerspectiveColumn"},
	{32,"PerspectiveHierarchy"},
	{33,"PerspectiveMeasure"},
	{34,"Role"},
	{35,"RoleMembership"},
	{36,"TablePermission"},
	{37,"Variation"},
	{38,"Set"},
	{39,"PerspectiveSet"},
	{40,"ExtendedProperty"},
	{41,"Expression"},
	{42,"ColumnPermission"},
	{43,"DetailRowsDefinition"},
	{44,"RelatedColumnDetails"},
	{45,"GroupByColumn"},
	{46,"CalculationGroup"},
	{47,"CalculationItem"},
	{48,"AlternateOf"},
	{49,"RefreshPolicy"},
	{50,"FormatStringDefinition"}
	}
	)
```
