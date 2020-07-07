---
title: "DAX glossary | Microsoft Docs"
description: Describes common terms used in the Data Analysis Expressions (DAX) language.
ms.service: powerbi 
ms.date: 07/06/2020
ms.reviewer: owend
ms.topic: conceptual
author: minewiskan
ms.author: owend

---
# DAX glossary

## Analytic query

Power BI visuals query a data model by using an *analytic query*. An analytic query strives to reduce potentially large data volumes and model complexities using three distinct phases: Filter, group and summarize. An analytic query is created automatically when fields are assigned to the wells of report visuals. Report authors can control the behavior of field assignments by renaming fields, modifying the summarization technique, or disabling summarization to achieve grouping. At report design time, filters can be added to the report, a report page, or a visual. In reading view, filters can be modified in the **Filters** pane, or by interactions with slicers and other visuals (cross-filtering).

## BLANK

DAX defines the absence of a value as BLANK. It's the equivalent of SQL NULL, but it doesn't behave exactly the same. It's more closely aligned to Excel and how it defines an empty cell. BLANK is evaluated as zero or an empty string when combined with other operations. For example, BLANK + 20 = 20. Always use capital letters; the plural is BLANKs, with a lowercase "s".

## Calculated column

A model calculation used to add a column to a tabular model by writing a DAX formula. The formula must return a scalar value, and it's evaluated for each row in the table. A calculated column can be added to an Import or DirectQuery storage mode table.

## Calculated measure

In tabular modeling, there's no such concept as a *calculated measure*. Use *measure* instead. The word *calculated* is used to describe calculated tables and calculated columns. It distinguishes them from tables and columns that originate from Power Query. Power Query doesn't have the concept of a measure.

## Calculated table

A model calculation used to add a table to a tabular model by writing a DAX formula. The formula must return a table object. It results in a table that uses Import storage mode.

## Calculation

A deliberate process that transforms one or more inputs into one or more results. In a tabular data model, a calculation can be a model object; either a calculated table, calculated column, or measure.

## Context

Describes the environment in which a DAX formula is evaluated. There are two types of context: *Row context* and *filter context*. Row context represents the "current row", and is used to evaluate calculated column formulas and expressions used by table iterators. Filter context is used to evaluate measures, and it represents filters applied directly to model columns and filters propagated by model relationships.

## Cube

See [Multidimensional model](#multidimensional-model).

## Data model

A data resource that's specifically prepared for reporting and analytics. It allows report users to browse and explore data in a simple and intuitive way. Importantly, it delivers high performance query results, even over large data volumes. It can integrate data from multiple sources and use calculations to transform data. It can enforce row-level permission to ensure different users have access to different data. Sometimes it's called a *Semantic model* or just a *Model*.

## Data modeler

A skilled data professional who creates data models. In self-service BI (SSBI), they can be called business analysts. In corporate BI, they can be called BI developers.

## DAX

Data Analysis Expressions (DAX) language is a formula language for Power Pivot in Excel, Power BI, Azure Analysis Services, and tabular modeling in SQL Server Analysis Services. You can also use DAX to add data model calculations and define row-level security (RLS) rules.

## Dynamic security

When RLS rules are enforced by using the identity of the report user. Rules filter model tables by using the user's account name, which can be done with the USERNAME or USERPRINCIPALNAME functions. See [Row-level security (RLS)](#row-level-security-(rls)).

## Expression

A unit of DAX logic that's evaluated and returns a result. Expressions can declare variables in which case they're assigned a sub-expression and must include a RETURN statement that outputs a final expression. Expressions are constructed by using model objects (tables, columns, or measures), functions, operators, or constants.

## Field

Data model resource presented in the **Fields** pane. Fields are used to configure report filters and visuals. Fields consist of model columns, hierarchy levels, and measures.

## Formula

One or more DAX expressions used to define a model calculation. Inner expressions are called sub-expressions. Plural is *formulas*.

## Function

DAX functions have arguments that allow passing in parameters. Formulas can use many function calls, possibly nesting functions within other functions.
In a formula, function names must be followed by parentheses. Within the parentheses, parameters are passed in.

## Implicit measure

An automatically generated calculation achieved by configuring a Power BI visual to summarize column values. **Numeric** columns support the greatest range of summarization, including: Sum, Average, Minimum, Maximum, Count (Distinct), Count, Standard deviation, Variance, or Median. Columns of other data types can be summarized, too. **Text** columns can be summarized by using: First (alphabetically), Last (alphabetically), Count (Distinct), or Count. **Date** columns can be summarized by using: Earliest, Latest, Count (Distinct), or Count. **Boolean** columns can be summarized by using: Count (Distinct), or Count.

## Iterator function

A DAX function that enumerates all rows of a given table and evaluate a given expression for each row. It provides flexibility and control over how model calculations summarize data.

## MDX

Multidimensional Expressions (MDX) language is a formula language for SQL Server Analysis Services multidimensional models (also known as *cubes*). MDX can be used to query tabular models, however it can't define implicit measures. It can only query measures that are already defined in the model.

## Measure

A calculation that achieves summarization. Measures are either [*implicit*](#implicit-measure) or *explicit*. An explicit measure is a calculation added to a tabular data model by writing a DAX formula. A measure formula must return a scalar value. In the **Fields** pane, explicit measures are adorned with a calculator icon. Explicit measures are required when the model is queried by using Multidimensional Expressions (MDX), as is the case when using Analyze in Excel. An explicit measure is commonly just called a measure.

## Measure group

A model table that contains at least one measure, and has no hierarchies or visible columns. In the **Fields** pane, each measure group is adorned with a multi-calculator icon. Measure groups are listed together at the top of the **Fields** pane, and sorted alphabetically by name.

## Model

See [Data model](#data-model).

## Modeler

See [Data modeler](#data-modeler).

## Model calculation

A named formula that's used to add a calculated table, calculated column, or measure to a tabular data model. Its structure is \<NAME> = \<FORMULA>. Most calculations are added by data modelers in Power BI Desktop, but measures can also be added to a live connection report. See [Report measures](#report-measures).

## Multidimensional model

A data model developed for SQL Server Analysis Services (multidimensional mode). It comprises dimensions and measures. It's often just called a *cube*.

## Quick measures

A feature in Power BI Desktop that eliminates the need to write DAX formulas for commonly defined measures. Quick measures include average per category, rank, and difference from baseline.

## Report measures

Also called *report-level measures*. They're added to a live connection report in Power BI Desktop by writing a DAX formula, but only for connections to Power BI models or Analysis Services tabular models.

## Row-level security (RLS)

Design technique to restrict access to subsets of data for specific users. In a tabular model, it's achieved by creating model roles. Roles have rules, which are DAX expressions to filter table rows.

## Semantic model

See [Data model](#data-model).

## Summarization

An operation applied to the values of a column. See [measure](#measure).

## Tabular cube

There's no such concept as a *tabular cube*. Use [Tabular model](#tabular-model) instead.

## Tabular model

A data model developed in Power Pivot in Excel, Power BI, Azure Analysis Services, or SQL Server Analysis Services (tabular mode).

## Time intelligence

Time intelligence relates to calculations over time, like year-to-date (YTD).

## Time intelligence function

DAX includes many time intelligence functions. Each time intelligence function achieves its result by modifying the filter context for date filters. Example functions: TOTALYTD and SAMEPERIODLASTYEAR.

## Value, values

Data to be visualized.

## What-if parameter

A Power BI Desktop feature that provides the ability to accept user input through slicers. Each parameter creates a single-column calculated table and a measure that returns a single-selected value. The measure can be used in model calculations to respond to the user's input.