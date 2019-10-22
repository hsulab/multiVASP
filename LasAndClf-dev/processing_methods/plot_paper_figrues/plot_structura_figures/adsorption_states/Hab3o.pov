#include "colors.inc"
#include "finish.inc"

global_settings {assumed_gamma 1 max_trace_level 6}
background {color White}
camera {perspective
  right -7.20*x up 7.20*y
  direction 50.00*z
  location <0,0,50.00> look_at <0,0,0>}
light_source {<  2.00,   3.00,  40.00> color White
  area_light <0.70, 0, 0>, <0, 0.70, 0>, 3, 3
  adaptive 1 jitter}

#declare simple = finish {phong 0.7}
#declare pale = finish {ambient .5 diffuse .85 roughness .001 specular 0.200 }
#declare intermediate = finish {ambient 0.3 diffuse 0.6 specular 0.10 roughness 0.04 }
#declare vmd = finish {ambient .0 diffuse .65 phong 0.1 phong_size 40. specular 0.500 }
#declare jmol = finish {ambient .2 diffuse .6 specular 1 roughness .001 metallic}
#declare ase2 = finish {ambient 0.05 brilliance 3 diffuse 0.6 metallic specular 0.70 roughness 0.04 reflection 0.15}
#declare ase3 = finish {ambient .15 brilliance 2 diffuse .6 metallic specular 1. roughness .001 reflection .0}
#declare glass = finish {ambient .05 diffuse .3 specular 1. roughness .001}
#declare glass2 = finish {ambient .0 diffuse .3 specular 1. reflection .25 roughness .001}
#declare Rcell = 0.100;
#declare Rbond = 0.200;

#macro atom(LOC, R, COL, TRANS, FIN)
  sphere{LOC, R texture{pigment{color COL transmit TRANS} finish{FIN}}}
#end
#macro constrain(LOC, R, COL, TRANS FIN)
union{torus{R, Rcell rotate 45*z texture{pigment{color COL transmit TRANS} finish{FIN}}}
      torus{R, Rcell rotate -45*z texture{pigment{color COL transmit TRANS} finish{FIN}}}
      translate LOC}
#end

atom(< -1.57,  -0.70,   0.00>, 0.26, rgb <1.00, 1.00, 1.00>, 0.0, ase3) // #0 
atom(<  0.93,   2.23, -12.73>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #1 
atom(<  0.93,  -0.69, -12.73>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #2 
atom(< -1.00,   0.77, -11.50>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #3 
atom(< -1.00,  -2.16, -11.50>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #4 
atom(<  2.87,   0.77, -11.50>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #5 
atom(<  2.87,  -2.16, -11.50>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #6 
atom(<  0.93,   2.23, -10.28>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #7 
atom(<  0.93,  -0.69, -10.28>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #8 
atom(< -2.23,   2.23,  -9.57>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #9 
atom(< -2.23,  -0.69,  -9.57>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #10 
atom(< -0.29,   0.77,  -8.34>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #11 
atom(< -0.29,  -2.16,  -8.34>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #12 
atom(<  2.16,   0.77,  -8.34>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #13 
atom(<  2.16,  -2.16,  -8.34>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #14 
atom(< -2.23,   2.23,  -7.12>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #15 
atom(< -2.23,  -0.69,  -7.12>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #16 
atom(<  0.93,   2.23,  -6.41>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #17 
atom(<  0.93,  -0.69,  -6.41>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #18 
atom(< -1.00,   0.76,  -5.18>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #19 
atom(< -1.00,  -2.15,  -5.18>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #20 
atom(<  2.86,   0.76,  -5.16>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #21 
atom(<  2.86,  -2.15,  -5.16>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #22 
atom(<  0.92,   2.23,  -3.99>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #23 
atom(<  0.90,  -0.69,  -3.96>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #24 
atom(< -2.18,   2.23,  -3.27>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #25 
atom(< -2.20,  -0.69,  -3.14>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #26 
atom(< -0.26,   0.85,  -1.80>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #27 
atom(< -0.26,  -2.24,  -1.80>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #28 
atom(<  2.19,   0.86,  -1.87>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #29 
atom(<  2.19,  -2.25,  -1.87>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #30 
atom(< -2.20,   2.23,  -0.72>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #31 
atom(< -2.27,  -0.69,  -0.67>, 0.56, rgb <1.00, 0.05, 0.05>, 0.0, ase3) // #32 
atom(< -2.23,   2.23, -11.50>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #33 
atom(< -2.23,  -0.69, -11.50>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #34 
atom(<  0.93,   0.77, -11.50>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #35 
atom(<  0.93,  -2.16, -11.50>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #36 
atom(< -2.23,   0.77,  -8.34>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #37 
atom(< -2.23,  -2.16,  -8.34>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #38 
atom(<  0.93,   2.23,  -8.34>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #39 
atom(<  0.93,  -0.69,  -8.34>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #40 
atom(< -2.23,   2.23,  -5.17>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #41 
atom(< -2.23,  -0.69,  -5.13>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #42 
atom(<  0.93,   0.76,  -5.21>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #43 
atom(<  0.93,  -2.15,  -5.21>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #44 
atom(< -2.20,   0.84,  -1.93>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #45 
atom(< -2.20,  -2.23,  -1.93>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #46 
atom(<  0.96,   2.23,  -2.14>, 1.20, rgb <0.09, 0.33, 0.53>, 0.0, ase3) // #47 
atom(<  0.97,  -0.69,  -2.01>, 1.02, rgb <0.40, 0.56, 0.56>, 0.0, ase3) // #48 
cylinder {< -2.27,  -0.69,  -0.67>, < -1.92,  -0.70,  -0.34>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -1.57,  -0.70,   0.00>, < -1.92,  -0.70,  -0.34>, Rbond texture{pigment {color rgb <1.00, 1.00, 1.00> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23, -11.50>, < -1.61,   1.50, -11.50>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.77, -11.50>, < -1.61,   1.50, -11.50>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23, -11.50>, < -2.23,   2.23, -10.54>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23,  -9.57>, < -2.23,   2.23, -10.54>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69, -11.50>, < -1.61,   0.04, -11.50>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.77, -11.50>, < -1.61,   0.04, -11.50>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69, -11.50>, < -1.61,  -1.42, -11.50>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -2.16, -11.50>, < -1.61,  -1.42, -11.50>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69, -11.50>, < -2.23,  -0.69, -10.54>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -9.57>, < -2.23,  -0.69, -10.54>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.77, -11.50>, <  0.93,   1.50, -12.12>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23, -12.73>, <  0.93,   1.50, -12.12>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.77, -11.50>, <  0.93,   0.04, -12.12>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69, -12.73>, <  0.93,   0.04, -12.12>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.77, -11.50>, < -0.03,   0.77, -11.50>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.77, -11.50>, < -0.03,   0.77, -11.50>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.77, -11.50>, <  1.90,   0.77, -11.50>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.87,   0.77, -11.50>, <  1.90,   0.77, -11.50>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.77, -11.50>, <  0.93,   1.50, -10.89>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23, -10.28>, <  0.93,   1.50, -10.89>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.77, -11.50>, <  0.93,   0.04, -10.89>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69, -10.28>, <  0.93,   0.04, -10.89>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16, -11.50>, <  0.93,  -1.42, -12.12>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69, -12.73>, <  0.93,  -1.42, -12.12>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16, -11.50>, < -0.03,  -2.16, -11.50>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -2.16, -11.50>, < -0.03,  -2.16, -11.50>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16, -11.50>, <  1.90,  -2.16, -11.50>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.87,  -2.16, -11.50>, <  1.90,  -2.16, -11.50>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.16, -11.50>, <  0.93,  -1.42, -10.89>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69, -10.28>, <  0.93,  -1.42, -10.89>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.77,  -8.34>, < -2.23,   1.50,  -8.96>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23,  -9.57>, < -2.23,   1.50,  -8.96>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.77,  -8.34>, < -2.23,   0.04,  -8.96>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -9.57>, < -2.23,   0.04,  -8.96>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.77,  -8.34>, < -1.26,   0.77,  -8.34>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,   0.77,  -8.34>, < -1.26,   0.77,  -8.34>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.77,  -8.34>, < -2.23,   1.50,  -7.73>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23,  -7.12>, < -2.23,   1.50,  -7.73>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   0.77,  -8.34>, < -2.23,   0.04,  -7.73>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -7.12>, < -2.23,   0.04,  -7.73>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.16,  -8.34>, < -2.23,  -1.42,  -8.96>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -9.57>, < -2.23,  -1.42,  -8.96>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.16,  -8.34>, < -1.26,  -2.16,  -8.34>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -2.16,  -8.34>, < -1.26,  -2.16,  -8.34>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -2.16,  -8.34>, < -2.23,  -1.42,  -7.73>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -7.12>, < -2.23,  -1.42,  -7.73>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23,  -8.34>, <  0.93,   2.23,  -9.31>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23, -10.28>, <  0.93,   2.23,  -9.31>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23,  -8.34>, <  0.32,   1.50,  -8.34>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,   0.77,  -8.34>, <  0.32,   1.50,  -8.34>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23,  -8.34>, <  1.54,   1.50,  -8.34>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,   0.77,  -8.34>, <  1.54,   1.50,  -8.34>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23,  -8.34>, <  0.93,   2.23,  -7.38>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23,  -6.41>, <  0.93,   2.23,  -7.38>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -8.34>, <  0.93,  -0.69,  -9.31>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69, -10.28>, <  0.93,  -0.69,  -9.31>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -8.34>, <  0.32,   0.04,  -8.34>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,   0.77,  -8.34>, <  0.32,   0.04,  -8.34>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -8.34>, <  0.32,  -1.42,  -8.34>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.29,  -2.16,  -8.34>, <  0.32,  -1.42,  -8.34>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -8.34>, <  1.54,   0.04,  -8.34>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,   0.77,  -8.34>, <  1.54,   0.04,  -8.34>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -8.34>, <  1.54,  -1.42,  -8.34>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.16,  -2.16,  -8.34>, <  1.54,  -1.42,  -8.34>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -8.34>, <  0.93,  -0.69,  -7.37>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -6.41>, <  0.93,  -0.69,  -7.37>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23,  -5.17>, < -2.23,   2.23,  -6.14>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23,  -7.12>, < -2.23,   2.23,  -6.14>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23,  -5.17>, < -1.62,   1.49,  -5.18>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.76,  -5.18>, < -1.62,   1.49,  -5.18>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,   2.23,  -5.17>, < -2.21,   2.23,  -4.22>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.18,   2.23,  -3.27>, < -2.21,   2.23,  -4.22>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -5.13>, < -2.23,  -0.69,  -6.13>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -7.12>, < -2.23,  -0.69,  -6.13>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -5.13>, < -1.62,   0.03,  -5.16>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.76,  -5.18>, < -1.62,   0.03,  -5.16>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -5.13>, < -1.62,  -1.42,  -5.16>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -2.15,  -5.18>, < -1.62,  -1.42,  -5.16>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.23,  -0.69,  -5.13>, < -2.21,  -0.69,  -4.14>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,  -0.69,  -3.14>, < -2.21,  -0.69,  -4.14>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.76,  -5.21>, <  0.93,   1.50,  -5.81>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   2.23,  -6.41>, <  0.93,   1.50,  -5.81>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.76,  -5.21>, <  0.93,   0.04,  -5.81>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -6.41>, <  0.93,   0.04,  -5.81>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.76,  -5.21>, < -0.04,   0.76,  -5.20>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,   0.76,  -5.18>, < -0.04,   0.76,  -5.20>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.76,  -5.21>, <  1.89,   0.76,  -5.19>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.86,   0.76,  -5.16>, <  1.89,   0.76,  -5.19>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.76,  -5.21>, <  0.92,   1.50,  -4.60>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.92,   2.23,  -3.99>, <  0.92,   1.50,  -4.60>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,   0.76,  -5.21>, <  0.91,   0.04,  -4.59>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.90,  -0.69,  -3.96>, <  0.91,   0.04,  -4.59>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.15,  -5.21>, <  0.93,  -1.42,  -5.81>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -0.69,  -6.41>, <  0.93,  -1.42,  -5.81>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.15,  -5.21>, < -0.04,  -2.15,  -5.20>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -1.00,  -2.15,  -5.18>, < -0.04,  -2.15,  -5.20>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.15,  -5.21>, <  1.89,  -2.15,  -5.19>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.86,  -2.15,  -5.16>, <  1.89,  -2.15,  -5.19>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.93,  -2.15,  -5.21>, <  0.91,  -1.42,  -4.59>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.90,  -0.69,  -3.96>, <  0.91,  -1.42,  -4.59>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,   0.84,  -1.93>, < -2.19,   1.53,  -2.60>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.18,   2.23,  -3.27>, < -2.19,   1.53,  -2.60>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,   0.84,  -1.93>, < -2.20,   0.07,  -2.53>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,  -0.69,  -3.14>, < -2.20,   0.07,  -2.53>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,   0.84,  -1.93>, < -1.23,   0.85,  -1.86>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,   0.85,  -1.80>, < -1.23,   0.85,  -1.86>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,   0.84,  -1.93>, < -2.20,   1.53,  -1.32>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,   2.23,  -0.72>, < -2.20,   1.53,  -1.32>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,   0.84,  -1.93>, < -2.23,   0.07,  -1.30>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.27,  -0.69,  -0.67>, < -2.23,   0.07,  -1.30>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,  -2.23,  -1.93>, < -2.20,  -1.46,  -2.53>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,  -0.69,  -3.14>, < -2.20,  -1.46,  -2.53>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,  -2.23,  -1.93>, < -1.23,  -2.23,  -1.86>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,  -2.24,  -1.80>, < -1.23,  -2.23,  -1.86>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {< -2.20,  -2.23,  -1.93>, < -2.23,  -1.46,  -1.30>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -2.27,  -0.69,  -0.67>, < -2.23,  -1.46,  -1.30>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.96,   2.23,  -2.14>, <  0.94,   2.23,  -3.06>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  0.92,   2.23,  -3.99>, <  0.94,   2.23,  -3.06>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.96,   2.23,  -2.14>, <  0.35,   1.54,  -1.97>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,   0.85,  -1.80>, <  0.35,   1.54,  -1.97>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.96,   2.23,  -2.14>, <  1.58,   1.54,  -2.00>, Rbond texture{pigment {color rgb <0.09, 0.33, 0.53> transmit 0.0} finish{ase3}}}
cylinder {<  2.19,   0.86,  -1.87>, <  1.58,   1.54,  -2.00>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.97,  -0.69,  -2.01>, <  0.94,  -0.69,  -2.99>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  0.90,  -0.69,  -3.96>, <  0.94,  -0.69,  -2.99>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.97,  -0.69,  -2.01>, <  0.35,   0.08,  -1.91>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,   0.85,  -1.80>, <  0.35,   0.08,  -1.91>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.97,  -0.69,  -2.01>, <  0.35,  -1.47,  -1.90>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {< -0.26,  -2.24,  -1.80>, <  0.35,  -1.47,  -1.90>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.97,  -0.69,  -2.01>, <  1.58,   0.08,  -1.94>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  2.19,   0.86,  -1.87>, <  1.58,   0.08,  -1.94>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
cylinder {<  0.97,  -0.69,  -2.01>, <  1.58,  -1.47,  -1.94>, Rbond texture{pigment {color rgb <0.40, 0.56, 0.56> transmit 0.0} finish{ase3}}}
cylinder {<  2.19,  -2.25,  -1.87>, <  1.58,  -1.47,  -1.94>, Rbond texture{pigment {color rgb <1.00, 0.05, 0.05> transmit 0.0} finish{ase3}}}
