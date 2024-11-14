select J.FLAVOR
from JULY J
    join FIRST_HALF F on J.FLAVOR = F.FLAVOR
group by J.FLAVOR
order by sum(J.TOTAL_ORDER)+ sum(F.TOTAL_ORDER) desc
limit 3