================================================
  NLOC    CCN   token  PARAM  length  location  
------------------------------------------------
       3      1     31      2       3 update_yaml@6-8@src/dda/yaml/set.py
       7      2     60      2       7 load_yaml@10-16@src/dda/yaml/set.py
      17      6    106      2      17 complete_yaml@18-34@src/dda/yaml/set.py
      32      6    308      5      38 draw_aim@10-47@src/dda/draw/aim.py
      31      4    334      8      31 visualize_progress@11-41@src/dda/draw/progress.py
       8      2     69      0      10 _create_dummy@47-56@src/dda/draw/progress.py
       2      1      6      0       2 hello@1-2@src/dda/__init__.py
      17      5     89      1      17 set_aim@14-30@src/dda/sub_main.py
      20      5     88      3      20 _communicate_interactive_via_key@32-51@src/dda/sub_main.py
      24      8    143      1      24 _update_aim@53-76@src/dda/sub_main.py
      33     10    259      1      36 update_progress@78-113@src/dda/sub_main.py
      10      1    100      3      10 draw_from_yaml@115-124@src/dda/sub_main.py
      32      6    241      0      33 main@7-39@src/dda/main.py
7 file analyzed.
==============================================================
NLOC    Avg.NLOC  AvgCCN  Avg.token  function_cnt    file
--------------------------------------------------------------
      0       0.0     0.0        0.0         0     src/dda/yaml/__init__.py
     30       9.0     3.0       65.7         3     src/dda/yaml/set.py
     55      32.0     6.0      308.0         1     src/dda/draw/aim.py
     57      19.5     3.0      201.5         2     src/dda/draw/progress.py
      2       2.0     1.0        6.0         1     src/dda/__init__.py
    119      20.8     5.8      135.8         5     src/dda/sub_main.py
     38      32.0     6.0      241.0         1     src/dda/main.py

===============================================================================================================
No thresholds exceeded (cyclomatic_complexity > 15 or length > 1000 or nloc > 1000000 or parameter_count > 100)
==========================================================================================
Total nloc   Avg.NLOC  AvgCCN  Avg.token   Fun Cnt  Warning cnt   Fun Rt   nloc Rt
------------------------------------------------------------------------------------------
       301      18.2     4.4      141.1       13            0      0.00    0.00
