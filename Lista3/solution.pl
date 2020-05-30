:- use_module(library(clpfd)).
solve([V0_0, V0_1, V0_2, V0_3, V0_4, V0_5, V0_6, V0_7, V0_8, V1_0, V1_1, V1_2, V1_3, V1_4, V1_5, V1_6, V1_7, V1_8, V2_0, V2_1, V2_2, V2_3, V2_4, V2_5, V2_6, V2_7, V2_8, V3_0, V3_1, V3_2, V3_3, V3_4, V3_5, V3_6, V3_7, V3_8, V4_0, V4_1, V4_2, V4_3, V4_4, V4_5, V4_6, V4_7, V4_8, V5_0, V5_1, V5_2, V5_3, V5_4, V5_5, V5_6, V5_7, V5_8, V6_0, V6_1, V6_2, V6_3, V6_4, V6_5, V6_6, V6_7, V6_8, V7_0, V7_1, V7_2, V7_3, V7_4, V7_5, V7_6, V7_7, V7_8, V8_0, V8_1, V8_2, V8_3, V8_4, V8_5, V8_6, V8_7, V8_8]) :- 
    V0_0 in 1..9, V0_1 in 1..9, V0_2 in 1..9, V0_3 in 1..9, V0_4 in 1..9, V0_5 in 1..9, 
    V0_6 in 1..9, V0_7 in 1..9, V0_8 in 1..9, V1_0 in 1..9, V1_1 in 1..9, V1_2 in 1..9, 
    V1_3 in 1..9, V1_4 in 1..9, V1_5 in 1..9, V1_6 in 1..9, V1_7 in 1..9, V1_8 in 1..9, 
    V2_0 in 1..9, V2_1 in 1..9, V2_2 in 1..9, V2_3 in 1..9, V2_4 in 1..9, V2_5 in 1..9, 
    V2_6 in 1..9, V2_7 in 1..9, V2_8 in 1..9, V3_0 in 1..9, V3_1 in 1..9, V3_2 in 1..9, 
    V3_3 in 1..9, V3_4 in 1..9, V3_5 in 1..9, V3_6 in 1..9, V3_7 in 1..9, V3_8 in 1..9, 
    V4_0 in 1..9, V4_1 in 1..9, V4_2 in 1..9, V4_3 in 1..9, V4_4 in 1..9, V4_5 in 1..9, 
    V4_6 in 1..9, V4_7 in 1..9, V4_8 in 1..9, V5_0 in 1..9, V5_1 in 1..9, V5_2 in 1..9, 
    V5_3 in 1..9, V5_4 in 1..9, V5_5 in 1..9, V5_6 in 1..9, V5_7 in 1..9, V5_8 in 1..9, 
    V6_0 in 1..9, V6_1 in 1..9, V6_2 in 1..9, V6_3 in 1..9, V6_4 in 1..9, V6_5 in 1..9, 
    V6_6 in 1..9, V6_7 in 1..9, V6_8 in 1..9, V7_0 in 1..9, V7_1 in 1..9, V7_2 in 1..9, 
    V7_3 in 1..9, V7_4 in 1..9, V7_5 in 1..9, V7_6 in 1..9, V7_7 in 1..9, V7_8 in 1..9, 
    V8_0 in 1..9, V8_1 in 1..9, V8_2 in 1..9, V8_3 in 1..9, V8_4 in 1..9, V8_5 in 1..9, 
    V8_6 in 1..9, V8_7 in 1..9, V8_8 in 1..9, all_distinct([V0_0, V1_0, V2_0, V3_0, V4_0, V5_0, V6_0, V7_0, V8_0]), 
    all_distinct([V0_1, V1_1, V2_1, V3_1, V4_1, V5_1, V6_1, V7_1, V8_1]), 
    all_distinct([V0_2, V1_2, V2_2, V3_2, V4_2, V5_2, V6_2, V7_2, V8_2]), 
    all_distinct([V0_3, V1_3, V2_3, V3_3, V4_3, V5_3, V6_3, V7_3, V8_3]), 
    all_distinct([V0_4, V1_4, V2_4, V3_4, V4_4, V5_4, V6_4, V7_4, V8_4]), 
    all_distinct([V0_5, V1_5, V2_5, V3_5, V4_5, V5_5, V6_5, V7_5, V8_5]), 
    all_distinct([V0_6, V1_6, V2_6, V3_6, V4_6, V5_6, V6_6, V7_6, V8_6]), 
    all_distinct([V0_7, V1_7, V2_7, V3_7, V4_7, V5_7, V6_7, V7_7, V8_7]), 
    all_distinct([V0_8, V1_8, V2_8, V3_8, V4_8, V5_8, V6_8, V7_8, V8_8]), 
    all_distinct([V0_0, V0_1, V0_2, V0_3, V0_4, V0_5, V0_6, V0_7, V0_8]), 
    all_distinct([V1_0, V1_1, V1_2, V1_3, V1_4, V1_5, V1_6, V1_7, V1_8]), 
    all_distinct([V2_0, V2_1, V2_2, V2_3, V2_4, V2_5, V2_6, V2_7, V2_8]), 
    all_distinct([V3_0, V3_1, V3_2, V3_3, V3_4, V3_5, V3_6, V3_7, V3_8]), 
    all_distinct([V4_0, V4_1, V4_2, V4_3, V4_4, V4_5, V4_6, V4_7, V4_8]), 
    all_distinct([V5_0, V5_1, V5_2, V5_3, V5_4, V5_5, V5_6, V5_7, V5_8]), 
    all_distinct([V6_0, V6_1, V6_2, V6_3, V6_4, V6_5, V6_6, V6_7, V6_8]), 
    all_distinct([V7_0, V7_1, V7_2, V7_3, V7_4, V7_5, V7_6, V7_7, V7_8]), 
    all_distinct([V8_0, V8_1, V8_2, V8_3, V8_4, V8_5, V8_6, V8_7, V8_8]), 
    all_distinct([V0_0, V0_1, V0_2, V1_0, V1_1, V1_2, V2_0, V2_1, V2_2]), 
    all_distinct([V0_3, V0_4, V0_5, V1_3, V1_4, V1_5, V2_3, V2_4, V2_5]), 
    all_distinct([V0_6, V0_7, V0_8, V1_6, V1_7, V1_8, V2_6, V2_7, V2_8]), 
    all_distinct([V3_3, V3_4, V3_5, V4_3, V4_4, V4_5, V5_3, V5_4, V5_5]), 
    all_distinct([V3_6, V3_7, V3_8, V4_6, V4_7, V4_8, V5_6, V5_7, V5_8]), 
    all_distinct([V6_6, V6_7, V6_8, V7_6, V7_7, V7_8, V8_6, V8_7, V8_8]), 
    all_distinct([V3_0, V3_1, V3_2, V4_0, V4_1, V4_2, V5_0, V5_1, V5_2]), 
    all_distinct([V6_0, V6_1, V6_2, V7_0, V7_1, V7_2, V8_0, V8_1, V8_2]), 
    V0_0 #= 3, V0_8 #= 1, V1_0 #= 4, V1_3 #= 3, V1_4 #= 8, V1_5 #= 6, V2_5 #= 1, V2_7 #= 4, 
    V3_0 #= 6, V3_2 #= 9, V3_3 #= 2, V3_4 #= 4, V3_7 #= 3, V4_2 #= 3, V5_6 #= 7, V5_7 #= 1, 
    V5_8 #= 9, V6_8 #= 6, V7_0 #= 2, V7_2 #= 7, V7_6 #= 3, 
    labeling([ff], [V0_0, V0_1, V0_2, V0_3, V0_4, V0_5, V0_6, V0_7, V0_8, V1_0, V1_1, V1_2, V1_3, V1_4, V1_5, V1_6, V1_7, V1_8, V2_0, V2_1, V2_2, V2_3, V2_4, V2_5, V2_6, V2_7, V2_8, V3_0, V3_1, V3_2, V3_3, V3_4, V3_5, V3_6, V3_7, V3_8, V4_0, V4_1, V4_2, V4_3, V4_4, V4_5, V4_6, V4_7, V4_8, V5_0, V5_1, V5_2, V5_3, V5_4, V5_5, V5_6, V5_7, V5_8, V6_0, V6_1, V6_2, V6_3, V6_4, V6_5, V6_6, V6_7, V6_8, V7_0, V7_1, V7_2, V7_3, V7_4, V7_5, V7_6, V7_7, V7_8, V8_0, V8_1, V8_2, V8_3, V8_4, V8_5, V8_6, V8_7, V8_8]).

:- solve(X), write(X), nl.
