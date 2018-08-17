---
title: "Accessing data functions | Microsoft Docs"
ms.date: 4/16/2018
ms.prod: power-query
ms.reviewer: owend
ms.topic: reference
author: minewiskan
ms.author: owend
manager: kfile
---
# Accessing data functions
 
  
## <a name="__toc360789771"></a>Accessing data  
Functions in this section access data and return table values. Most of these functions return a table value that is called a **navigation table**. A **navigation table** is a two column table. The first column contains the name of an item and the corresponding second column contains the value of that item. This shape is primarily used by the Power Query user interface to provide navigation experience over the potentially large hierarchical data returned.  
  
|Function|Description|  
|------------|---------------|  
|[Access.Database](access-database.md)|Returns a structural representation of an Microsoft Access database. |  
|[ActiveDirectory.Domains](activedirectory-domains.md)|Returns a table with Domain information available in the current domain or optional Active Directory forest.|  
|[AdobeAnalytics.Cubes](adobeanalytics-cubes.md)   | Returns a table of multidimensional packages from Adobe Analyics.  |
|[AdoDotNet.DataSource](adodotnet-datasource.md)|Returns the schema collection for an ADO.NET data source.|
|[AdoDotNet.Query](adodotnet-query.md)|Returns the result of running a native query on an ADO.NET data source.|
|[AnalysisServices.Database](analysisservices-database.md)|Returns a table of multidimensional cubes or tabular models from the Analysis Services database.|  
|[AnalysisServices.Databases](analysisservices-databases.md)|Returns the Analysis Services databases on a particular host.|
|[AzureStorage.BlobContents](azurestorage-blobcontents.md) | Returns the content of the specified blob from an Azure storage vault. |  
|[AzureStorage.Blobs](azurestorage-blobs.md)|Returns a navigational table containing all containers found in the Azure Storage account. Each row has the container name and a link to the container blobs.|  
|[AzureStorage.Tables](azurestorage-tables.md)|Returns a navigational table containing a row for each table found at the account URL from an Azure storage vault. Each row contains a link to the azure table.|  
|[AzureStorage.DataLakeContents](azurestorage-datalakecontents.md)|Returns the content of the file at the URL from an Azure Data Lake Storage filesystem.|
|[Csv.Document](csv-document.md)|Returns the contents of a CSV document as a table using the specified encoding.|
|[CsvStyle.QuoteAfterDelimiter](csvstyle-quoteafterdelimiter.md)|Quotes in a field are only significant immediately following the delimiter.| 
|[CsvStyle.QuoteAlways](csvstyle-quotealways.md)|Quotes in a field are always significant regardless of where they appear.
|[Cube.AddAndExpandDimensionColumn](cube-addandexpanddimensioncolumn.md)|Merges the specified dimension table, dimensionSelector, into the cube’s, cube, filter context and changes the dimensional granularity by expanding the specified set, attributeNames, of dimension attributes. |
|[Cube.AddMeasureColumn](cube-addmeasurecolumn.md)|Adds a column with the name column to the cube that contains the results of the measure measureSelector applied in the row context of each row. |
|[Cube.ApplyParameter](cube-applyparameter.md)|Returns a cube after applying parameter with arguments to cube.|
|[Cube.AttributeMemberId](cube-attributememberid.md)|Returns the unique member identifier from a member property value.| 
|[Cube.AttributeMemberProperty](cube-attributememberproperty.md) | Returns the property `propertyName` of dimension attribute `attribute`.|
|[Cube.CollapseAndRemoveColumns](cube-collapseandremovecolumns.md)|Changes the dimensional granularity of the filter context for the cube by collapsing the attributes mapped to the specified columns columnNames.|
|[Cube.Dimensions](cube-dimensions.md)|Returns a table containing the set of available dimensions within the cube.|
|[Cube.DisplayFolders](cube-displayfolders.md)|Returns a nested tree of tables representing the display folder hierarchy of the objects (e.g. dimensions and measures) available for use in the cube.
|[Cube.Measures](cube-measures.md)|Returns a table containing the set of available measures within the cube.|
|[Cube.MeasureProperties](cube-measureproperties.md)|Returns a table containing the set of available properties for measures that are expanded in the cube.|
|[Cube.MeasureProperty](cube-measureproperty.md)|Returns the property of a measure.|
|[Cube.Parameters](cube-parameters.md)|Returns a table containing the set of parameters that can be applied to cube.|   
|[Cube.Properties](cube-properties.md)|Returns a table containing the set of available properties for dimensions that are expanded in the cube.|
| [Cube.PropertyKey](cube-propertykey.md)  | Returns the key of property `property`.  |
|[Cube.ReplaceDimensions](cube-replacedimensions.md)||
|[Cube.Transform](cube-transform.md)|Applies the list cube functions, transforms, on the cube.|
|[DB2.Database](db2-database.md)|Returns a table with data relating to the tables in the specified DB2 Database.|  
|[Excel.CurrentWorkbook](excel-currentworkbook.md)|Returns the tables in the current Excel workbook|
|[Excel.Workbook](excel-workbook.md)|Returns a table representing sheets in the given excel workbook.|  
|[Exchange.Contents](exchange-contents.md)|Returns a table of contents from a Microsoft Exchange account.| 
|[Facebook.Graph](facebook-graph.md)|Returns a table containing content from the Facebook graph .|  
|[File.Contents](file-contents.md)|Returns the binary contents of the file located at a path.|  
|[Folder.Contents](folder-contents.md)|Returns a table containing the properties and contents of the files and folders found at path.|  
|[Folder.Files](folder-files.md)|Returns a table containing a row for each file found at a folder path, and subfolders. Each row contains properties of the folder or file and a link to its content.|  
|[GoogleAnalytics.Accounts](googleanalytics-accounts.md)|Returns the Google Analytics accounts for the current credential.| 
|[Hdfs.Contents](hdfs-contents.md)|Returns a table containing a row for each folder and file found at the folder url, {0}, from a Hadoop file system. Each row contains properties of the folder or file and a link to its content.|  
|[Hdfs.Files](hdfs-files.md)|Returns a table containing a row for each file found at the folder url, {0}, and subfolders from a Hadoop file system. Each row contains properties of the file and a link to its content.|  
|[HdInsight.Containers](hdinsight-containers.md)|Returns a navigational table containing all containers found in the HDInsight account. Each row has the container name and table containing its files.|  
|[HdInsight.Contents](hdinsight-contents.md)|Returns a navigational table containing all containers found in the HDInsight account. Each row has the container name and table containing its files.|  
|[HdInsight.Files](hdinsight-files.md)|Returns a table containing a row for each folder and file found at the container URL, and subfolders from an HDInsight account. Each row contains properties of the file/folder and a link to its content.|  
|[Informix.Database](informix-database.md)|Returns a table of SQL tables and views available in an Informix database on server <code>server</code> in the database instance named <code>database</code>.|  
|[Json.Document](json-document.md)|Returns the contents of a JSON document. The contents may be directly passed to the function as text, or it may be the binary value returned by a function like File.Contents.|  
|[Json.FromValue](json-fromvalue.md)|Produces a JSON representation of a given value value with a text encoding specified by encoding.|
|[MySQL.Database](mysql-database.md)|Returns a table with data relating to the tables in the specified MySQL Database.| 
|[OData.Feed](odata-feed.md)|Returns a table of OData feeds offered by an OData serviceUri.|  
|[Odbc.DataSource](odbc-datasource.md)|Returns a table of SQL tables and views from the ODBC data source specified by the connection string <code>connectionString</code>. |  
|[Odbc.InferOptions](odbc-inferoptions.md)|Returns the result of trying to infer SQL capabilities for an ODBC driver. |  
|[Odbc.Query](odbc-query.md)|Connects to a generic provider with the given connection string and returns the result of evaluating the query.|  
|[OleDb.DataSource](oledb-datasource.md)|Returns a table of SQL tables and views from the OLE DB data source specified by the connection string.| 
|[OleDb.Query](oledb-query.md)|Returns the result of running a native query on an OLE DB data source.| 
|[Oracle.Database](oracle-database.md)|Returns a table with data relating to the tables in the specified Oracle Database.| 
|[PostgreSQL.Database](postgresql-database.md)|Returns a table with data relating to the tables in the specified PostgreSQL Database.|
|[RData.FromBinary](rdata-frombinary.md)|Returns a record of data frames from the RData file.|  
|[Salesforce.Data](salesforce-data.md)|Connects to the Salesforce Objects API and returns the set of available objects (i.e. Accounts).|  
|[Salesforce.Reports](salesforce-reports.md)|Connects to the Salesforce Reports API and returns the set of available reports.|  
|[SapBusinessObjects.Universes](sapbusinessobjects-universes.md)|Connects to the SAP BusinessObjects BI Universe at the specified URL and returns the set of available universes.|  
|[SapBusinessWarehouse.Cubes](sapbusinesswarehouse-cubes.md)|Returns the InfoCubes and queries in an SAP Business Warehouse system grouped by InfoArea.| 
|[SapBusinessWarehouseExecutionMode.DataStream](sapbusinesswarehouseexecutionmode.datastream.md)|'DataStream flattening mode' option for MDX execution in SAP Business Warehouse.| 
|[SapBusinessWarehouseExecutionMode.BasXml](sapbusinesswarehouseexecutionmode.basxml.md)|'bXML flattening mode' option for MDX execution in SAP Business Warehouse.| 
|[SapBusinessWarehouseExecutionMode.BasXmlGzip](sapbusinesswarehouseexecutionmode.basxmlgzip.md)|'Gzip compressed bXML flattening mode' option for MDX execution in SAP Business Warehouse. Recommended for low latency or high volume queries.| 
|[SapHana.Database](saphana-database.md)|Returns the packages in an SAP HANA database.| 
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
|[SharePoint.Contents](sharepoint-contents.md)|Returns a table containing a row for each folder and document found at the SharePoint site url. Each row contains properties of the folder or file and a link to its content.|  
|[SharePoint.Files](sharepoint-files.md)|Returns a table containing a row for each document found at the SharePoint site url, and subfolders. Each row contains properties of the folder or file and a link to its content.| 
|[SharePoint.Tables](sharepoint-tables.md)|Returns a table containing the result of a SharePoint List as an OData feed.|  
|[Soda.Feed](soda-feed.md)|Returns the resulting table of a CSV file that can be accessed using the SODA 2.0 API. The URL must point to a valid SODA-compliant source that ends in a .csv extension.|  
|[Sql.Database](sql-database.md)|Returns a table containing SQL tables located on a SQL Server instance database.|
|[Sql.Databases](sql-databases.md)|Returns a table with references to databases located on a SQL Server instance. Returns a navigation table.|  
|[Sybase.Database](sybase-database.md)|Returns a table with data relating to the tables in the specified Sybase Database.|  
|[Teradata.Database](teradata-database.md)|Returns a table with data relating to the tables in the specified Teradata Database.|  
|[WebAction.Request](webaction-request.md)|Creates an action that, when executed, will return the results of performing a method request against url using HTTP as a binary value.|  
|[Web.Contents](web-contents.md)|Returns the contents downloaded from a web url as a binary value.| 
|[Web.Page](web-page.md)|Returns the contents of an HTML webpage as a table.|  
|[WebMethod.Delete](webmethod-delete.md) | Specifies the DELETE method for HTTP.|
|[WebMethod.Get](webmethod-get.md) | Specifies the GET method for HTTP.|
|[WebMethod.Head](webmethod-head.md) | Specifies the HEAD method for HTTP.|
|[WebMethod.Patch](webmethod-patch.md) | Specifies the PATCH method for HTTP.|
|[WebMethod.Post](webmethod-post.md) | Specifies the POST method for HTTP.|
|[WebMethod.Put](webmethod-put.md) | Specifies the PUT method for HTTP.|
|[Xml.Document](xml-document.md)|Returns the contents of an XML document as a hierarchical table (list of records).|  
|[Xml.Tables](xml-tables.md)|Returns the contents of an XML document as a nested collection of flattened tables.|  


  
