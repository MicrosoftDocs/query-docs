---
description: "Learn more about: Accessing data functions"
title: "Accessing data functions"
ms.date: 7/16/2025
ms.custom: "nonautomated-date"
---
# Accessing data functions

These functions access data and return table values. Most of these functions return a table value called a **navigation table**. Navigation tables are primarily used by the Power Query user interface to provide a navigation experience over the potentially large hierarchical data sets returned.

|Name|Description|
|------------|---------------|
|[AccessControlEntry.ConditionToIdentities](accesscontrolentry-conditiontoidentities.md)|Returns a list of identities that the condition will accept.|
|[Access.Database](access-database.md)|Returns a structural representation of a Microsoft Access database. |
|[ActiveDirectory.Domains](activedirectory-domains.md)|Returns a list of Active Directory domains in the same forest as the specified domain or of the current machine's domain if none is specified.|
|[AdobeAnalytics.Cubes](adobeanalytics-cubes.md) | Returns the report suites in Adobe Analytics.|
|[AdoDotNet.DataSource](adodotnet-datasource.md)|Returns the schema collection for an ADO.NET data source.|
|[AdoDotNet.Query](adodotnet-query.md)|Returns the result of running a native query on an ADO.NET data source.|
|[AnalysisServices.Database](analysisservices-database.md)|Returns a table of multidimensional cubes or tabular models from the Analysis Services database.|
|[AnalysisServices.Databases](analysisservices-databases.md)|Returns the Analysis Services databases on a particular host.|
|[AzureStorage.BlobContents](azurestorage-blobcontents.md) |Returns the content of the specified blob from an Azure storage vault. |
|[AzureStorage.Blobs](azurestorage-blobs.md)|Returns a navigational table containing the containers found in the specified account from an Azure storage vault. Each row has the container name and a link to the container blobs.|
|[AzureStorage.DataLake](azurestorage-datalake.md)|Returns a navigational table containing the documents found in the specified container and its subfolders from Azure Data Lake Storage.|
|[AzureStorage.DataLakeContents](azurestorage-datalakecontents.md)|Returns the content of the specified file from an Azure Data Lake Storage filesystem.|
|[AzureStorage.Tables](azurestorage-tables.md)|Returns a navigational table containing the tables found in the specified account from an Azure storage vault. Each row contains a link to the azure table.|
|[Cdm.Contents](cdm-contents.md)|This function is unavailable because it requires .NET 4.5.|
|[Csv.Document](csv-document.md)|Returns the contents of the CSV document as a table using the specified encoding.|
|[Cube.AddAndExpandDimensionColumn](cube-addandexpanddimensioncolumn.md)|Merges the specified dimension table into the cube’s filter context and changes the dimensional granularity of the filter context by expanding the specified set of dimension attributes.|
|[Cube.AddMeasureColumn](cube-addmeasurecolumn.md)|AAdds a column to the cube that contains the results of the measure applied in the row context of each row.|
|[Cube.ApplyParameter](cube-applyparameter.md)|Returns a cube after applying a parameter to it.|
|[Cube.AttributeMemberId](cube-attributememberid.md)|Returns the unique member identifier from members property value.|
|[Cube.AttributeMemberProperty](cube-attributememberproperty.md) | Returns a property of a dimension attribute.|
|[Cube.CollapseAndRemoveColumns](cube-collapseandremovecolumns.md)|Changes the dimensional granularity of the filter context for the cube by collapsing the attributes mapped to the specified columns.|
|[Cube.Dimensions](cube-dimensions.md)|Returns a table containing the set of available dimensions.|
|[Cube.DisplayFolders](cube-displayfolders.md)|Returns a nested tree of tables representing the display folder hierarchy of the objects (for example, dimensions and measures).|
|[Cube.MeasureProperties](cube-measureproperties.md)|Returns a table containing the set of available measure properties that are expanded in the cube.|
|[Cube.MeasureProperty](cube-measureproperty.md)|Returns a property of a measure (cell property).|
|[Cube.Measures](cube-measures.md)|Returns a table containing the set of available measures.|
|[Cube.Parameters](cube-parameters.md)|Returns a table containing the set of parameters that can be applied to the cube.|
|[Cube.Properties](cube-properties.md)|Returns a table containing the set of available properties for dimensions that are expanded in the cube.|
|[Cube.PropertyKey](cube-propertykey.md) | Returns the key of a property.|
|[Cube.ReplaceDimensions](cube-replacedimensions.md)|Replaces the set of dimensions returned by [Cube.Dimensions](/powerquery-m/cube-dimensions).|
|[Cube.Transform](cube-transform.md)|Applies a list of cube functions.|
|[DB2.Database](db2-database.md)|Returns a table of SQL tables and views available in a Db2 database.|
|[DeltaLake.Metadata](deltalake-metadata.md)|This function is unavailable in the current context.|
|[DeltaLake.Table](deltalake-table.md)|This function is unavailable in the current context.|
|[Essbase.Cubes](essbase-cubes.md)|Returns the cubes in an Essbase instance grouped by Essbase server.|
|[Excel.CurrentWorkbook](excel-currentworkbook.md)|Returns the contents of the current Excel workbook.|
|[Excel.Workbook](excel-workbook.md)|Returns the contents of the Excel workbook.|
|[Exchange.Contents](exchange-contents.md)|Returns a table of contents from a Microsoft Exchange account.|
|[File.Contents](file-contents.md)|Returns the contents of the specified file as binary.|
|[Folder.Contents](folder-contents.md)|Returns a table containing the properties and contents of the files and folders found in the specified folder.|
|[Folder.Files](folder-files.md)|Returns a table containing the properties and contents of the files found in the specified folder and subfolders. Each row contains properties of the folder or file and a link to its content.|
|[GoogleAnalytics.Accounts](googleanalytics-accounts.md)|Returns the Google Analytics accounts for the current credential.|
|[Hdfs.Contents](hdfs-contents.md)|Returns a table containing the properties and contents of the files and folders found in the specified folder from a Hadoop file system. Each row contains properties of the folder or file and a link to its content.|
|[Hdfs.Files](hdfs-files.md)|Returns a table containing the properties and contents of the files found in the specified folder and subfolders from a Hadoop file system. Each row contains properties of the file and a link to its content.|
|[HdInsight.Containers](hdinsight-containers.md)|Returns a navigational table containing the containers found in the specified account from an Azure storage vault. Each row has the container name and table containing its files.|
|[HdInsight.Contents](hdinsight-contents.md)|Returns a navigational table containing the containers found in the specified account from an Azure storage vault. Each row has the container name and table containing its files.|
|[HdInsight.Files](hdinsight-files.md)|Returns a table containing the properties and contents of the blobs found in the specified container from an Azure storage vault. Each row contains properties of the file/folder and a link to its content.|
|[Html.Table](html-table.md)|Returns a table containing the results of running the specified CSS selectors against the provided HTML.|
|[Identity.From](identity-from.md)|Creates an identity.|
|[Identity.IsMemberOf](identity-ismemberof.md)|Determines whether an identity is a member of an identity collection.|
|[IdentityProvider.Default](identityprovider-default.md)|The default identity provider for the current host.|
|[Informix.Database](informix-database.md)|Returns a table of SQL tables and views available in an Informix database.|
|[Json.Document](json-document.md)|Returns the content of the JSON document. The contents can be directly passed to the function as text, or it can be the binary value returned by a function like [File.Contents](file-contents.md).|
|[Json.FromValue](json-fromvalue.md)|Produces a JSON representation of a given value value with a text encoding specified by encoding.|
|[MySQL.Database](mysql-database.md)|Returns a table of SQL tables, views, and stored scalar functions available in a MySQL database.|
|[OData.Feed](odata-feed.md)|Returns a table of OData feeds offered by an OData service.|
|[Odbc.DataSource](odbc-datasource.md)|Returns a table of SQL tables and views from the ODBC data source.|
|[Odbc.InferOptions](odbc-inferoptions.md)|Returns the result of trying to infer SQL capabilities for an ODBC driver. |
|[Odbc.Query](odbc-query.md)|Returns the result of running a native query on an ODBC data source.|
|[OleDb.DataSource](oledb-datasource.md)|Returns a table of SQL tables and views from the OLE DB data source.|
|[OleDb.Query](oledb-query.md)|Returns the result of running a native query on an OLE DB data source.|
|[Oracle.Database](oracle-database.md)|Returns a table of SQL tables and views from the Oracle database.|
|[Pdf.Tables](pdf-tables.md)|This function is unavailable in the current context.|
|[PostgreSQL.Database](postgresql-database.md)|Returns a table of SQL tables and views available in a PostgreSQL database.|
|[RData.FromBinary](rdata-frombinary.md)|Returns a record of data frames from the RData file.|
|[Salesforce.Data](salesforce-data.md)|Returns the objects from the Salesforce account.|
|[Salesforce.Reports](salesforce-reports.md)|Returns the reports from the Salesforce account.|
|[SapBusinessWarehouse.Cubes](sapbusinesswarehouse-cubes.md)|Returns the InfoCubes and queries in an SAP Business Warehouse system grouped by InfoArea.|
|[SapHana.Database](saphana-database.md)|Returns the packages in an SAP HANA database.|
|[SharePoint.Contents](sharepoint-contents.md)|Returns a table containing content from a SharePoint site. Each row contains properties of the folder or file and a link to its content.|
|[SharePoint.Files](sharepoint-files.md)|Returns a table containing documents from a SharePoint site. Each row contains properties of the folder or file and a link to its content.|
|[SharePoint.Tables](sharepoint-tables.md)|Returns a table containing content from a SharePoint List.|
|[Soda.Feed](soda-feed.md)|Returns a table from the contents at the specified URL formatted according to the SODA 2.0 API. The URL must point to a valid SODA-compliant source that ends in a .csv extension.|
|[Sql.Database](sql-database.md)|Returns a table of SQL tables, views, and stored functions from the SQL Server database.|
|[Sql.Databases](sql-databases.md)|Returns a table of databases on a SQL Server.|
|[Sybase.Database](sybase-database.md)|Returns a table of SQL tables and views available in a Sybase database.|
|[Teradata.Database](teradata-database.md)|Returns a table of SQL tables and views from the Teradata database.|
|[WebAction.Request](webaction-request.md)|Creates an action that, when executed, will return the results of performing a method request against url using HTTP as a binary value.|
|[Web.BrowserContents](web-browsercontents.md)|Returns the HTML for the specified URL, as viewed by a web browser.|
|[Web.Contents](web-contents.md)|Returns the contents downloaded from the URL as binary.|
|[Web.Headers](web-headers.md)|Returns the HTTP headers downloaded from the URL as a record value.|
|[Web.Page](web-page.md)|Returns the contents of the HTML document broken into its constituent structures, as well as a representation of the full document and its text after removing tags.|
|[Xml.Document](xml-document.md)|Returns the contents of the XML document as a hierarchical table (list of records).|
|[Xml.Tables](xml-tables.md)|Returns the contents of an XML document as a nested collection of flattened tables.|
