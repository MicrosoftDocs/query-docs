---
description: "Learn more about: AnalysisServices.Database"
title: "AnalysisServices.Database"
ms.subservice: m-source
---
# AnalysisServices.Database

## Syntax

<pre>
AnalysisServices.Database(
    <b>server</b> as text,
    <b>database</b> as text,
    optional <b>options</b> as nullable record
) as table
</pre>

## About

Returns a table of multidimensional cubes or tabular models from the Analysis Services database `database` on server `server`. An optional record parameter, `options`, may be specified to control the following options:

* `Query`: A native MDX query used to retrieve data.
* `TypedMeasureColumns`: A logical value indicating if the types specified in the multidimensional or tabular model will be used for the types of the added measure columns. When set to false, the type "number" will be used for all measure columns. The default value for this option is false.
* `Culture`: A culture name specifying the culture for the data. This corresponds to the 'Locale Identifier' connection string property.
* `CommandTimeout`: A duration that controls how long the server-side query is allowed to run before it is canceled. The default value is driver-dependent.
* `ConnectionTimeout`: A duration that controls how long to wait before abandoning an attempt to make a connection to the server. The default value is driver-dependent.
* `SubQueries`: A number (0, 1 or 2) that sets the value of the "SubQueries" property in the connection string. This controls the behavior of calculated members on subselects or subcubes. (The default value is 2).
* `Implementation`

## Related content

* [How culture affects text formatting](how-culture-affects-text-formatting.md)
