def cableresistance():
   string = '''Size,Earth Size,Multicore_PVC_Reactance,Multicore_PVC_Resistance,Multicore_XLPE_Reactance,Multicore_XLPE_Resistance,Single Core_PVC_Reactance,Single Core_PVC_Resistance,Single Core_XLPE_Reactance,Single Core_XLPE_Resistance
mm2,mm2,ohm/km,ohm/km,ohm/km,ohm/km,ohm/km,ohm/km,ohm/km,ohm/km
2.5,2.5,0.102,9.01,0.0988,9.45,0.143,9.01,0.141,9.45
4,2.5,0.102,5.61,0.093,5.88,0.137,5.61,0.131,5.88
6,2.5,0.0967,3.75,0.0887,3.93,0.128,3.75,0.123,3.93
10,4,0.0906,2.23,0.084,2.33,0.118,2.23,0.114,2.33
16,6,0.0861,1.4,0.0805,1.47,0.111,1.4,0.106,1.47
25,6,0.0853,0.884,0.0808,0.927,0.106,0.884,0.102,0.927
35,10,0.0826,0.638,0.0786,0.669,0.101,0.638,0.0982,0.668
50,16,0.0797,0.471,0.0751,0.494,0.0962,0.471,0.0924,0.494
70,25,0.077,0.327,0.0741,0.343,0.0917,0.327,0.0893,0.342
95,25,0.0766,0.236,0.0725,0.248,0.0904,0.236,0.0868,0.247
120,35,0.0743,0.188,0.0713,0.197,0.087,0.188,0.0844,0.197
150,50,0.0745,0.153,0.0718,0.16,0.0868,0.153,0.0844,0.16
185,70,0.0744,0.123,0.072,0.129,0.0862,0.123,0.0835,0.129
240,95,0.0735,0.0955,0.0709,0.0998,0.0847,0.0948,0.0818,0.0991
300,120,0.0732,0.0778,0.0704,0.0812,0.0839,0.077,0.0809,0.0803
400,120,0.0728,0.063,0.0702,0.0656,0.0829,0.062,0.0802,0.0646
500,120,0.0723,0.0525,0.07,0.0544,0.082,0.0506,0.0796,0.0525
630,120,#N/A,#N/A,#N/A,#N/A,0.08,0.0418,0.0787,0.0432'''
   from io import StringIO
   f = StringIO(string)
   return f

def mcore_pvc_res_data():
   string ='''Size,Multicore_PVC_Reactance,Multicore_PVC_Resistance
mm2,ohm/km,ohm/km
2.5,0.102,9.01
4,0.102,5.61
6,0.0967,3.75
10,0.0906,2.23
16,0.0861,1.4
25,0.0853,0.884
35,0.0826,0.638
50,0.0797,0.471
70,0.077,0.327
95,0.0766,0.236
120,0.0743,0.188
150,0.0745,0.153
185,0.0744,0.123
240,0.0735,0.0955
300,0.0732,0.0778
400,0.0728,0.063
500,0.0723,0.0525
630,#N/A,#N/A
   '''
   from io import StringIO
   f = StringIO(string)
   return f


def mcore_xlpe_res_data():
   string ='''Size,Multicore_XLPE_Reactance,Multicore_XLPE_Resistance
mm2,ohm/km,ohm/km
2.5,0.0988,9.45
4,0.093,5.88
6,0.0887,3.93
10,0.084,2.33
16,0.0805,1.47
25,0.0808,0.927
35,0.0786,0.669
50,0.0751,0.494
70,0.0741,0.343
95,0.0725,0.248
120,0.0713,0.197
150,0.0718,0.16
185,0.072,0.129
240,0.0709,0.0998
300,0.0704,0.0812
400,0.0702,0.0656
500,0.07,0.0544
630,#N/A,#N/A
   '''
   from io import StringIO
   f = StringIO(string)
   return f

def score_pvc_res_data():
   string ='''Size,Single Core_PVC_Reactance,Single Core_PVC_Resistance
mm2,ohm/km,ohm/km
2.5,0.143,9.01
4,0.137,5.61
6,0.128,3.75
10,0.118,2.23
16,0.111,1.4
25,0.106,0.884
35,0.101,0.638
50,0.0962,0.471
70,0.0917,0.327
95,0.0904,0.236
120,0.087,0.188
150,0.0868,0.153
185,0.0862,0.123
240,0.0847,0.0948
300,0.0839,0.077
400,0.0829,0.062
500,0.082,0.0506
630,0.08,0.0418
   '''
   from io import StringIO
   f = StringIO(string)
   return f

def score_xlpe_res_data():
   string ='''Size,Single Core_XLPE_Reactance,Single Core_XLPE_Resistance
mm2,ohm/km,ohm/km
2.5,0.141,9.45
4,0.131,5.88
6,0.123,3.93
10,0.114,2.33
16,0.106,1.47
25,0.102,0.927
35,0.0982,0.668
50,0.0924,0.494
70,0.0893,0.342
95,0.0868,0.247
120,0.0844,0.197
150,0.0844,0.16
185,0.0835,0.129
240,0.0818,0.0991
300,0.0809,0.0803
400,0.0802,0.0646
500,0.0796,0.0525
630,0.0787,0.0432
   '''
   from io import StringIO
   f = StringIO(string)
   return f


def aerial_res_data():
   string = '''Conductor codename,inductive reactance,ac resistance,dc resistance
,0.3m,at 75 deg,at 20 deg
,at 50 hz,at 50 hz,
,ohm/km,ohm/km,ohm/km
Almond,0.296,1.31,0.975
Apricot,0.29,1.08,0.805
Apple,0.285,0.91,0.677
Banana,0.271,0.582,0.433
Cherry,0.256,0.367,0.271
Grape,0.24,0.263,0.196
Lemon,0.228,0.167,0.136
Lychee,0.223,0.142,0.116
Lime,0.219,0.123,0.1
Mango,0.212,0.0955,0.0758
Orange,0.207,0.0816,0.0646
Olive,0.202,0.0705,0.0557
Pawpaw,0.198,0.0615,0.0485
Quince,0.346,4.37,3.25
Raisin,0.324,2.14,1.59
Sultana,0.302,1.21,0.897
Walnut,0.288,0.77,0.573
   '''
   from io import StringIO
   f = StringIO(string)
   return f

def aerialcabledata():
   string = '''Conductor codename,Stranding and wire diameter no/mm ,Stranding and wire diameter no/mm ,Nominal overall diameter,Cross-sectional area,Approximate mass,Breaking load,Modulus of elasticity, Coefficient of linear expansion,Product code,,dc resistance,ac resistance,inductive reactance,Rural,Rural,Rural,Rural,Rural,Rural,Industrial,Industrial,Industrial,Industrial,Industrial,Industrial
,,,,,,,,,,,at 20 deg,at 75 deg,0.3m,Winter Night,Winter Night,Winter Night,Summer Noon,Summer Noon,Summer Noon,Winter Night,Winter Night,Winter Night,Summer Noon,Summer Noon,Summer Noon
,,,,,,,,,,,,at 50 hz,at 50 hz,still air,1m/s, 2m/s,still air,1m/s, 2m/s,still air,1m/s, 2m/s,still air,1m/s, 2m/s
,Aluminium,Steel,mm,mm2,kg/km,kN,GPa,X10-6/degC,codename,,ohm/km,ohm/km,ohm/km,A,A,A,A,A,A,A,A,A,A,A,A
Almond,6/2.50,1/2.50,7.5,34.4,119,10.5,83,19.3,Almond,Almond,0.975,1.31,0.296,108,186,216,84,167,198,116,190,220,79,164,196
Apricot,6/2.75,1/2.75,8.3,41.6,144,12.6,83,19.3,Apricot,Apricot,0.805,1.08,0.29,123,209,244,95,188,223,131,215,248,89,184,220
Apple,6/3.00,1/3.00,9,49.5,171,14.9,83,19.3,Apple,Apple,0.677,0.91,0.285,138,233,272,107,209,248,148,240,277,98,205,244
Banana,6/3.75,1/3.75,11.3,77.3,268,22.7,83,19.3,Banana,Banana,0.433,0.582,0.271,187,309,359,141,274,326,201,318,367,129,268,321
Cherry,6/4.75,7/1.60,14.3,120,402,33.4,80,19.9,Cherry,Cherry,0.271,0.367,0.256,259,416,483,191,364,434,280,430,495,171,354,426
Grape,30/2.50,7/2.50,17.5,182,677,63.5,88,18.4,Grape,Grape,0.196,0.263,0.24,330,513,598,238,449,531,361,532,614,211,436,520
Lemon,30/3.00,7/3.00,21,262,973,90.4,88,18.4,Lemon,Lemon,0.136,0.167,0.228,441,680,787,307,586,698,482,707,811,269,567,682
Lychee,30/3.25,7/3.25,22.8,307,1140,105,88,18.4,Lychee,Lychee,0.116,0.142,0.223,493,752,879,341,645,769,540,783,906,298,623,751
Lime,30/3.50,7/3.50,24.5,356,1320,122,88,18.4,Lime,Lime,0.1,0.123,0.219,548,826,976,377,706,843,601,862,1007,328,681,823
Mango,54/3.00,7/3.00,27,431,1440,119,78,19.9,Mango,Mango,0.0758,0.0955,0.212,648,960,1147,443,816,991,711,1003,1183,383,786,966
Orange,54/3.25,7/3.25,29.3,506,1690,137,78,19.9,Orange,Orange,0.0646,0.0816,0.207,724,1061,1282,492,898,1106,796,1110,1323,424,863,1078
Olive,54/3.50,7/3.50,31.5,587,1960,159,78,19.9,Olive,Olive,0.0557,0.0705,0.202,804,1165,1421,543,981,1225,884,1220,1466,466,941,1194
Pawpaw,54/3.75,19/2.25,33.8,672,2240,178,77,20,Pawpaw,Pawpaw,0.0485,0.0615,0.198,885,1270,1563,595,1065,1347,974,1333,1614,508,1020,1312
Quince,3/1.75,4/1.75,5.3,16.8,95,12.7,136,13.9,Quince,Quince,3.25,4.37,0.346,53,93,108,42,85,100,56,95,110,40,83,99
Raisin,3/2.50,4/2.50,7.5,34.4,195,24.4,136,13.9,Raisin,Raisin,1.59,2.14,0.324,85,145,169,66,131,155,91,149,172,61,129,153
Sultana,4/3.00,3/3.00,9,49.5,243,28.3,119,15.2,Sultana,Sultana,0.897,1.21,0.302,120,203,236,91,181,215,129,208,241,84,178,212
Walnut,4/3.75,3/3.75,11.3,77.3,380,43.9,119,15.2,Walnut,Walnut,0.573,0.77,0.288,161,269,312,121,238,283,175,277,319,111,233,279
'''

def mcore_pvc_unenclosed_amp():
   string = '''size mm2,un-enclosed spaced 3 phase,un-enclosed spaced 1 phase
2.5,23,27
4,31,37
6,40,46
10,54,64
16,72,85
25,97,113
35,120,139
50,146,170
70,185,215
95,228,265
120,265,307
150,303,351
185,348,403
240,412,477
300,472,547
400,544,631
500,616,716
630,#N/A,#N/A
   '''
   from io import StringIO
   f = StringIO(string)
   return f

def mcore_pvc_dburied_amp():
   string = '''size,direct buried 3 phase,direct buried 1 phase
2.5,25,30
4,33,39
6,42,50
10,55,66
16,96,114
25,125,147
35,150,178
50,178,211
70,219,259
95,263,311
120,300,355
150,336,398
185,379,449
240,438,520
300,493,586
400,557,663
500,620,741
630,#N/A,#N/A
   '''
   from io import StringIO
   f = StringIO(string)
   return f

def mcore_pvc_conduit_amp():
   string = '''size,mcore_pvc_conduit_three phase,mcore_pvc_conduit_single phase
2.5,25,30
4,33,39
6,42,50
10,55,66
16,73,86
25,94,112
35,114,136
50,136,162
70,170,202
95,208,243
120,237,282
150,266,317
185,304,363
240,359,421
300,404,483
400,468,548
500,522,628
630,#N/A,#N/A
   '''
   from io import StringIO
   f = StringIO(string)
   return f

def mcore_xlpe_unenclosed_amp():
   string = '''Size,mcore_xlpe_unenclosed space_three phase,mcore_xlpe_unenclosed space_single phase
2.5,28,34
4,38,45
6,48,57
10,66,78
16,88,104
25,119,140
35,147,173
50,180,211
70,229,268
95,283,331
120,330,385
150,377,441
185,436,509
240,517,604
300,594,694
400,685,804
500,779,915
630,#N/A,#N/A'''
   from io import StringIO
   f = StringIO(string)
   return f


def mcore_xlpe_dburied_amp():
   string = '''Size,mcore_xlpe_dburied_three phase,mcore_xlpe_dburied_single phase
2.5,29,34
4,37,45
6,46,56
10,63,75
16,110,132
25,143,170
35,172,205
50,204,244
70,251,300
95,302,360
120,344,410
150,385,460
185,435,520
240,504,603
300,567,680
400,640,771
500,714,862
630,#N/A,#N/A
   '''
   from io import StringIO
   f = StringIO(string)
   return f

def mcore_xlpe_conduit_amp():
   string = '''Size,mcore_xlpe_Conduit_three phase,mcore_xlpe_Conduit_single phase
2.5,29,34
4,37,45
6,46,56
10,63,75
16,81,98
25,107,128
35,130,154
50,155,185
70,193,228
95,233,279
120,270,318
150,304,365
185,348,413
240,411,485
300,463,558
400,524,633
500,601,728
630,#N/A,#N/A
'''
   from io import StringIO
   f = StringIO(string)
   return f

def score_pvc_unenclosed_amp():
   string = '''Size,score_pvc_unenclosed space_three phase,score_pvc_unenclosed space_single phase
2.5,25,29
4,33,39
6,42,49
10,58,67
16,77,89
25,103,119
35,127,145
50,156,177
70,197,223
95,246,276
120,287,321
150,330,367
185,383,424
240,457,505
300,529,582
400,615,676
500,710,780
630,817,897
   '''
   from io import StringIO
   f = StringIO(string)
   return f

def score_pvc_dburied_amp():
   string = '''Size,score_pvc_dburied_three phase,score_pvc_dburied_single phase
2.5,27,32
4,36,41
6,45,52
10,59,69
16,104,122
25,134,158
35,160,190
50,190,225
70,233,277
95,279,332
120,317,378
150,356,424
185,402,480
240,465,556
300,524,628
400,593,713
500,668,805
630,748,904
   '''
   from io import StringIO
   f = StringIO(string)
   return f

def score_pvc_conduit_amp():
   string = '''Size,score_pvc_conduit_three phase,score_pvc_conduit_single phase
2.5,27,32
4,36,41
6,45,52
10,59,69
16,78,89
25,100,116
35,122,139
50,144,168
70,180,206
95,217,252
120,252,287
150,283,329
185,325,373
240,377,438
300,434,496
400,492,575
500,571,649
630,639,750
   '''
   from io import StringIO
   f = StringIO(string)
   return f


def score_xlpe_unenclosed_amp():
   string = '''Size,score_xlpe_unenclosed space_three phase,score_xlpe_unenclosed space_single phase
2.5,30,36
4,40,47
6,50,60
10,69,82
16,92,108
25,125,145
35,154,177
50,188,216
70,240,273
95,298,338
120,349,393
150,403,451
185,468,522
240,560,622
300,648,718
400,756,836
500,874,966
630,1010,1113
   '''
   from io import StringIO
   f = StringIO(string)
   return f

def score_xlpe_dburied_amp():
   string = '''Size,score_xlpe_dburied_three phase,score_xlpe_dburied_single phase
2.5,31,36
4,40,46
6,50,58
10,67,78
16,117,139
25,151,179
35,180,215
50,214,255
70,262,313
95,313,375
120,356,427
150,400,480
185,452,543
240,523,630
300,589,711
400,668,808
500,752,913
630,843,1026
   '''
   from io import StringIO
   f = StringIO(string)
   return f

def score_xlpe_conduit_amp():
   string = '''Size,score_xlpe_conduit_three phase,score_xlpe_conduit_single phase
2.5,31,36
4,40,46
6,50,58
10,67,78
16,86,100
25,113,131
35,137,157
50,163,189
70,203,233
95,244,285
120,284,325
150,320,365
185,363,423
240,426,497
300,491,562
400,557,653
500,648,739
630,727,856
   '''
   from io import StringIO
   f = StringIO(string)
   return f

def earthsize():
   string = '''Size,Earth Size
mm2,mm2
2.5,2.5
4,2.5
6,2.5
10,4
16,6
25,6
35,10
50,16
70,25
95,25
120,35
150,50
185,70
240,95
300,120
400,120
500,120
630,120'''
   from io import StringIO
   f = StringIO(string)
   return f

def score_xlpe_ndiameter():
   string = '''single core XLPE,diameter mm
2.5,##
4,##
6,##
10,##
16,9.3
25,10.5
35,11.5
50,12.9
70,14.7
95,17.2
120,19.6
150,21.3
185,23.5
240,26.6
300,29.4
400,33.3
500,37
630,41.4
   '''
   from io import StringIO
   f = StringIO(string)
   return f

def score_pvc_ndiameter():
   string = '''single core XLPE,diameter mm
2.5,3.6
4,4.5
6,5.1
10,6.0
16,6.9
25,8.4
35,9.4
50,10.9
70,12.4
95,15.2
120,17.3
150,18.8
185,21.1
240,24.1
300,26.9
400,30.6
500,34.1
630,37.8
   '''
   from io import StringIO
   f = StringIO(string)
   return f


def mcore_pvc_ndiameter():
   string = '''Multicore PVC,diameter mm
2.5,13.5
4,15.5
6,17
10,19.3
16,21.6
25,##
35,##
50,##
70,##
95,##
120,##
150,##
185,##
240,##
300,##
400,##
500,##
630,##
   '''
   from io import StringIO
   f = StringIO(string)
   return f

def mcore_xlpe_ndiameter():
   string = '''Multicore XLPE,diameter mm
2.5,##
4,##
6,##
10,##
16,20.4
25,23.1
35,25.7
50,29.7
70,34.4
95,38.8
120,44.8
150,49.9
185,56.1
240,62.6
300,74.1
400,##
500,##
630,##
   '''
   from io import StringIO
   f = StringIO(string)
   return f
