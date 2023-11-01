# count할 때, 중복은 제거해서 count 하도록 하기
SELECT COUNT(DISTINCT NAME) 
FROM ANIMAL_INS 
# null인 값 제거 
WHERE NAME IS NOT NULL ;