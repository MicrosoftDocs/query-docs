---
title: "INFO functions (DAX)"
description: "Learn more about: INFO DAX functions"
author: DataZoeMS
ms.author: zoedouglas
ms.date: 03/13/2025
ms.topic: overview
ms.service: powerbi
ms.subservice: dax
---
# INFO functions

Data Analysis Expressions (DAX) includes a set of INFO functions based on the library of [Dynamic Management Views (DMVs) in Analysis Services](/analysis-services/instances/use-dynamic-management-views-dmvs-to-monitor-analysis-services), which have been modified to work as DAX functions. INFO DAX functions output as a table data type. As tables they can be used with other DAX functions such as FILTER, SELECTCOLUMNS, ADDCOLUMNS, and others. This section describes INFO functions available in the DAX language.

For Power BI semantic models, just like DMVs, the INFO DAX functions require semantic model admin permissions. Some also require workspace admin permissions. 

As DAX functions these INFO functions go beyond the capability of the DMVs, which use a SQL-like syntax and return a row set. As these new functions are DAX functions, they can be used like any table in a DAX query – further combined and structured in the DAX query.

```dax
EVALUATE
	ADDCOLUMNS(
		SELECTCOLUMNS(
			INFO.VIEW.MEASURES(),
			"Measure", [Name],
			[Description],
			"DAX Formula", [Expression],
			"State", [State]
		),
		"Model name", "My semantic model",
		"As of date", NOW()
	)
```

INFO functions are supported on Power BI semantic models but not on SQL Server Analysis Services models, Azure Analysis Services models, or PowerPivot models. INFO.VIEW DAX functions can be run in calculated tables, columns, measures, and DAX queries, but other INFO DAX functions can only be run in DAX queries.

## INFO.VIEW DAX functions

Four of the INFO DAX functions also have INFO.VIEW DAX functions counterparts. Friendly names, such as table name instead of table ID, are used and new columns added to make it easier to use without the need to join other INFO DAX function tables. INFO.VIEW DAX functions can be used in calculations inside a semantic model. When included in a [calculated table](/power-bi/transform-model/desktop-calculated-tables) they can self-document a model for other people using it to build reports or DAX queries.

### INFO.VIEW.TABLES 
INFO.VIEW.TABLES contains information about the tables in the model, such as the table name, description, storage mode, and whether it is hidden or not. 

```dax
// Remove EVALUATE when using this DAX function in a calculated table
EVALUATE INFO.VIEW.TABLES()
```

The following screenshot is an example of using this DAX function in [DAX query view](/power-bi/transform-model/dax-query-view) with the **Regional Sales Sample** available from **Learn** in the Power BI service.

:::image type="content" source="media/info-functions-dax/info-view-tables-dax-query.png" alt-text="Screenshot showing the output of INFO.VIEW.TABLES() DAX function in DAX query view." lightbox="media/info-functions-dax/info-view-tables-dax-query.png":::

### INFO.VIEW.COLUMNS
INFO.VIEW.COLUMNS contains information about the columns in a model, such as the column name, data type, and whether it is hidden or not. 

```dax
// Remove EVALUATE when using this DAX function in a calculated table
EVALUATE INFO.VIEW.COLUMNS()
```

The following screenshot is an example of using this DAX function in [DAX query view](/power-bi/transform-model/dax-query-view) with the **Regional Sales Sample** available from **Learn** in the Power BI service.

:::image type="content" source="media/info-functions-dax/info-view-columns-dax-query.png" alt-text="Screenshot showing the output of INFO.VIEW.COLUMNS() DAX function in DAX query view." lightbox="media/info-functions-dax/info-view-columns-dax-query.png":::

### INFO.VIEW.MEASURES
INFO.VIEW.MEASURES contains information about the measures in the model, such as the measure name, expression, and format string. 

```dax
// Remove EVALUATE when using this DAX function in a calculated table
EVALUATE INFO.VIEW.MEASURES()
```

The following screenshot is an example of using this DAX function in [DAX query view](/power-bi/transform-model/dax-query-view) with the **Regional Sales Sample** available from **Learn** in the Power BI service.

:::image type="content" source="media/info-functions-dax/info-view-measures-dax-query.png" alt-text="Screenshot showing the output of INFO.VIEW.MEASURES() DAX function in DAX query view." lightbox="media/info-functions-dax/info-view-measures-dax-query.png":::

### INFO.VIEW.RELATIONSHIPS
INFO.VIEW.RELATIONSHIPS contains information about the relationships in the model, such as the to and from table and columns, cardinality, and cross filter direction.

```dax
// Remove EVALUATE when using this DAX function in a calculated table
EVALUATE INFO.VIEW.RELATIONSHIPS()
```

The following screenshot is an example of using this DAX function in [DAX query view](/power-bi/transform-model/dax-query-view) with the **Regional Sales Sample** available from **Learn** in the Power BI service.

:::image type="content" source="media/info-functions-dax/info-view-relationships-dax-query.png" alt-text="Screenshot showing the output of INFO.VIEW.RELATIONSHIPS() DAX function in DAX query view." lightbox="media/info-functions-dax/info-view-relationships-dax-query.png":::

## INFO DAX functions

Here is the list of INFO functions. Some work only on specific compat levels and for certain storage modes or other semantic model properties. 

| [Function]                                    | [Description]                                                                                                                                   |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------|
| INFO.VIEW.COLUMNS                             | Returns a list of all columns in the current model. Can use in calculations, including calculated tables.                                       |
| INFO.VIEW.MEASURES                            | Returns a list of all measures in the current model. Can use in calculations, including calculated tables.                                      |
| INFO.VIEW.RELATIONSHIPS                       | Returns a list of all relationships in the current model. Can use in calculations, including calculated tables.                                 |
| INFO.VIEW.TABLES                              | Returns a list of all tables in the current model. Can use in calculations, including calculated tables.                                        |
| INFO.ALTERNATEOFDEFINITIONS                   | Returns a table with information about each alternate of definition in the semantic model with metadata about alternate definitions for model objects. |
| INFO.ANNOTATIONS                              | Returns a list of all annotations in the current model with columns matching the schema rowset for annotation objects.                          |
| INFO.ATTRIBUTEHIERARCHIES                     | Represents the TMSCHEMA_ATTRIBUTE_HIERARCHIES DMV query function.                                                                               |
| INFO.ATTRIBUTEHIERARCHYSTORAGES               | Returns a table with information about each attribute hierarchy storage in the semantic model with metadata about the storage characteristics of attribute hierarchies. |
| INFO.CALCDEPENDENCY                           | Returns information about the calculation dependency for a DAX query.                                                                           |
| INFO.CALCULATIONGROUPS                        | Returns a table with information about each calculation group in the semantic model with metadata about calculation groups and their properties. |
| INFO.CALCULATIONITEMS                         | Returns a table with information about each calculation item in the semantic model with metadata about calculation items within calculation groups. |
| INFO.CATALOGS                                 | Represents the DBSCHEMA_CATALOGS DMV query function.                                                                                            |
| INFO.CHANGEDPROPERTIES                        | Represents the TMSCHEMA_CHANGED_PROPERTIES DMV query function.                                                                                  |
| INFO.COLUMNPARTITIONSTORAGES                  | Returns a table with information about each column partition storage in the semantic model with metadata about how column partitions are stored. |
| INFO.COLUMNPERMISSIONS                        | Returns a list of all column permissions in the current model with columns matching the schema rowset for column permissions objects.           |
| INFO.COLUMNS                                  | Returns a list of all columns in the current model with columns matching the schema rowset for column objects.                                  |
| INFO.COLUMNSTORAGES                           | Returns a list of all column storages in the current model with columns matching the schema rowset for column storage objects.                  |
| INFO.CSDLMETADATA                             | Returns information about database metadata in XML format.                                                                                      |
| INFO.CULTURES                                 | Returns a list of all cultures in the current model with columns matching the schema rowset for culture objects.                                |
| INFO.DATACOVERAGEDEFINITIONS                  | Returns a table with information about each data coverage definition in the semantic model with metadata about data coverage settings and definitions. |
| INFO.DATASOURCES                              | Represents the TMSCHEMA_DATASOURCES DMV query function.                                                                                         |
| INFO.DELTATABLEMETADATASTORAGES               | Returns a table with information about each delta table metadata storage in the semantic model with metadata about delta table storage characteristics. |
| INFO.DEPENDENCIES                             | Returns information about the calculation dependency for a DAX query.                                                                           |
| INFO.DETAILROWSDEFINITIONS                    | Returns a list of all detail rows definitions in the current model with columns matching the schema rowset for detail rows definitions objects. |
| INFO.DICTIONARYSTORAGES                       | Returns a table with information about each dictionary storage in the semantic model with metadata about dictionary storage characteristics and compression. |
| INFO.EXCLUDEDARTIFACTS                        | Represents the TMSCHEMA_EXCLUDED_ARTIFACTS DMV query function.                                                                                  |
| INFO.EXPRESSIONS                              | Returns a list of all expressions in the current model with columns matching the schema rowset for expressions objects.                         |
| INFO.EXTENDEDPROPERTIES                       | Returns a list of all extended properties in the current model with columns matching the schema rowset for extended properties objects.         |
| INFO.FORMATSTRINGDEFINITIONS                  | Returns a table with information about each format string definition in the semantic model with metadata about format string definitions for measures and columns. |
| INFO.FUNCTIONS                                | Returns information about the functions that are currently available for use in the DAX programming language.                                   |
| INFO.GENERALSEGMENTMAPSEGMENTMETADATASTORAGES | Returns a table with information about each general segment map segment metadata storage in the semantic model with metadata about segment map storage characteristics. |
| INFO.GROUPBYCOLUMNS                           | Returns a table with information about each group by column in the semantic model with metadata about columns used in group by operations. |
| INFO.HIERARCHIES                              | Represents the TMSCHEMA_HIERARCHIES DMV query function.                                                                                         |
| INFO.HIERARCHYSTORAGES                        | Returns a table with information about each hierarchy storage in the semantic model with metadata about how hierarchies are stored. |
| INFO.KPIS                                     | Returns a list of all KPIS in the current model with columns matching the schema rowset for KPI objects.                                        |
| INFO.LEVELS                                   | Returns a list of all levels in the current model with columns matching the schema rowset for level objects.                                    |
| INFO.LINGUISTICMETADATA                       | Represents the TMSCHEMA_LINGUISTIC_METADATA DMV query function.                                                                                 |
| INFO.MEASURES                                 | Returns a list of all measures in the current model with columns matching the schema rowset for measure objects.                                |
| INFO.MODEL                                    | Represents the TMSCHEMA_MODEL DMV query function.                                                                                               |
| INFO.OBJECTTRANSLATIONS                       | Returns a list of all object translations in the current model with columns matching the schema rowset for object translation objects.          |
| INFO.PARQUETFILESTORAGES                      | Returns a table with information about each Parquet file storage in the semantic model with metadata about Parquet file storage characteristics. |
| INFO.PARTITIONS                               | Represents the TMSCHEMA_PARTITIONS DMV query function.                                                                                          |
| INFO.PARTITIONSTORAGES                        | Returns a list of all partition storages in the current model with columns matching the schema rowset for partition storage objects.            |
| INFO.PERSPECTIVECOLUMNS                       | Returns a list of all perspective columns in the current model with columns matching the schema rowset for perspective columns objects.         |
| INFO.PERSPECTIVEHIERARCHIES                   | Returns a list of all perspective hierarchies in the current model with columns matching the schema rowset for perspective hierarchies objects. |
| INFO.PERSPECTIVEMEASURES                      | Returns a list of all perspective measures in the current model with columns matching the schema rowset for perspective measures objects.       |
| INFO.PERSPECTIVES                             | Returns a list of all perspectives in the current model with columns matching the schema rowset for perspectives objects.                       |
| INFO.PERSPECTIVETABLES                        | Returns a list of all perspective tables in the current model with columns matching the schema rowset for perspective tables objects.           |
| INFO.PROPERTIES                               | Represents the DISCOVER_PROPERTIES DMV query function.                                                                                          |
| INFO.QUERYGROUPS                              | Returns a table with information about each query group in the semantic model with metadata about query groups defined in the model. |
| INFO.REFRESHPOLICIES                          | Returns a table with information about each refresh policy in the semantic model with metadata about refresh policies defined for tables. |
| INFO.RELATEDCOLUMNDETAILS                     | Returns a table with information about each related column detail in the semantic model with metadata about related column details for relationships. |
| INFO.RELATIONSHIPINDEXSTORAGES                | Returns a table with information about each relationship index storage in the semantic model with metadata about relationship index storage characteristics. |
| INFO.RELATIONSHIPS                            | Represents the TMSCHEMA_RELATIONSHIPS DMV query function.                                                                                       |
| INFO.RELATIONSHIPSTORAGES                     | Returns a table with information about each relationship storage in the semantic model with metadata about how relationships are stored. |
| INFO.ROLEMEMBERSHIPS                          | Returns a list of all role memberships in the current model with columns matching the schema rowset for role memberships objects.               |
| INFO.ROLES                                    | Returns a list of all roles in the current model with columns matching the schema rowset for roles objects.                                     |
| INFO.SEGMENTMAPSTORAGES                       | Returns a list of all segment map storages in the current model with columns matching the schema rowset for segment map storage objects.        |
| INFO.SEGMENTSTORAGES                          | Returns a table with information about each segment storage in the semantic model with metadata about segment storage characteristics. |
| INFO.STORAGEFILES                             | Returns a list of all storage files in the current model with columns matching the schema rowset for storage file objects.                      |
| INFO.STORAGEFOLDERS                           | Returns a list of all storage folders in the current model with columns matching the schema rowset for storage folder objects.                  |
| INFO.STORAGETABLECOLUMNS                      | Returns statistics about the columns of in-memory tables.                                                                                       |
| INFO.STORAGETABLECOLUMNSEGMENTS               | Returns information about the column segments used for storing data for in-memory tables.                                                       |
| INFO.STORAGETABLES                            | Returns statistics about in-memory tables.                                                                                                      |
| INFO.TABLEPERMISSIONS                         | Returns a list of all table permissions in the current model with columns matching the schema rowset for table permissions objects.             |
| INFO.TABLES                                   | Returns a list of all tables in the current model with columns matching the schema rowset for table objects.                                    |
| INFO.TABLESTORAGES                            | Returns a list of all table storages in the current model with columns matching the schema rowset for table storage objects.                    |
| INFO.VARIATIONS                               | Returns a list of all variations in the current model with columns matching the schema rowset for variations objects.                           |
