---
description: "Learn more about: Accessing data enueration values"
title: "Accessing data enumeration values | Microsoft Docs"
ms.date: 4/21/2022
ms.service: powerquery
ms.reviewer: dougklo
ms.topic: reference
author: dougklopfenstein
ms.author: bezhan
---
# Accessing data enumeration values

These enumeration values are used by functions that access data.
  
|Enumeration value|Description|  
|------------|---------------|  
|[AccessControlKind.Allow](accesscontrolkind-allow.md)|Access is allowed.|
|[AccessControlKind.Deny](accesscontrolkind-deny.md)|Access is denied.|
|[BufferMode.Delayed](buffermode-delayed.md)|The type of the value is computed immediately but its contents aren't buffered until data is needed, at which point the entire value is immediately buffered.|
|[BufferMode.Eager](buffermode-eager.md)|The entire value is immediately buffered in memory before continuing.|
|[CsvStyle.QuoteAfterDelimiter](csvstyle-quoteafterdelimiter.md)|Quotes in a field are only significant immediately following the delimiter.|
|[CsvStyle.QuoteAlways](csvstyle-quotealways.md)|Quotes in a field are always significant regardless of where they appear.
|[LimitClauseKind.AnsiSql2008](limitclausekind-ansisql2008.md)|This SQL dialect supports an ANSI SQL-compatible LIMIT N ROWS specifier to limit the number of rows returned.|
|[LimitClauseKind.Limit](limitclausekind-limit.md) |This SQL dialect supports a LIMIT specifier to limit the number of rows returned.|
|[LimitClauseKind.LimitOffset](limitclausekind-limitoffset.md)|This SQL dialect supports LIMIT and OFFSET specifiers to limit the number of rows returned.|
|[LimitClauseKind.None](limitclauseKind-none.md)|This SQL dialect does not support a limit clause.|
|[LimitClauseKind.Top](limitclausekind-top.md)|This SQL dialect supports a TOP specifier to limit the number of rows returned.|
|[ODataOmitValues.Nulls](odataomitvalues-nulls.md)|Allows the OData service to omit null values.|
|[SapBusinessWarehouseExecutionMode.DataStream](sapbusinesswarehouseexecutionmode.datastream.md)|'DataStream flattening mode' option for MDX execution in SAP Business Warehouse.|
|[SapBusinessWarehouseExecutionMode.BasXml](sapbusinesswarehouseexecutionmode.basxml.md)|'bXML flattening mode' option for MDX execution in SAP Business Warehouse.|
|[SapBusinessWarehouseExecutionMode.BasXmlGzip](sapbusinesswarehouseexecutionmode.basxmlgzip.md)|'Gzip compressed bXML flattening mode' option for MDX execution in SAP Business Warehouse. Recommended for low latency or high volume queries.|
|[SapHanaDistribution.All](saphanadistribution-all.md)|Returns the packages in an SAP HANA database.|
|[SapHanaDistribution.Connection](saphanadistribution-connection.md)|'Connection' distribution option for SAP HANA.|
|[SapHanaDistribution.Off](saphanadistribution-off.md)|'Off' distribution option for SAP HANA.|
|[SapHanaDistribution.Statement](saphanadistribution-statement.md)|'Statement' distribution option for SAP HANA.|
|[SapHanaRangeOperator.Equals](saphanarangeoperator-equals.md)|'Equals' range operator for SAP HANA input parameters.|
|[SapHanaRangeOperator.GreaterThan](saphanarangeoperator-greaterthan.md)|'Greater than' range operator for SAP HANA input parameters.|
|[SapHanaRangeOperator.GreaterThanOrEquals](saphanarangeoperator-greaterthanorequals.md)|'Greater than or equals' range operator for SAP HANA input parameters.|
|[SapHanaRangeOperator.LessThan](saphanarangeoperator-lessthan.md)|'Less than' range operator for SAP HANA input parameters.|
|[SapHanaRangeOperator.LessThanOrEquals](saphanarangeoperator-lessthanorequals.md)|'Less than or equals' range operator for SAP HANA input parameters.|
|[SapHanaRangeOperator.NotEquals](saphanarangeoperator-equals.md)|'Not equals' range operator for SAP HANA input parameters.|
|[WebMethod.Delete](webmethod-delete.md) | Specifies the DELETE method for HTTP.|
|[WebMethod.Get](webmethod-get.md) | Specifies the GET method for HTTP.|
|[WebMethod.Head](webmethod-head.md) | Specifies the HEAD method for HTTP.|
|[WebMethod.Patch](webmethod-patch.md) | Specifies the PATCH method for HTTP.|
|[WebMethod.Post](webmethod-post.md) | Specifies the POST method for HTTP.|
|[WebMethod.Put](webmethod-put.md) | Specifies the PUT method for HTTP.|

## See also

[Accessing data functions](accessing-data-functions.md)
