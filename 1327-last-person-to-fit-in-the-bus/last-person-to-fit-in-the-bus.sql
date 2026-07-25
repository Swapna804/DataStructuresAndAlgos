# Write your MySQL query statement below
select person_name from(select *,sum(weight) over(order by turn)as running_weight from Queue )q
where running_weight <=1000
order by running_weight desc limit 1;
