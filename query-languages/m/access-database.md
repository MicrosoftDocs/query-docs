---
description: "Learn more about: Access.Database"
title: "Access.Database"
ms.date: 12/12/2018
---
# Access.Database

## Syntax

<pre>  
Access.Database(<b>database</b> as binary, optional <b>options</b> as nullable record) as table 
</pre> 
  
## About  
Returns a structural representation of an Access database, `database`. An optional record parameter, `options`, may be specified to control the following options: <ul> <li> `CreateNavigationProperties` : A logical (true/false) that sets whether to generate navigation properties on the returned values (default is false).</li> <li> `NavigationPropertyNameGenerator` : A function that is used for the creation of names for navigation properties.</li> </ul> The record parameter is specified as [option1 = value1, option2 = value2...], for example.  

