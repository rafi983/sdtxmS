# Problem 6 - ER Diagram: Simple Online Retail System
# No database connection needed.

print("""
ER DIAGRAM - Simple Online Retail System
=========================================

  +------------------+          +------------------+
  |     CUSTOMER     |          |     CATEGORY     |
  +------------------+          +------------------+
  | *CustomerID      |          | *CategoryID      |
  |  Name            |          |  CategoryName    |
  |  Email           |          +--------+---------+
  |  Phone           |                   | 1
  |  Address         |                   |
  +--------+---------+                   | N
           | 1               +-----------+----------+
           |                 |        PRODUCT       |
           | N               +----------------------+
  +--------+---------+       | *ProductID           |
  |       ORDER      |       |  Name                |
  +------------------+       |  Description         |
  | *OrderID         |       |  Price               |
  | #CustomerID      |       |  StockQty            |
  |  OrderDate       |       | #CategoryID          |
  |  Status          |       +----------+-----------+
  |  TotalAmount     |                  | 1
  +--------+---------+                  |
           | 1                          | N
           |               +------------+----------+
           | N             |       ORDER_ITEM      |
           +---------------+----------------------+
                           | *OrderItemID         |
                           | #OrderID             |
                           | #ProductID           |
                           |  Quantity            |
                           |  UnitPrice           |
                           +----------------------+

Legend:  * = Primary Key    # = Foreign Key

Relationships:
  - One CUSTOMER places many ORDERs              (1:N)
  - One ORDER contains many ORDER_ITEMs          (1:N)
  - One PRODUCT appears in many ORDER_ITEMs      (1:N)
  - One CATEGORY has many PRODUCTs               (1:N)
  - ORDER and PRODUCT have a M:N relationship
    resolved through ORDER_ITEM
""")
