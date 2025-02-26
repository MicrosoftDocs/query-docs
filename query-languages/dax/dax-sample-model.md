---
title: "DAX sample model"
description: DAX sample model to support reference articles.
author: peter-myers
ms.topic: conceptual
---

# DAX sample model

The **Adventure Works DW 2020** Power BI Desktop sample model is designed to support your DAX learning. The model is based on the [Adventure Works data warehouse sample](/sql/samples/adventureworks-install-configure#data-warehouse-downloads) for AdventureWorksDW2017—however, the data has been modified to suit the objectives of the sample model.

The sample model does not contain any DAX formulas. It does however support hundreds or even thousands of potential calculation formulas and queries. Some function examples, like those in CALCULATE, DATESBETWEEN, DATESIN PERIOD, IF, and LOOKUPVALUE can be added to the sample model without modification. We're working on including more examples in other function reference articles that work with the sample model.

## Scenario

:::image type="content" source="media/dax-sample-model/adventure-works-logo-150x150.png" alt-text="An image of the Adventure Works company logo is shown.":::

The Adventure Works company represents a bicycle manufacturer that sells bicycles and accessories to global markets. The company has their data warehouse data stored in an Azure SQL Database.

## Model structure

The model has seven tables:

|**Table**|**Description**|
|-----|-------|
|**Customer**|Describes customers and their geographic location. Customers purchase products online (Internet sales).|
|**Date**|There are three relationships between the **Date** and **Sales** tables, for order date, ship date, and due date. The order date relationship is active. The company's reports sales using a fiscal year that commences on July 1 of each year. The table is marked as a date table using the **Date** column.|
|**Product**|Stores finished products only.|
|**Reseller**|Describes resellers and their geographic location. Reseller on sell products to their customers.|
|**Sales**|Stores rows at sales order line grain. All financial values are in US dollars (USD). The earliest order date is July 1, 2017, and the latest order date is June 15, 2020.|
|**Sales Order**|Describes sales order and order line numbers, and also the sales channel, which is either **Reseller** or **Internet**. This table has a one-to-one relationship with the **Sales** table.|
|**Sales Territory**|Sales territories are organized into groups (North America, Europe, and Pacific), countries, and regions. Only the United States sells products at the region level.|

## Download sample

Download the Power BI Desktop sample model file [here](https://aka.ms/dax-docs-sample-file).

## Related content

- Learning path: [Use DAX in Power BI Desktop](/training/paths/dax-power-bi/)
- Questions? [Try asking the Power BI Community](https://community.powerbi.com/)
- Suggestions? [Contribute ideas to improve Power BI](https://ideas.powerbi.com)
