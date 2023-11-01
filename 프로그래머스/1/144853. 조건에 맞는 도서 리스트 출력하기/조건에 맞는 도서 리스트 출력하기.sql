
/*
1. 2021년에 출판
2. '인문' 카테고리에 속하는 도서
3. 출판일을 기준으로 오름차순 정렬
*/
SELECT BOOK_ID, DATE_FORMAT(PUBLISHED_DATE, '%Y-%m-%d') AS PUBLISHED_DATE
FROM BOOK
WHERE YEAR(PUBLISHED_DATE)=2021
      AND CATEGORY = '인문'
ORDER BY PUBLISHED_DATE

; 