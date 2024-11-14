select O.ANIMAL_ID, O.ANIMAL_TYPE, O.NAME
from ANIMAL_OUTS O
    join ANIMAL_INS I on O.ANIMAL_ID = I.ANIMAL_ID
where I.SEX_UPON_INTAKE like 'Intact%' and (O.SEX_UPON_OUTCOME like 'Neutered%' or O.SEX_UPON_OUTCOME like 'Spayed%') 
