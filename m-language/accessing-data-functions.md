---
title: "Accessing data functions | Microsoft Docs"
ms.custom: ""
ms.date: "12/28/2017"
ms.prod: "powerbi"
ms.reviewer: ""
ms.suite: ""
ms.technology: 
  - "mlang"
ms.tgt_pltfrm: ""
ms.topic: "index-page "
ms.assetid: 8a2b13de-5256-4124-a980-cc53535e4022
caps.latest.revision: 23
author: "Minewiskan"
ms.author: "owend"
manager: "erikre"
---
# Accessing data functions
The Power Query Formula Language is a mashup language for transforming data. It's a functional, case sensitive language similar to F\#. Power Query Formula Language is used in a number of Microsoft products such as Power BI Desktop, Excel, and Analysis Services. To learn more about the language, see [PowerQueryName reference](https://msdn.microsoft.com/en-us/library/mt211003.aspx).  
  
## <a name="__toc360789771"></a>Accessing data  
Functions in this section access data and return table values. Most of these functions return a table value that is called a **navigation table**. A **navigation table** is a two column table. The first column contains the name of an item and the corresponding second column contains the value of that item. This shape is primarily used by the Power Query user interface to provide navigation experience over the potentially large hierarchical data returned.  
  
|Function|Description|  
|------------|---------------|  
|[Access.Database](../PowerQuery/access-database.md)|Returns a structural representation of an Microsoft Access database. The database argument is     The return value is a record, where each field represents a table in the Access database.|  
|[ActiveDirectory.Domains](../PowerQuery/activedirectory-domains.md)|Returns a table with Domain information available in the current domain or optional Active Directory forest.|  
|[AdoDotNet.DataSource](../PowerQuery/adodotnet-datasource.md)|Returns the schema collection for an ADO.NET data source.|
|[AdoDotNet.Query](../PowerQuery/adodotnet-query.md)|Returns the result of running a native query on an ADO.NET data source.|
|[AnalysisServices.Database](../PowerQuery/analysisservices-database.md)|Returns a table of multidimensional cubes or tabular models from the Analysis Services database.|  
|[AnalysisServices.Databases](../PowerQuery/analysisservices-databases.md)|Returns the Analysis Services databases on a particular host.|  
|[AzureStorage.Blobs](../PowerQuery/azurestorage-blobs.md)|Returns a navigational table containing all containers found in the Azure Storage account. Each row has the container name and a link to the container blobs.|  
|[AzureStorage.Tables](../PowerQuery/azurestorage-tables.md)|Returns a navigational table containing a row for each table found at the account URL from an Azure storage vault. Each row contains a link to the azure table.|  
|[Csv.Document](../PowerQuery/csv-document.md)|Returns the contents of a CSV document as a table using the specified encoding.|
|[CsvStyle.QuoteAfterDelimiter](../PowerQuery/csvstyle-quoteafterdelimiter.md)|Quotes in a field are only significant immediately following the delimiter.| 
|[CsvStyle.QuoteAlways](../PowerQuery/csvstyle-quotealways.md)|Quotes in a field are always significant regardless of where they appear.
|[Cube.AddAndExpandDimensionColumn](../PowerQuery/cube-addandexpanddimensioncolumn.md)|Merges the specified dimension table, dimensionSelector, into the cube?s, cube, filter context and changes the dimensional granularity by expanding the specified set, attributeNames, of dimension attributes. |
|[Cube.AddMeasureColumn](../PowerQuery/cube-addmeasurecolumn.md)|Adds a column with the name column to the cube that contains the results of the measure measureSelector applied in the row context of each row. |
|[Cube.ApplyParameter](../PowerQuery/cube-applyparameter.md)|Returns a cube after applying parameter with arguments to cube.|
|[Cube.AttributeMemberId](../PowerQuery/cube-attributememberid.md)|Returns the unique member identifier from a member property value.| 
|[Cube.CollapseAndRemoveColumns](../PowerQuery/cube-collapseandremovecolumns.md)|Changes the dimensional granularity of the filter context for the cube by collapsing the attributes mapped to the specified columns columnNames.|
|[Cube.Dimensions](../PowerQuery/cube-dimensions.md)|Returns a table containing the set of available dimensions within the cube.|
|[Cube.DisplayFolders](../PowerQuery/cube-displayfolders.md)|Returns a nested tree of tables representing the display folder hierarchy of the objects (e.g. dimensions and measures) available for use in the cube.
|[Cube.Measures](../PowerQuery/cube-measures.md)|Returns a table containing the set of available measures within the cube.|
|[Cube.Parameters](../PowerQuery/cube-parameters.md)|Returns a table containing the set of parameters that can be applied to cube.|
|[Cube.ReplaceDimensions](../PowerQuery/cube-replacedimensions.md)||
|[Cube.Transform](../PowerQuery/cube-transform.md)|Applies the list cube functions, transforms, on the cube.|
|[DB2.Database](../PowerQuery/db2-database.md)|Returns a table with data relating to the tables in the specified DB2 Database.|  
|[Excel.CurrentWorkbook](../PowerQuery/excel-currentworkbook.md)|Returns the tables in the current Excel workbook|
|[Excel.Workbook](../PowerQuery/excel-workbook.md)|Returns a table representing sheets in the given excel workbook.|  
|[Exchange.Contents](../PowerQuery/exchange-contents.md)|Returns a table of contents from a Microsoft Exchange account.| 
|[Facebook.Graph](../PowerQuery/facebook-graph.md)|Returns a table containing content from the Facebook graph .|  
|[File.Contents](../PowerQuery/file-contents.md)|Returns the binary contents of the file located at a path.|  
|[Folder.Contents](../PowerQuery/folder-contents.md)|Returns a table containing the properties and contents of the files and folders found at path.|  
|[Folder.Files](../PowerQuery/folder-files.md)|Returns a table containing a row for each file found at a folder path, and subfolders. Each row contains properties of the folder or file and a link to its content.|  
|[GoogleAnalytics.Accounts](../PowerQuery/googleanalytics-accounts.md)|Returns the Google Analytics accounts for the current credential.| 
|[Hdfs.Contents](../PowerQuery/hdfs-contents.md)|Returns a table containing a row for each folder and file found at the folder url, {0}, from a Hadoop file system. Each row contains properties of the folder or file and a link to its content.|  
|[Hdfs.Files](../PowerQuery/hdfs-files.md)|Returns a table containing a row for each file found at the folder url, {0}, and subfolders from a Hadoop file system. Each row contains properties of the file and a link to its content.|  
|[HdInsight.Containers](../PowerQuery/hdinsight-containers.md)|Returns a navigational table containing all containers found in the HDInsight account. Each row has the container name and table containing its files.|  
|[HdInsight.Contents](../PowerQuery/hdinsight-contents.md)|Returns a navigational table containing all containers found in the HDInsight account. Each row has the container name and table containing its files.|  
|[HdInsight.Files](../PowerQuery/hdinsight-files.md)|Returns a table containing a row for each folder and file found at the container URL, and subfolders from an HDInsight account. Each row contains properties of the file/folder and a link to its content.|  
|[Informix.Database](../PowerQuery/informix-database.md)|Returns a table of SQL tables and views available in an Informix database on server <code>server</code> in the database instance named <code>database</code>.|  
|[Json.Document](../PowerQuery/json-document.md)|Returns the contents of a JSON document. The contents may be directly passed to the function as text, or it may be the binary value returned by a function like File.Contents.|  
|[Json.FromValue](../PowerQuery/json-fromvalue.md)|Produces a JSON representation of a given value value with a text encoding specified by encoding.|
|[Marketplace.Subscriptions](../PowerQuery/marketplace-subscriptions.md)|Returns feeds offered by the Microsoft Azure DataMarket subscribed by the current user as a table.|  
|[MQ.Queue](../PowerQuery/mq-queue.md)|Returns a table that defines the IBM WebSphere MQ Server information required for reading and writing messages.|  
|[MySQL.Database](../PowerQuery/mysql-database.md)|Returns a table with data relating to the tables in the specified MySQL Database.| 
|[OData.Feed](../PowerQuery/odata-feed.md)|Returns a table of OData feeds offered by an OData serviceUri.|  
|[Odbc.DataSource](../PowerQuery/odbc-datasource.md)|Returns a table of SQL tables and views from the ODBC data source specified by the connection string <code>connectionString</code>. |  
|[Odbc.Query](../PowerQuery/odbc-query.md)|Connects to a generic provider with the given connection string and returns the result of evaluating the query.|  
|[OleDb.DataSource](../PowerQuery/oledb-datasource.md)|Returns a table of SQL tables and views from the OLE DB data source specified by the connection string.| 
|[OleDb.Query](../PowerQuery/oledb-query.md)|Returns the result of running a native query on an OLE DB data source.| 
|[Oracle.Database](../PowerQuery/oracle-database.md)|Returns a table with data relating to the tables in the specified Oracle Database.| 
|[PostgreSQL.Database](../PowerQuery/postgresql-database.md)|Returns a table with data relating to the tables in the specified PostgreSQL Database.|
|[RData.FromBinary](../PowerQuery/rdata-frombinary.md)|Returns a record of data frames from the RData file.|  
|[Salesforce.Data](../PowerQuery/salesforce-data.md)|Connects to the Salesforce Objects API and returns the set of available objects (i.e. Accounts).|  
|[Salesforce.Reports](../PowerQuery/salesforce-reports.md)|Connects to the Salesforce Reports API and returns the set of available reports.|  
|[SapBusinessObjects.Universes](../PowerQuery/sapbusinessobjects-universes.md)|Connects to the SAP BusinessObjects BI Universe at the specified URL and returns the set of available universes.|  
|[SapBusinessWarehouse.Cubes](../PowerQuery/sapbusinesswarehouse-cubes.md)|Returns the InfoCubes and queries in an SAP Business Warehouse system grouped by InfoArea.| 
|[SapHana.Database](../PowerQuery/saphana-database.md)|Returns the packages in an SAP HANA database.| 
|[SapHanaDistribution.All](../PowerQuery/saphanadistribution-all.md)|Returns the packages in an SAP HANA database.|
|[SapHanaDistribution.Connection](../PowerQuery/saphanadistribution-connection.md)|'Connection' distribution option for SAP HANA.|
|[SapHanaDistribution.Off](../PowerQuery/saphanadistribution-off.md)|'Off' distribution option for SAP HANA.|
|[SapHanaDistribution.Statement](../PowerQuery/saphanadistribution-statement.md)|'Statement' distribution option for SAP HANA.|
|[SapHanaRangeOperator.Equals](../PowerQuery/saphanarangeoperator-equals.md)|'Equals' range operator for SAP HANA input parameters.|
|[SapHanaRangeOperator.GreaterThan](../PowerQuery/saphanarangeoperator-greaterthan.md)|'Greater than' range operator for SAP HANA input parameters.|
|[SapHanaRangeOperator.GreaterThanOrEquals](../PowerQuery/saphanarangeoperator-greaterthanorequals.md)|'Greater than or equals' range operator for SAP HANA input parameters.|
|[SapHanaRangeOperator.LessThan](../PowerQuery/saphanarangeoperator-lessthan.md)|'Less than' range operator for SAP HANA input parameters.|
|[SapHanaRangeOperator.LessThanOrEquals](../PowerQuery/saphanarangeoperator-lessthanorequals.md)|'Less than or equals' range operator for SAP HANA input parameters.|
|[SapHanaRangeOperator.NotEquals](../PowerQuery/saphanarangeoperator-equals.md)|'Not equals' range operator for SAP HANA input parameters.|
|[SharePoint.Contents](../PowerQuery/sharepoint-contents.md)|Returns a table containing a row for each folder and document found at the SharePoint site url. Each row contains properties of the folder or file and a link to its content.|  
|[SharePoint.Files](../PowerQuery/sharepoint-files.md)|Returns a table containing a row for each document found at the SharePoint site url, and subfolders. Each row contains properties of the folder or file and a link to its content.| 
|[SharePoint.Tables](../PowerQuery/sharepoint-tables.md)|Returns a table containing the result of a SharePoint List as an OData feed.|  
|[Soda.Feed](../PowerQuery/soda-feed.md)|Returns the resulting table of a CSV file that can be accessed using the SODA 2.0 API. The URL must point to a valid SODA-compliant source that ends in a .csv extension.|  
|[Sql.Database](../PowerQuery/sql-database.md)|Returns a table containing SQL tables located on a SQL Server instance database.|
|[Sql.Databases](../PowerQuery/sql-databases.md)|Returns a table with references to databases located on a SQL Server instance. Returns a navigation table.|  
|[Sybase.Database](../PowerQuery/sybase-database.md)|Returns a table with data relating to the tables in the specified Sybase Database.|  
|[Teradata.Database](../PowerQuery/teradata-database.md)|Returns a table with data relating to the tables in the specified Teradata Database.|  
|[Web.Contents](../PowerQuery/web-contents.md)|Returns the contents downloaded from a web url as a binary value.| 
|[Web.Page](../PowerQuery/web-page.md)|Returns the contents of an HTML webpage as a table.|  
|[WebMethod.Delete](../PowerQuery/webmethod-delete.md) | Specifies the DELETE method for HTTP.|
|[WebMethod.Get](../PowerQuery/webmethod-get.md) | Specifies the GET method for HTTP.|
|[WebMethod.Head](../PowerQuery/webmethod-head.md) | Specifies the HEAD method for HTTP.|
|[WebMethod.Patch](../PowerQuery/webmethod-patch.md) | Specifies the PATCH method for HTTP.|
|[WebMethod.Post](../PowerQuery/webmethod-post.md) | Specifies the POST method for HTTP.|
|[WebMethod.Put](../PowerQuery/webmethod-put.md) | Specifies the PUT method for HTTP.|
|[Xml.Document](../PowerQuery/xml-document.md)|Returns the contents of an XML document as a hierarchical table (list of records).|  
|[Xml.Tables](../PowerQuery/xml-tables.md)|Returns the contents of an XML document as a nested collection of flattened tables.|  


  
