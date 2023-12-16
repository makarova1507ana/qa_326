use shop;
# https://docs.google.com/document/d/1XKWRqu-CmtBfFTihvkW5tS0W8EHorrDox9fuJZEW1tQ/edit?usp=sharing 

-- CREATE VIEW info_order
-- AS SELECT amt, odate, cname
-- FROM orders, customers
-- WHERE orders.id_customer = customers.id;

select * from info_order;
SELECT sum(amt), cname 
FROM info_order 
group by cname;