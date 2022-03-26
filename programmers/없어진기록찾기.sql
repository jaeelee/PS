--# **************************************************************************** #
--#                                                                              #
--#                                                         :::      ::::::::    #
--#    없어진기록찾기.sql                                     :+:      :+:    :+:    #
--#                                                     +:+ +:+         +:+      #
--#    By: jaeelee <jaeelee@student.42seoul.kr>       +#+  +:+       +#+         #
--#                                                 +#+#+#+#+#+   +#+            #
--#    Created: 2022/03/23 20:01:27 by jaeelee           #+#    #+#              #
--#    Updated: 2022/03/23 20:01:27 by jaeelee          ###   ########seoul.kr   #
--#                                                                              #
--# **************************************************************************** #

-- outer join 을 사용하는 문제
-- 참고 : https://bit.ly/3ulsdp9
select ANIMAL_OUTS.ANIMAL_ID, ANIMAL_OUTS.NAME
from ANIMAL_OUTS left outer join ANIMAL_INS
on ANIMAL_INS.ANIMAL_ID=ANIMAL_OUTS.ANIMAL_ID
where ANIMAL_INS.ANIMAL_ID is null
ORDER BY ANIMAL_OUTS.ANIMAL_ID